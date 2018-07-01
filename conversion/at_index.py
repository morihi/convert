#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

'''

引数のDataFrameから注意係数を算出する

'''

def at_index(csv):

    '''
    conversion.pyで出力したSP表を読み込む
    SP表.csvはshift-jis
    '''
    #csv = pd.read_csv("SP表.csv",encoding="SHIFT-JIS",index_col=0)
    drop_list = []       #全て0の列を格納する
    #print(csv[[0]])
    k = 0

    '''
    SP表の中で列の値が全て0の物を格納
    列の数字を足してkに代入。k=0なら全て0の列
    '''
    for i in range(csv.shape[1]):
        k = 0
        for j in range(csv.shape[0]):
            k += csv[csv.columns.values[i]][j]
        if k == 0:
            #delete this columns
            #print(csv[csv.columns.values[i]])
            drop_list.append(csv.columns.values[i])
        else :
            #do nothing
            pass
    '''
    格納された列を削除
    '''
    for i in drop_list :
        csv.drop([i],axis=1,inplace=True)    #inplace=Trueで現在読み込んでいるDataFrameに反映させる
    #print(csv)

    '''
    ソート処理
    ①生徒の順番
    '''
    sum_list = []
    k = 0
    for i in range(csv.shape[0]):
        k = 0
        for j in range(csv.shape[1]):
                k += csv[csv.columns.values[j]][i]
        sum_list.append(k)
    csv['sum'] = np.array(sum_list)
    csv.sort_values(by="sum",ascending=False,inplace=True)
    #print(csv)
    csv.drop("sum",axis=1,inplace=True)

    '''
    ソート処理
    ②問題の順番
    '''

    question_list=[]
    k = 1
    for i in range(csv.shape[1]):
        k = 0
        for j in range(csv.shape[0]):
            k += csv[csv.columns.values[i]][j]
        question_list.append(k)
    csv.loc["q_sum"] = question_list
    csv.sort_values(by="q_sum",axis=1,ascending=False,inplace=True)
    csv.drop("q_sum",axis=0,inplace=True)
    #print(csv)

    '''
    注意係数算出
    '''

    #μ'を算出
    q_sum = sum(question_list)
    myu = q_sum / csv.shape[1]
    '''
    print(csv.shape[0])
    print(csv.shape[1])
    print(myu)
    '''
    zero_sum = 0
    one_sum = 0
    total = 0
    tyuikeisu = []
    #print(csv[csv.columns.values[0]][1])
    for i in range(csv.shape[0]):
        zero_sum = 0
        one_sum = 0
        total = 0
        '''
        生徒iのS曲線から左の0に対応する結線数の和
        '''
        for j in range(sum_list[i]):
            if csv[csv.columns.values[j]][i] == 0:
                zero_sum += question_list[j]
        #print(csv.index[i] + ":" + str(zero_sum))
        '''
        生徒iのS曲線から左の0に対応する結線数の和
        '''
        b = csv.shape[1] - sum_list[i]
        for k in range(b):
            if csv[csv.columns.values[sum_list[i]+k]][i] == 1:
                one_sum += question_list[sum_list[i]+k]
        #print(csv.index[i] + ":" + str(one_sum))
        '''
        生徒iのS曲線から左の問題の結線数の和
        '''
        for l in range(sum_list[i]):
            total += question_list[l]
        #print(csv.index[i] + ":" + str(total))
        '''
        注意係数算出＋DataFrameに書き込み
        '''
        tyuikeisu.append(( zero_sum - one_sum ) / ( total - ( sum_list[i] * myu ) ))
    #print(np.round(np.array(tyuikeisu),2))
    csv["注意係数"] = np.round(np.array(tyuikeisu),2)
    #print(csv)
    csv.to_csv('./csv/SP/SP表.csv',encoding="SHIFT-JIS")
    print("######################"+"\n"+" conversion complete!"+"\n"+"######################")
