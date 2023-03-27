# -*- coding: utf-8 -*-
# @Time : 2023/3/25 21:21
# @Author : Zhangmiaosong
import pickle
import DataProcessing as dp


if __name__ == '__main__':
    # 从文件中加载模型
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # 从文件中读取变量
    with open("locs.pkl", "rb") as f:
        locs = pickle.load(f)
    with open("locToIndexOflocs.pkl", "rb") as f:
        locToIndexOflocs = pickle.load(f)
    with open("locstoneid.pkl", "rb") as f:
        locstoneid = pickle.load(f)



        data = []
        Seqs = dp.GenSeqs(data, 1000)

        for i in range(len(Seqs)):
            for j in range(len(Seqs[i])):
                Seqs[i][j] = list(set(map(lambda x: x, [locToIndexOflocs[x[5]] for x in Seqs[i][j]])))  # 序列中项集中的项为设备定位信息
            Seqs[i] = dp.Seq_compression(Seqs[i])
            # 按序列长度排个序
        Seqs = sorted(Seqs, key=lambda x: len(x))
        test = []


        pred = model.predict(test)