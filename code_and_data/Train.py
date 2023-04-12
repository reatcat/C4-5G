# -*- coding: utf-8 -*-
# @Time : 2023/3/21 22:52
# @Author : Zhangmiaosong
import pandas as pd
def read_data(file_path):
    '''读取初始表数据，先转成csv格式'''
    df = pd.read_csv( \
        file_path, usecols=[0, 6, 8, 13, 16, 21, 22], \
        dtype={ \
            'clogid': int, \
            'calarmcode': int, \
            'cneid': int, \
            'calarmlevel': int, \
            'coccuructime': object, \
            'clocationinfo': object, \
            'clinport': object \
            }, \
        low_memory=False, encoding="gbk")
    data = df.values
    return data
def getdataByalarmlevel(data):
    '''
        根据alarmlevel划分数据
    '''
    level0, level1, level2, level3 = 0, 0, 0, 0
    for alarm in data:
        if alarm[3] == 0:
            level0+=1
        elif alarm[3] == 1:
            level1+=1
        elif alarm[3] == 2:
            level2+=1
        else:
            level3+=1
    return level0,level1,level2,level3

# 传入数据的位置，使用pd进行读取
if __name__ == '__main__':
    '''
    接收传入参数为一个csv的文件，返回总告警信息和各个级别的告警信息
    '''
    choice = input("Enter 0 to use default file path, or enter your file path: ")

    if choice == "0":
        # Use default file path
        data = read_data("t_alarmlogcur.csv")
    else:
        # Use user-specified file path
        data = read_data(choice)
    level0, level1, level2, level3 = getdataByalarmlevel(data)
    all_account = level0+level1+level2+level3
    # 分别返回5个数据，all_account, level0, level1, level2, level3
    print("总共告警信息有" + str(all_account) + "条")
    print("提示告警信息有" + str(level0) + "条")
    print("次要告警信息有" + str(level1) + "条")
    print("主要告警信息有" + str(level2) + "条")
    print("紧急告警信息有" + str(level3) + "条")
#
# # 数据和标签
# labels_pie = ['Prompt alarm', 'Minor alarm', 'Major alarm', 'Critical alarm']
# sizes_pie = [level0, level1, level2, level3]
#
# # 绘制饼状图
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes_pie, labels=labels_pie, autopct='%1.1f%%', startangle=90)
# ax1.axis('equal')
# ax1.set_title('Alarm Levels (Pie Chart)')
#
#     # 柱状图数据和标签
# labels_bar = ['Prompt alarm', 'Minor alarm', 'Major alarm', 'Critical alarm']
# values_bar = [level0, level1, level2, level3]
#
#     # 绘制柱状图
# fig2, ax2 = plt.subplots()
# ax2.bar(labels_bar, values_bar)
# ax2.set_title('Alarm Levels (Bar Chart)')
# ax2.set_xlabel('Alarm Level')
# ax2.set_ylabel('Number of Alarms')
#
#     # 显示图形
# plt.show()