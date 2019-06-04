import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from matplotlib import pyplot as plt;

def writeToExcel(itr):
 rows1=np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',''])
 cols1=np.array(['TEAMS','A-HOME','B-HOME','C-HOME','D-HOME','E-HOME','F-HOME','G-HOME','H-HOME','I-HOME','J-HOME','K-HOME','L-HOME','M-HOME','N-HOME',
      'O-HOME','P-HOME','Q-HOME','R-HOME','S-HOME','T-HOME','A-AWAY','B-AWAY','C-AWAY','D-AWAY','E-AWAY','F-AWAY','G-AWAY','H-AWAY','I-AWAY','J-AWAY','K-AWAY','L-AWAY','M-AWAY','N-AWAY',
      'O-AWAY','P-AWAY','Q-AWAY','R-AWAY','S-AWAY','T-AWAY'])

 df1=pd.DataFrame()
 dict = {'TEAMS': rows1}
 for n in range(itr):
  print("Writing to FILE..!! ITERATION ::"+str(n+1))
  for j in range(1,len(cols1)):
   val=[];

   for i in range(0,20):
       if(rows1[i]==cols1[j][0:1]):
          val=val+['']

       else:
          val=val+[np.random.randint(0,high=38*3)]

   dict[str(cols1[j])]=val+['ITR ::'+str(n+1)+' END']
  df2 = pd.DataFrame(dict,columns=cols1)
  df1=pd.concat([df1,df2])
 writer = ExcelWriter('E:\\Sanya-EPL.xlsx')
 df1.to_excel(writer,'RAW DATA',index=False)
 writer.save()
 print("Data FILE SAVED")
 print("Wait.!! Calculating output")

def readExcel(itr):
    charsli=[]
    sumsli=[]
    avgli=[]
    file=pd.read_excel('E:\\Sanya-EPL.xlsx','RAW DATA')
    for i in range(0,20):
     sums=0
     rows = file[i:file.last_valid_index():21].sum()
     for j in range(1,len(rows)):
      sums=sums+int(rows[j])
     charsli.append(chr(i+65))
     sumsli.append(sums)
     avgli.append(np.round(sums/itr,decimals=2))
     print(chr(i+65)+' :: '+str(sums)+' :: '+str(np.round(sums/itr,decimals=2)))
    df1=pd.DataFrame({'TEAMS':charsli,'SUM':sumsli,'AVG.':avgli},columns=['TEAMS','SUM','AVG.'])
    writer = ExcelWriter('E:\\Sanya-EPL - OUTPUT.xlsx')
    df1.to_excel(writer, 'OP DATA', index=False)
    writer.save()
    plt.title("Output Graph - Avg. Score v/s Teams")
    print("OUTPUT FILE SAVED")
    plt.xlabel("Teams")

    plt. ylabel("Average Score")
    plt.plot(charsli,avgli)
    plt.show()
itr=int(input("Enter iterations :: "))
writeToExcel(itr)
readExcel(itr);

