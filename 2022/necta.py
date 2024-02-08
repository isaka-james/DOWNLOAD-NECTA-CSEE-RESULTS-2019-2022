import requests as req
import pandas as pd
import os

class scrap:
    def _init_(self,w,x,y,z):
        self.w,self.x,self.y,self.z=w,x,y,z
    def  returnAllYears(w,x,y,z):
        data1=req.get(w)
        data2=req.get(x)
        data3=req.get(y)
        data4=req.get(z)
        return data1,data2,data3,data4

    def convToText(data1,data2,data3,data4):
        t1=data1.text
        t2=data2.text
        t3=data3.text
        t4=data4.text
        return t1,t2,t3,t4
        
    def convToPd(t1,t2,t3,t4):
        pd1=pd.read_html(t1)
        pd2=pd.read_html(t2)
        pd3=pd.read_html(t3)
        pd4=pd.read_html(t4)
        return pd1[2],pd2[2],pd3[2],pd4[2]
        
    def getList(pd1,pd2,pd3,pd4):
        theListOne=[]
        theListTwo=[]
        theListThree=[]
        theListFour=[]
        #Get list for 2019
        for rowIndex, row in pd1.iterrows(): #iterate over rows
            for columnIndex, value in row.items():
                theListOne.append(value)
        
        #Get list for 2020
        for rowIndex, row in pd2.iterrows(): #iterate over rows
            for columnIndex, value in row.items():
                theListTwo.append(value)

        #Get list for 2021
        for rowIndex, row in pd3.iterrows(): #iterate over rows
            for columnIndex, value in row.items():
                theListThree.append(value)
        
        #Get list for 2022
        for rowIndex, row in pd4.iterrows(): #iterate over rows
            for columnIndex, value in row.items():
                theListFour.append(value)

        return theListOne,theListTwo,theListThree,theListFour
        
def main():
   url_1="https://maktaba.tetea.org/exam-results/CSEE2019/csee.htm"
   url_2="https://onlinesys.necta.go.tz/results/2020/csee/csee.htm"
   url_3="https://onlinesys.necta.go.tz/results/2021/csee/csee.htm"
   url_4="https://onlinesys.necta.go.tz/results/2022/csee/index.htm"
   
   data1,data2,data3,data4=scrap.returnAllYears(url_1,url_2,url_3,url_4)
   t1,t2,t3,t4=scrap.convToText(data1,data2,data3,data4)
   pd1,pd2,pd3,pd4=scrap.convToPd(t1,t2,t3,t4)
   list_One,list_Two,list_Three,list_Four=scrap.getList(pd1,pd2,pd3,pd4)
   
   #Get the lists of Htmls
   print("Starting for 2022...")
   for i in list_Four:
       url=f"https://onlinesys.necta.go.tz/results/2022/csee/results/{i[:5].lower()}.htm"
       datas=req.get(url)
       texts=datas.text
       f = open(f"{i[:5]}.htm", "w")
       f.write(texts)
       f.close()
       print(f"Downloaded {i}")


   os.system("clear")
   print("DONE")
   
   
main()