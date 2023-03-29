# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import values

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
    labels_pie = ['Prompt alarm', 'Minor alarm', 'Major alarm', 'Critical alarm']
    sizes_pie = [level0, level1, level2, level3]

    # 绘制饼状图
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes_pie, labels=labels_pie, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    ax1.set_title('Alarm Levels (Pie Chart)')

    # 柱状图数据和标签
    labels_bar = ['Prompt alarm', 'Minor alarm', 'Major alarm', 'Critical alarm']
    values_bar = [level0, level1, level2, level3]

    # 绘制柱状图
    fig2, ax2 = plt.subplots()
    ax2.bar(labels_bar, values_bar)
    ax2.set_title('Alarm Levels (Bar Chart)')
    ax2.set_xlabel('Alarm Level')
    ax2.set_ylabel('Number of Alarms')

    # 显示图形
    plt.show()
