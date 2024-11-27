import json

from flask import Response

from dto.request.TaskDTO import TaskDTO
from dto.request.WorkerTasksDTO import WorkerTasksDTO
from entity.Task import Task
from entity.Worker import Worker
from repository.TaskRepository import TaskRepository
from repository.TeamRepository import TeamRepository
from repository.WorkerRepository import WorkerRepository
from utils.Graph import Graph
from utils.Hungarian import Hungarian


class TaskService:
    def __init__(self):
        self.repo = TaskRepository()

    def getAssignedTaskList(self) -> Response:
        result = self.repo.selectAssignedTasks()
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')

    def getUnassignedTaskList(self) -> Response:
        result = self.repo.selectUnassignedTasks()
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')

    def addTask(self, task:TaskDTO):
        result = self.repo.createNewTask(task)
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')

    def assignTask(self, workerTaskList:list[WorkerTasksDTO]):
        for workerTask in workerTaskList:
            for taskId in workerTask.tasks:
                self.repo.assignTask(taskId, workerTask.workerId)
        return Response(status=200)

    def recommendDistributionTasks(self, tasks:list[int]):
        # 조직에 개설된 팀 ID 불러오기
        teamData = TeamRepository().selectTeam()
        taskData = {}
        workerData = {}
        for teamId, _ in teamData:
            # 팀에 따라 분배해야 하는 업무 불러오기
            loadedTasks = TaskRepository().selectTasksByTeam(tasks, teamId)
            taskData[teamId] = [Task.fromJson(json.dumps(task, ensure_ascii=False)) for task in loadedTasks]

            # 팀에 따라 업무를 할당받을 워커들 불러오기
            loadedWorkers = WorkerRepository().selectFreeWorkersByTeam(teamId)
            workerData[teamId] = [Worker.fromJson(json.dumps(worker, ensure_ascii=False)) for worker in loadedWorkers]

        # 기준에 따라 업무 분배
        result = []
        for std in [Graph.deadline, Graph.importance, Graph.suitability]:
            case = {}
            for teamId, teamName in teamData:
                # graph 생성 & 알고리즘 실행
                graph = Graph(std).create(workerData[teamId], taskData[teamId])
                pos, minCost, matchingResult = Hungarian.solve(graph)
                pos.sort(key = lambda x : x[0])

                # formatting & save
                teamDistribution = {}
                teamDistribution['name'] = teamName
                teamDistribution['workers'] = {}
                for x, y in pos:
                    workerId = graph.index[x]
                    taskId = graph.columns[y]
                    if workerId not in teamDistribution['workers']:
                        teamDistribution['workers'][workerId] = []
                    task = next(task for task in taskData[teamId] if task.id == taskId)
                    teamDistribution['workers'][workerId].append({'id': taskId, 'name': task.name})
                case[teamId] = teamDistribution

            result.append(case)

        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')