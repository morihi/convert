# -*- coding: utf-8 -*-
import pandas as pd
import sys

'''

各生徒のチャートCSVファイルから,構造図の結果をSP表用にまとめたCSVを出力する。
CSVの形式は、ヘッダー一行、インデックス一行、結線がある場合1,ない場合0とする。

'''

class Conversion :

    #教師データなし
    def conversion(student_name,df_list):

        std_num = len(student_name)

        '''
        読み込んだCSVの値を格納するリスト
        '''

        cvs_list = []
        for a in range(0,std_num):
            cvs_list.append([])


        '''
        作成するCSVのインデックス用リスト
        '''
        list_index = []
        for i in student_name:
            f = []
            f = i.split('.')
            list_index.append(f[0])

        '''
        CSVのデータを変換し、listに格納
        '''
        c = 0
        for i in range(0,std_num):
            for a in range(0,len(df_list[i])):
                c = 0
                for b in df_list[i].values[a]:
                    if a == c :
                        #do nothing
                        pass
                    elif b == 1:
                        cvs_list[i].append(1)
                    else:
                        cvs_list[i].append(0)
                    c += 1

        '''
        ヘッダー用リスト作成
        '''
        list_columns=[]
        for a in range(1,len(df_list[0])+1):
            for b in range(1,len(df_list[0])+1):
                if  a == b:
                    #do nothing
                    pass
                else:
                    list_columns.append(str(a)+"→"+str(b))

        #print(list_name)
        #print(cvs_list)
        '''
        作成したリストをCSVデータフレームに変換
        '''
        df2 = pd.DataFrame(
        cvs_list,
        columns = list_columns,
        index = list_index
        )

        #print(df2)
        #df2.to_csv('SP表.csv',encoding="SHIFT-JIS")
        return df2

    #教師データあり
    def conversion1(student_name,df_list,teacher_data):
        std_num = len(student_name)

        dft = pd.read_csv("teacher_data/"+teacher_data,index_col=0)

        '''
        CSVの形式を確認
        '''


        if ( len(dft) != len(dft.columns)):
            print("教師データの行数と列数が一致しません")
            sys.exit()

        '''
        print(len(df_list[0]))
        print(len(df_list[1]))
        print(len(dft))
        print(len(df_list[0].columns))
        print(len(dft.columns))
        print(df_list[0].values[1])
        '''

        '''
        読み込んだCSVの値を格納するリスト
        '''

        cvs_list = []
        for a in range(0,std_num):
            cvs_list.append([])

        '''
        CSVのデータを変換し、listに格納
        '''

        c = 0
        for i in range(0,std_num):
            for a in range(0,len(df_list[i])):
                c = 0
                for b in df_list[i].values[a]:
                    if a == c :
                        #do nothing
                        pass
                    elif b == dft.values[a][c]:
                        cvs_list[i].append(1)
                    else:
                        cvs_list[i].append(0)
                    c += 1

        '''
        ヘッダー用リスト作成
        '''
        list_columns=[]
        for a in range(1,len(df_list[0])+1):
            for b in range(1,len(df_list[0])+1):
                if  a == b:
                    #do nothing
                    pass
                else:
                    list_columns.append(str(a)+"→"+str(b))
        '''
        作成するCSVのインデックス用リスト
        '''
        list_index = []
        for i in student_name:
            f = []
            f = i.split('.')
            list_index.append(f[0])

        '''
        作成したリストをCSVデータフレームに変換
        '''
        df2 = pd.DataFrame(
        cvs_list,
        columns = list_columns,
        index = list_index
        )

        return df2
