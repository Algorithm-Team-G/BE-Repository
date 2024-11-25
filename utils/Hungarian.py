import random
from datetime import datetime

import numpy as np
from pandas import DataFrame

from entity.Task import Task
from entity.Worker import Worker


class Hungarian:
    @staticmethod
    def createGraph(workers: list[Worker], tasks: list[Task]) -> DataFrame:
        workerCount = len(workers)
        taskCount = len(tasks)
        if workerCount > taskCount:
            workers.sort(key=lambda x: (x.taskCount, x.career))
            workers = workers[:taskCount]
        elif workerCount < taskCount:
            workers.sort(key=lambda x: (x.taskCount, x.career))
            while workerCount < taskCount:
                diff = taskCount - workerCount
                diff = diff if diff < len(workers) else len(workers)
                workers += workers[:diff]
                workerCount += diff

        instance = Hungarian()
        graph = DataFrame(0.0, index=[worker.id for worker in workers], columns=[task.id for task in tasks])
        # graph = DataFrame(0.0, index=[worker for worker in workers], columns=[task for task in tasks])
        for worker in workers:
            for task in tasks:
                graph.at[worker.id, task.id] = instance.__getScore(worker, task)
                # graph.at[worker, task] = random.randint(1, 20)
        return graph

    @staticmethod
    def solve(graph:DataFrame) -> tuple:
        instance = Hungarian()
        pos = instance.__mainAlgorithm(graph.copy())
        total, ans_matrix = instance.__findAnswer(graph.copy(), pos)
        return pos, total, ans_matrix

    def __getScore(self, worker: Worker, task: Task) -> float:
        """
        워커 W에거 업무 T를 분배하는 것이 적절한지 계산하는 함수

        [점수를 계산하는 지표]
        1. T의 마감 날짜가 급한 경우
        2. T의 중요도가 높은 경우
        3. T의 작업 기간이 짧은 경우
        4. T의 Level이 W의 career와 적절한 경우
        5. W와 T의 직군이 같은 경우

        [점수 계산식]
        (* 가중치를 최소화하는 방향으로)
        """

        # p1. T의 마감 날짜가 급한 경우 (작은 게 이득)
        p1 = (task.end - datetime.today()).days

        # p2. T의 중요도가 높은 경우 (큰 게 이득)
        p2 = task.importance

        # p3. T의 작업 기간이 짧은 경우 (작은 게 이득)
        p3 = (task.end - task.begin).days

        # p4. T의 Level이 W의 career와 적절한 경우 (큰 게 이득)
        p4 = worker.career / task.level

        # p5. W와 T의 직군이 같은 경우 (작은 게 이득)
        p5 = 0 if worker.jobId == task.jobId else 1

        return (p1 + p3 + p5) / (p2 + p4)

    def __minZeroRow(self, zeros, coorZero):
        min_row = [99999, -1]

        for row_index in range(zeros.shape[0]):
            if np.sum(zeros[row_index] == True) > 0 and min_row[0] > np.sum(zeros[row_index] == True):
                # 만약 각 열에서 0인 부분이 이전 열의 그것보다 적다면
                min_row = [np.sum(zeros[row_index] == True), row_index]
                # 0의 개수로 최솟값을 가지는 열은 그 열로 한다.

        zero_index = np.where(zeros[min_row[1]] == True)[0][0]  # 0의 개수가 최소인 열의 값들 중 제일 위에 있는 0의 y값(열번호)를 저장합니다.
        coorZero.append((min_row[1], zero_index))  # 해당하는 그 값의 좌표를 저장합니다.
        zeros[min_row[1], :] = False  # 최소였던 열의 전부를 False로 바꿉니다.
        zeros[:, zero_index] = False  # 최소였던 행의 전부를 False로 바꿉니다. 이렇게 해서 다른 것이 중복지정되지 않도록 합니다.

    def __markMatrix(self, listing) -> tuple:
        current_listing = listing
        bool_listing = (current_listing == 0)
        bool_listing_copy = bool_listing.copy()

        # 가능한 경우의 수를 모두 계산합니다.

        zero_coordinate = []

        while (True in bool_listing_copy):  # 배분표에 적어도 0이 하나라도 존재한다면 계속 계산
            self.__minZeroRow(bool_listing_copy, zero_coordinate)

        # 각 경우의 좌표값을 행과 열로 각각 분리합니다.

        zero_coordinate_row = []
        zero_coordinate_col = []

        for i in range(len(zero_coordinate)):
            zero_coordinate_row.append(zero_coordinate[i][0])
            zero_coordinate_col.append(zero_coordinate[i][1])

        # 0을 포함하지 않는 열을 저장합니다.

        no_zero_row = list(set(range(current_listing.shape[0])) - set(zero_coordinate_row))

        si_ceros_col = []
        state = True

        while state:

            state = False

            for i in range(len(no_zero_row)):

                row_arr = bool_listing[no_zero_row[i], :]

                for j in range(row_arr.shape[0]):

                    if row_arr[
                        j] == True and j not in si_ceros_col:  # 0을 포함하지 않는 열의 요소들을 찾고, 그 요소들을 포함하는 행에 0이 있는지 확인합니다.

                        si_ceros_col.append(j)  # 그 요소들을 포함하는 행에 0을 포함하면, 그 행 번호를 저장합니다.
                        state = True

            for row_index, col_index in zero_coordinate:

                if row_index not in no_zero_row and col_index in si_ceros_col:  # 그 값이 위치한 열에는 0이 없는데 행에는 0이 있는 위치라면

                    no_zero_row.append(row_index)  # 그 열 값을 저장
                    state = True

        si_ceros_row = list(set(range(listing.shape[0])) - set(no_zero_row))

        return zero_coordinate, si_ceros_row, si_ceros_col

    def __adjustMatrix(self, listing, si_rows, si_cols):
        current_listing = listing
        no_zero_element = []

        for row in range(len(current_listing)):  # 각 선이 차지하지 않은 영역의 최솟값을 찾습니다.
            if row not in si_rows:
                for i in range(len(current_listing[row])):
                    if i not in si_cols:
                        no_zero_element.append(current_listing[row][i])

        minimum = min(no_zero_element)

        for row in range(len(current_listing)):  # 각 선이 차지하지 않은 영역의 값들을 그 영역의 최솟값으로 빼줍니다.
            if row not in si_rows:
                for i in range(len(current_listing[row])):
                    if i not in si_cols:
                        current_listing[row, i] -= minimum

        for row in range(len(si_rows)):  # 체크된 행과 열에 모두 포함되는 값에 그 최솟값을 더해줍니다.
            for col in range(len(si_cols)):
                current_listing[si_rows[row], si_cols[col]] += minimum

        return current_listing

    def __mainAlgorithm(self, graph: DataFrame):
        listing = graph.to_numpy()
        current_listing = listing

        for row_index in range(listing.shape[0]):
            current_listing[row_index] -= np.min(current_listing[row_index])

        for col_index in range(listing.shape[1]):
            current_listing[:, col_index] -= np.min(current_listing[:, col_index])

        zero_count = 0

        while zero_count < listing.shape[0]:  # 각 행과 열에서 0을 최대로 하는 곳을 찾습니다.
            ans_pos, RowCount, ColCount = self.__markMatrix(current_listing)
            zero_count = len(RowCount) + len(ColCount)

            if zero_count < listing.shape[0]:
                current_listing = self.__adjustMatrix(current_listing, RowCount, ColCount)

        return ans_pos

    def __findAnswer(self, graph, pos):
        listing = graph.to_numpy()
        total = 0
        ans_matrix = np.zeros((listing.shape[0], listing.shape[1]))
        for i in range(len(pos)):
            total += listing[pos[i][0], pos[i][1]]
            ans_matrix[pos[i][0], pos[i][1]] = listing[pos[i][0], pos[i][1]]

        return total, ans_matrix