from datetime import datetime

from pandas import DataFrame

from entity.Task import Task
from entity.Worker import Worker


class Graph:
    # 가중치 계산 시, 가중치의 기준
    deadline = 0
    importance = 1
    suitability = 2

    def __init__(self, std:int):
        if std not in [0, 1, 2]:
            raise ValueError("Invalid weightStandard value")

        self.sortingFunc = lambda x: (x.taskCount, x.career)

        self.weights = []
        if std == Graph.deadline:
            self.weights = [0.1, 0.5, 0.3, 0.5, 1]
        elif std == Graph.importance:
            self.weights = [0.2, 1.0, 0.5, 0.7, 1]
        else:
            self.weights = [0.4, 0.8, 0.4, 1.0, 1]

    def create(self, workers: list[Worker], tasks: list[Task]) -> DataFrame:
        workerCount = len(workers)
        taskCount = len(tasks)
        if workerCount != taskCount:
            workers.sort(key=self.sortingFunc)
            if workerCount > taskCount:
                workers = workers[:taskCount]
            else:
                while workerCount < taskCount:
                    diff = taskCount - workerCount
                    diff = diff if diff < len(workers) else len(workers)
                    workers += workers[:diff]
                    workerCount += diff

        graph = DataFrame(0.0, index=[worker.id for worker in workers], columns=[task.id for task in tasks])
        # graph = DataFrame(0.0, index=[worker for worker in workers], columns=[task for task in tasks])
        for worker in workers:
            for task in tasks:
                graph.at[worker.id, task.id] = self.__getScore(worker, task)
                # graph.at[worker, task] = random.randint(1, 20)
        return graph

    def __getScore(self, worker: Worker, task: Task) -> float:
        """
        워커 W에거 업무 T를 분배하는 것이 적절한지 계산하는 함수

        [점수를 계산하는 지표]
        1. T의 마감 날짜가 급한 경우 (S)
        2. T의 중요도가 높은 경우 (B)
        3. T의 작업 기간이 짧은 경우 (S)
        4. W의 career 경력이 높은 경우 (B)
        5. W와 T의 직군이 같은 경우 (S)

        [점수 계산식]
        (* 가중치를 최소화하는 방향으로)
        """

        # p1. T의 마감 날짜가 급한 경우 (작은 게 이득)
        p1 = (task.end - datetime.today()).days * self.weights[0]

        # p2. T의 중요도가 높은 경우 (큰 게 이득)
        p2 = task.importance * self.weights[1]

        # p3. T의 작업 기간이 짧은 경우 (작은 게 이득)
        p3 = (task.end - task.begin).days * self.weights[2]

        # p4. T의 Level이 W의 career와 적절한 경우 (큰 게 이득)
        p4 = worker.career / task.level * self.weights[3]

        # p5. W와 T의 직군이 같은 경우 (작은 게 이득)
        p5 = (0 if worker.jobId == task.jobId else 1) * self.weights[4]

        return (p1 + p3 + p5) / (p2 + p4)