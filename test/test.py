import random
from datetime import datetime, timedelta

from entity.Task import Task
from entity.Worker import Worker
from utils.Graph import Graph
from utils.Hungarian import Hungarian

worker_size = 10
task_size = 6

workers = []
tasks = []
print("================ workers ====================")
for i in range(worker_size):
    career = random.randint(0, 10)
    teamId = random.randint(0, 4)
    jobId = random.randint(0, 20)
    taskCount = random.randint(0, 5)
    workers.append(Worker(i, f"워커{i}", career, teamId, jobId, taskCount, 5))
    print(f"""
< 워커{i} >
- 팀: {teamId}
- 직군: {jobId}
- 경력: {career}
- 현재 담당 업무 수: {taskCount}
""")
print("================ tasks ====================")
for i in range(task_size):
    teamId = random.randint(0, 4)
    jobId = random.randint(0, 20)
    level = random.randint(1, 5)
    importance = random.randint(1, 5)
    begin = datetime.now() + timedelta(days=random.randint(0, 8))
    end = begin + timedelta(days=random.randint(0, 10))
    tasks.append(Task(i, f"업무{i}", teamId, jobId, begin, end, importance, level))
    print(f"""
< 업무{i} >
- 팀: {teamId}
- 직군: {jobId}
- 난이도: {level}
- 중요도: {importance}
- 시작일: {begin}
- 마감일: {end}
""")

print("================== graph =====================")
weightStandard = int(input("기준을 선택해주세요. (0: deadline, 1: importance, 2: suitability): "))
graph = Graph(weightStandard).create(workers, tasks)
print(f"\n그래프:\n{graph}")

pos, minCost, matchingResult = Hungarian.solve(graph)

print("==============================================")
print("이런 상황에서, " + str(minCost) + " 의 최소비용으로 일을 처리할 수 있습니다.")
print("배분은 다음과 같습니다.")
print("==============================================")

pos.sort(key = lambda x : x[0])
finalResult = {}
for x, y in pos:
    workerId = graph.index[x]
    taskId = graph.columns[y]
    if workerId not in finalResult:
        finalResult[workerId] = []
    finalResult[workerId].append(int(taskId))

for workerId in sorted(finalResult.keys()):
    print(f"워커{workerId}: {finalResult[workerId]}")