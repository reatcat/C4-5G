# -*- coding: utf-8 -*-

import pandas as pd
import DataProcessing as dp
import numpy as np
import csv
from spmf.mining import *
from CPT import *
import operator
import matplotlib.pyplot as plt
file_path = '.\\t_alarmlogcur.csv'

if __name__ == '__main__':
    data = dp.read_data(file_path)
    print('数据内部清洗前长度为', len(data))
    level0, level1, level2, level3 = dp.getdataByalarmlevel(data)
    print("提示告警信息有" + str(level0) + "条")
    print("次要告警信息有" + str(level1) + "条")
    print("主要告警信息有" + str(level2) + "条")
    print("紧急告警信息有" + str(level3) + "条")


    # 数据和标签
    labels = ['Prompt alarm', 'Minor alarm', 'Major alarm', 'Critical alarm']
    sizes = [level0, level1, level2, level3]

    # 绘制饼状图
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    # 添加标题
    plt.title('Alarm Levels')

    # 显示图形
    plt.show()
