# -*- coding: utf-8 -*-
import conversion as cv
import readCSV as rd
import at_index as at
import error as er
import sys
import judge as jd
import make

'''

$ python main.py (-t or -m) (file name or percent)

$ pip show pandas
Version : 0.23.1

root/
│
├ main.py
├ conversion.py     //生徒データを集約したDataFrameへ変換し、返す
├ at_index.py      //生徒データが集約されたcsvから注意係数を算出し、SP表.csv出力
├ readCSV.py        //生徒,教師CSVデータをディレクトリから検索し、戻り値で渡す
├ make.py       //生徒のデータから教師データを作成する
├ error.py      //エラーメッセージを返す
├ judge.py      //生徒データの正誤判断、DataFrameで返す
└ csv/      //生徒データは全てここにおく
   ├ 生徒A.csv
   ├ 生徒B.csv
   ├ ...
   ├ 生徒X.csv
   ├ SP/        //SP表がここに出力される
   └ teacher_data/       //教師データがある場合はここにおく
      └teacher.csv

'''


args = sys.argv     #コマンドライン引数をlistでもつ
student_name = []
if len(args) == 1:
    #コマンドライン引数が渡されない場合
    student_name = rd.readCSV()
    if student_name == 0 :
        print("生徒のCSVデータが存在しません")
    elif student_name == 1 :
        print("生徒データが一件しかありません")
    else :
        df_list = jd.judge(student_name)
        print("教師データなしで実行します..")
        df = cv.Conversion.conversion(student_name,df_list)
        at.at_index(df)
elif len(args) == 2:
    #コマンドライン引数が渡された場合
    if (args[1] == "--teacher" or args[1] == "-t") :
        teacher_data = rd.readTeacher()
        if teacher_data == 0 :
            print("teacher.csvが存在しません")
        elif teacher_data == 1 :
            student_name = rd.readCSV()
            if student_name == 0 :
                print("生徒のCSVデータが存在しません")
            elif student_name == 1 :
                print("生徒データが一件しかありません")
            else :
                df_list = jd.judge(student_name)
                print("正解データありで実行します..")
                df = cv.Conversion.conversion1(student_name,df_list,"teacher.csv")
                at.at_index(df)
    elif (args[1] == "--make" or args[1] == "-m") :
        student_name = rd.readCSV()
        if student_name == 0 :
            print("生徒のCSVデータが存在しません")
        elif student_name == 1 :
            print("生徒データが一件しかありません")
        else :
            df_list = jd.judge(student_name)
            make.make(student_name,df_list,80)
            df = cv.Conversion.conversion1(student_name,df_list,"teacher.csv")
            print("正解データを正答率80%で作成して実行します..")
            at.at_index(df)
    else :
        print(er.error(1))
elif len(args) == 3 :
    #コマンドライン引数と教師データの指定があった場合
    if(args[1] == "--teacher" or args[1] == "-t"):
        teacher_data = rd.spec_teacher(args[2])
        if teacher_data == 0:
            print(args[2]+"が存在しません")
        else :
            student_name = rd.readCSV()
            if student_name == 0 :
                print("生徒のCSVデータが存在しません")
            elif student_name == 1 :
                print("生徒データが一件しかありません")
            else :
                df_list = jd.judge(student_name)
                print("正解データを"+args[2]+"で実行します..")
                df = cv.Conversion.conversion1(student_name,df_list,teacher_data)
                at.at_index(df)
    elif (args[1] == "--make" or args[1] == "-m") :
        student_name = rd.readCSV()
        if student_name == 0 :
            print("生徒のCSVデータが存在しません")
        elif student_name == 1 :
            print("生徒データが一件しかありません")
        else :
            df_list = jd.judge(student_name)
            make.make(student_name,df_list,int(args[2]))
            df = cv.Conversion.conversion1(student_name,df_list,"teacher.csv")
            print("正解データを正答率"+str(args[2])+"%で作成して実行します..")
            at.at_index(df)
    else :
        print(er.error(1))
else :
    print(er.error(2))
