#!/usr/bin/env python
# -*- coding: utf-8 -*-

import conversion
import sys
import os

"""

$ python main.py (-t(教師データあり) or -m(教師データ作成)) (file name or percent)

$ pip show pandas
Version : 0.23.1

conversion/
│
├ README
├ main.py       //ここにスクリプトを置いて実行（パスを取得して絶対パスで投げる）
├ conversion/
│  ├ __init__.py        //import
│  ├ conversion.py     //生徒データを集約したDataFrameへ変換し、返す
│  ├ at_index.py      //生徒データが集約されたcsvから注意係数を算出し、SP表.csv出力
│  ├ readCSV.py        //生徒,教師CSVデータをディレクトリから検索し、渡す
│  ├ make.py       //生徒のデータから教師データを作成する
│  ├ error.py      //エラーメッセージを返す
│  ├ judge.py      //生徒データの正誤判断、DataFrameで返す
│  └ changerJSON/
│       ├changer.py     //firebaeのJSONをCSVに変換
│       └hoge.json      //変換するJSON
└ csv/      //生徒データは全てここにおく
   ├ 生徒A.csv
   ├ 生徒B.csv
   ├ ...
   ├ 生徒X.csv
   ├ SP/        //SP表がここに出力される
   └ teacher_data/       //教師データがある場合はここにおく
      └teacher.csv

"""


args = sys.argv     #コマンドライン引数をlistでもつ
#絶対パスでcsvディレクトリを指定する
name = os.path.dirname(os.path.abspath(__name__))
joined_path = os.path.join(name,'./csv')
path = os.path.normpath(joined_path)

student_name = []



if len(args) == 1:
    #コマンドライン引数が渡されない場合

    student_name = conversion.rd.get_std_name(path)
    if student_name == 0 :
        print("生徒のCSVデータが存在しません")
    elif student_name == 1 :
        print("生徒データが一件しかありません")
    else :
        df_list = conversion.rd.get_std_df(path,student_name)
        if conversion.jd.judge(df_list) :
            print("教師データなしで実行します..")
            df = conversion.cv.Conversion.conversion(student_name,df_list)
            conversion.at.at_index(path,df)

elif len(args) == 2:
    #コマンドライン引数が渡された場合

    if (args[1] == "--teacher" or args[1] == "-t") :
        teacher_data = conversion.rd.readTeacher(path)
        if teacher_data == 0 :
            print("teacher.csvが存在しません")
        elif teacher_data == 1 :
            student_name = conversion.rd.get_std_name(path)
            if student_name == 0 :
                print("生徒のCSVデータが存在しません")
            elif student_name == 1 :
                print("生徒データが一件しかありません")
            else :
                df_list = conversion.rd.get_std_df(path,student_name)
                if conversion.jd.judge(df_list) :
                    dft = conversion.rd.get_tec_df(path,"teacher.csv")
                    if conversion.jd.judge_tec(dft,df_list):
                        print("正解データありで実行します..")
                        df = conversion.cv.Conversion.cnv_tec(student_name,df_list,dft)
                        conversion.at.at_index(path,df)

    elif (args[1] == "--make" or args[1] == "-m") :
        student_name = conversion.rd.get_std_name(path)
        if student_name == 0 :
            print("生徒のCSVデータが存在しません")
        elif student_name == 1 :
            print("生徒データが一件しかありません")
        else :
            df_list = conversion.rd.get_std_df(path,student_name)
            if conversion.jd.judge(df_list) :
                dft = conversion.make.make(path,student_name,df_list,80)
                df = conversion.cv.Conversion.cnv_tec(student_name,df_list,dft)
                print("正解データを正答率80%で作成して実行します..")
                conversion.at.at_index(path,df)
    else :
        print(conversion.er.error(1))

elif len(args) == 3 :
    #コマンドライン引数と教師データの指定があった場合

    if(args[1] == "--teacher" or args[1] == "-t"):
        teacher_data = conversion.rd.spec_teacher(path,args[2])
        if teacher_data == 0:
            print(args[2]+"が存在しません")

        else :
            student_name = conversion.rd.get_std_name(path)

            if student_name == 0 :
                print("生徒のCSVデータが存在しません")
            elif student_name == 1 :
                print("生徒データが一件しかありません")
            else :
                df_list = conversion.rd.get_std_df(path,student_name)
                if conversion.jd.judge(df_list) :
                    print("正解データを"+args[2]+"で実行します..")
                    dft = conversion.rd.get_tec_df(path,teacher_data)
                    if conversion.jd.judge_tec(dft,df_list):
                        df = conversion.cv.Conversion.cnv_tec(student_name,df_list,dft)
                        conversion.at.at_index(path,df)

    elif (args[1] == "--make" or args[1] == "-m") :
        student_name = conversion.rd.get_std_name(path)
        if student_name == 0 :
            print("生徒のCSVデータが存在しません")
        elif student_name == 1 :
            print("生徒データが一件しかありません")
        else :
            df_list = conversion.rd.get_std_df(path,student_name)
            if conversion.jd.judge(df_list):
                dft = conversion.make.make(path,student_name,df_list,int(args[2]))
                df = conversion.cv.Conversion.cnv_tec(student_name,df_list,dft)
                print("正解データを正答率"+str(args[2])+"%で作成して実行します..")
                conversion.at.at_index(path,df)
    else :
        print(conversion.er.error(1))
else :
    print(conversion.er.error(2))
