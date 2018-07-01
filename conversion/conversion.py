#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

"""

各生徒のチャートCSVファイルから,構造図の結果をSP表用にまとめたCSVを出力する。
CSVの形式は、ヘッダー一行、インデックス一行、結線がある場合1,ない場合0とする。

"""

class Conversion :

    def conversion(student_name,df_list):

        """
        生徒のデータを集め、SP表にするための一つのDataFrameに変換する

        Parameters
        ----------
        student_name : list of str
            生徒名を格納したリスト
        df_list : list of DataFrame
            生徒の結線データを格納したリスト

        Returns
        -------
        df2 : DaraFrame
            生徒データを集約してSP表用にまとめたDataFrame
        """

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

        '''
        作成したリストをCSVデータフレームに変換
        '''
        df2 = pd.DataFrame(
        cvs_list,
        columns = list_columns,
        index = list_index
        )

        return df2


    def cnv_tec(student_name,df_list,dft):

        """
        生徒のデータを集め、教師データと比較して一つのDataFrameに変換する

        student_name : list of str
            生徒名を格納したリスト
        df_list : list of DataFrame
            生徒の結線データを格納したリスト
        dft : DaraFrame
            教師データのDataFrame

        Returns
        -------
        df2 : DaraFrame
            教師データと比較した生徒データを集約してSP表用にまとめたDataFrame
        """

        std_num = len(student_name)


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
