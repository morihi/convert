#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import json
import sys

"""

firebaseのJSONからCSVデータへの変換

"""

list_size = 8

li=[]
for i in range(list_size):
    li.append([])

for j in range(list_size):
    for i in range(list_size):
        li[j].append(0)

'''
ヘッダー用リスト作成
'''
list_columns=[]
for i in range(8):
    list_columns.append("C"+str(i))

'''
作成するCSVのインデックス用リスト
'''
list_index = []
for i in range(list_size):
    list_index.append("L"+str(i))
list=[]

def std_changer(name_list,json_name,class_name):
    global list
    f = open(json_name,'r')
    json_data = json.load(f)

    #print("{}".format(json.dumps(json_data,indent=4)))

    if type(name_list) is 'list':
        for name in name_list :
            list.append(json_data[class_name][name]["cell_link_source"])
            list.append(json_data[class_name][name]["cell_link_target"])
            print(list[0])
            print(list[1])
            for j in range(len(list[0])):
                li[int(list[0][int(j)])][int(list[1][int(j)])] = 1
            df = pd.DataFrame(
            li,
            columns = list_columns,
            index = list_index
            )
            df.to_csv('../../csv/'+name+".csv",encoding="shift-jis")
            for k in range(list_size):
                for l in range(list_size):
                    li[k][l]=0
            list = []

    elif type(name_list) is 'str':
        list.append(json_data[class_name][name]["cell_link_source"])
        list.append(json_data[class_name][name]["cell_link_target"])
        print(list[0])
        print(list[1])
        for j in range(len(list[0])):
            li[int(list[0][int(j)])][int(list[1][int(j)])] = 1
        df = pd.DataFrame(
        li,
        columns = list_columns,
        index = list_index
        )
        df.to_csv('../../csv/'+name+".csv",encoding="shift-jis")
        for k in range(list_size):
            for l in range(list_size):
                li[k][l]=0
        list = []

def tec_changer(json_name,class_name):
    global list
    f = open(json_name,'r')
    json_data = json.load(f)
    list.append(json_data[class_name]["先生"]["cell_link_source"])
    list.append(json_data[class_name]["先生"]["cell_link_target"])
    print(list[0])
    print(list[1])
    for j in range(len(list[0])):
        li[int(list[0][int(j)])][int(list[1][int(j)])] = 1
    df = pd.DataFrame(
    li,
    columns = list_columns,
    index = list_index
    )
    df.to_csv('../../csv/teacher_data/teacher.csv',encoding="shift-jis")


#コマンドラインから呼びたい
if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        std_changer(args[1],args[2],args[3])
    elif len(args) == 3:
        tec_changer(args[1],args[2])
