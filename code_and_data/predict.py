# -*- coding: utf-8 -*-
# @Time : 2023/3/25 21:21
# @Author : Zhangmiaosong
import operator
import pickle
import DataProcessing as dp


if __name__ == '__main__':
    # 从文件中加载模型
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # 从文件中读取变量
    with open("locs.pkl", "rb") as f:
        locs = pickle.load(f)
    with open("train.pkl", "rb") as f:
        train = pickle.load(f)
        # train, test = dp.data_split(train, 1000)
        # truth = [[x[-1]] for x in test]
        # test = [x[:-1] for x in test]
        # p = model.predict(train, test, 5, 10)
        # right, wrong = 0, 0
        # part_right = 0
        # for i in range(len(p)):
        #     if operator.eq(p[i], truth[i]):
        #         right += 1
        #     elif len(set(p[i]).intersection(set(truth[i]))) == 0:  # 如果没有交集
        #         # elif len(set(tuple(p[i])).intersection(set(tuple(truth[i])))) == 0:
        #         wrong += 1
        #     else:
        #         part_right += 1
        #
        # result = ([locs[i] for i in itemset] for itemset in p)
        # result_list = list(result)
        # for i in range(100):
        #     print(result_list[i])
        # print(
        #     f'right = {right}/{right + wrong + part_right}, wrong = {wrong}/{right + wrong + part_right},part_right = {part_right}/{right + wrong + part_right}')
        # print(f'有{len(test) - right - wrong - part_right}条序列未作出预测')
        # print("请输入一条数据")
        # data = input()
        # Seqs = dp.GenSeqs(data, 1000)
        #
        # for i in range(len(Seqs)):
        #     for j in range(len(Seqs[i])):
        #         Seqs[i][j] = list(set(map(lambda x: x, [locToIndexOflocs[x[5]] for x in Seqs[i][j]])))  # 序列中项集中的项为设备定位信息
        #     Seqs[i] = dp.Seq_compression(Seqs[i])
        #     # 按序列长度排个序
        # test = sorted(Seqs, key=lambda x: len(x))

        #
        # pred = model.predict(test)