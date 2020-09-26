# -*- coding: utf-8 -*-



box=float(0)
styrofoam=float(0)
washing_machine=float(0)
bucket=float(0)
toilet=float(0)
bowl=float(0)
bottle=float(0)
water_tower=float(0)
tire=float(0)
plate=float(0)
plastic_bag=float(0)
tub=float(0)
aquarium=float(0)

index=-1

import shutil
import os
path = "D:/University's_homework/影像辨識報告/train_cdc/train_annotations" #資料夾目錄
path2 = "D:/University's_homework/影像辨識報告/train_cdc/train_images" #資料夾目錄
files= os.listdir(path) #得到資料夾下的所有檔名稱
files2= os.listdir(path2) #得到資料夾下的所有檔名稱
s = []
for file in files: #遍歷資料夾
    if not os.path.isdir(file): #判斷是否是資料夾,不是資料夾才打開
        f = open(path+"/"+file); #開啟檔案
        iter_f = iter(f); #建立迭代器
        str = ""
        index+=1
        for line in iter_f: #遍歷檔案,一行行遍歷,讀取文字


            if(line=="		<name>box</name>\n"):
                box+=1
            if(line=="		<name>styrofoam</name>\n"):
                styrofoam+=1
                shutil.copy(path+"/"+file, 'D:/test/testann')
                shutil.copy(path2+"/"+files2[index], 'D:/test/testimg')
            if(line=="		<name>washing_machine</name>\n"):
                washing_machine+=1
            if(line=="		<name>bucket</name>\n"):
                bucket+=1
            if(line=="		<name>toilet</name>\n"):
                toilet+=1
                shutil.copy(path+"/"+file, 'D:/test/testann')
                shutil.copy(path2+"/"+files2[index], 'D:/test/testimg')
            if(line=="		<name>bowl</name>\n"):
                bowl+=1
            if(line=="		<name>water_tower</name>\n"):
                water_tower+=1
            if(line=="		<name>tire</name>\n"):
                tire+=1                
            if(line=="		<name>plate</name>\n"):
                plate+=1
            if(line=="		<name>plastic_bag</name>\n"):
                plastic_bag+=1
            if(line=="		<name>tub</name>\n"):
                tub+=1
                shutil.copy(path+"/"+file, 'D:/test/testann')
                shutil.copy(path2+"/"+files2[index], 'D:/test/testimg')
            if(line=="		<name>aquarium</name>\n"):
                aquarium+=1          
                shutil.copy(path+"/"+file, 'D:/test/testann')
                shutil.copy(path2+"/"+files2[index], 'D:/test/testimg')
            if(line=="		<name>bottle</name>\n"):
                bottle+=1                  
       
print("box= %.0f\n"%(box)) 
print("styrofoam= %.0f\n"%(styrofoam))
print("washing_machine= %.0f\n"%(washing_machine))
print("bucket= %.0f\n"%(bucket))
print("toilet= %.0f\n"%(toilet))
print("bowl= %.0f\n"%(bowl)) 
print("bottle= %.0f\n"%(bottle))
print("water_tower= %.0f\n"%(water_tower))
print("tire= %.0f\n"%(tire))
print("plate= %.0f\n"%(plate))
print("plastic_bag= %.0f\n"%(plastic_bag)) 
print("tub= %.0f\n"%(tub))
print("aquarium= %.0f\n"%(aquarium))
print(index)
print(files2[index])



          
