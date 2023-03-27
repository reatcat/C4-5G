# -*- coding: utf-8 -*-
# @Time : 2023/3/25 21:20
# @Author : Zhangmiaosong
# -*- coding: utf-8 -*-
# @Time : 2023/3/21 20:52
# @Author : Zhangmiaosong
import pickle

import pandas as pd
import DataProcessing as dp
import numpy as np
import csv
from spmf.mining import *
from CPT import *
import operator
# 保存挖掘出的频繁序列
output_freseqs_path = '.\\output\\freseq.csv'
# 保存挖掘出的规则项集
output_assorules_path = '.\\output\\assorules.csv'

file_path = '.\\t_alarmloghist_1_1.csv'
output_path = '.\\output\\predict_rusult.csv'
if __name__ == '__main__':
    # 数据输入
    data = dp.read_data(file_path)
    print('数据内部清洗前长度为', len(data))
    # 清洗数据，按照时间，端口号等进行聚类
    data = dp.Datacluster(data,eps = 0.005)


    #  所有数据的clocationinfo信息列表locs，反索引列表locToIndexOflocs，loc对应的网元id、端口信息、定位信息列表locstoneid
    locs, locToIndexOflocs, locstoneid = dp.getContextofLocs(data)

    # 保存变量到文件
    with open("locs.pkl", "wb") as f:
        pickle.dump(locs, f)
    with open("locToIndexOflocs.pkl", "wb") as f:
        pickle.dump(locToIndexOflocs, f)
    with open("locstoneid.pkl", "wb") as f:
        pickle.dump(locstoneid, f)

    ## 生成所有时间序列
    Seqs = dp.GenSeqs(data, 100)


    # 对序列进行字符串化,去除序列中每个项目集的重复项
    for i in range(len(Seqs)):
        for j in range(len(Seqs[i])):
            Seqs[i][j] = list(set(map(lambda x:x,[locToIndexOflocs[x[5]] for x in Seqs[i][j]])))  # 序列中项集中的项为设备定位信息
        Seqs[i] = dp.Seq_compression(Seqs[i])
    # 按序列长度排个序
    Seqs = sorted(Seqs,key = lambda x: len(x))
    maxseqlen = max([len(Seq) for Seq in Seqs])

    ## 频繁序列挖掘 SPAM
    freqSeqs = Mining_FreSeqPatterns(Seqs,minsp=12/len(Seqs),minpatternlen=2,maxpatternlen=10,maxgap=100)
    freqSeqs = sorted(freqSeqs,key = lambda x: x[-1])
    # 保存挖掘出的频繁序列
    column_Seq = pd.Series([x[0] for x in freqSeqs],name='Seq')
    column_Seq_detailed = pd.Series([[[locstoneid[locs[int(item)]] for item in items] for items in x[0]] for x in freqSeqs],name='Seq_detailed') #具体点的
    column_sup = pd.Series([x[1] for x in freqSeqs],name='sup')
    con = pd.concat([column_Seq,column_Seq_detailed,column_sup],axis=1)
    con.to_csv(output_freseqs_path,index = True,sep=',',mode='w+',encoding='utf_8_sig')

    ## 序列预测 CPT
    Seqs = dp.Seqs_dim_reduction(Seqs)

    # 筛掉只有长度为1的序列（长度都为1了还预测个啥QAQ）
    Seqs = [seq for seq in Seqs if len(seq) > 1]

    model = CPT()

    train = Seqs

    model.train(train)
    print("训练完成")
    # 使用Python的pickle模块将模型对象序列化成二进制数据并写入文件

    # 保存模型到文件
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
