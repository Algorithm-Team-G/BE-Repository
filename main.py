from flask import Flask
from flask_restx import Api

from controller.TaskController import TaskNamespace

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

api = Api(app)
api.add_namespace(TaskNamespace, "/task")

if __name__ == '__main__':
    app.run()


# from utils.Hungarian import Hungarian
#
# worker_size = 8
# task_size = 6
#
# workers = [i for i in range(worker_size)]
# tasks = [i for i in range(task_size)]
#
# graph = Hungarian.createGraph(workers, tasks)
#
# print(f"workers: {workers}")
# print(f"tasks: {tasks}")
# print(f"graph:\n{graph}\n")
#
# pos, minCost, matchingResult = Hungarian.solve(graph)
#
# print("==============================================")
# print("이런 상황에서, " + str(minCost) + " 의 최소비용으로 일을 처리할 수 있습니다.")
# print("배분은 다음과 같습니다.")
# print("==============================================")
#
# # alpabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# #
# # pos.sort(key = lambda x : x[0])
# #
# # for x, y in pos:
# #     print(f'워커{alpabets[x%26]}에는 작업{y+1}를 배분해줍니다.')
# #
# # print(pos)
# # print(matchingResult)
#
# pos.sort(key = lambda x : x[0])
# finalResult = {}
# for x, y in pos:
#     workerId = graph.index[x]
#     taskId = graph.columns[y]
#     if workerId not in finalResult:
#         finalResult[workerId] = []
#     finalResult[workerId].append(int(taskId))
#
# for workerId, tasks in finalResult.items():
#     print(f'워커{workerId}: {tasks}')