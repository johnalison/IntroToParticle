# Detailed problem by problem break down
# https://docs.google.com/spreadsheets/d/1cG-qH2vXRKDGHq8PzlV82spaq9uhJzEla_rXIVfAO58/edit#gid=0

import matplotlib.pyplot as plt

import numpy as np
import matplotlib

names = [      " Josh Freud."
              ," Steven Hall"
              ," Josh Kim "
              ," Brandon N"
              ," Ian Harris"
              ," Max Perry"
              ," Ruvini"
              ," Ian Holst"
              ," Naren"
              ," Yue Xu"
              ]


final_raw = [#64  # Kiran
              55 # Josh Freudenhammer
              ,50 # Steven HAll
              ,62 # Josh Kim 
              ,56 # Brandon N
              ,81 # Ian Harris
              ,45 # Max Perry
              ,68 # Ruvini
              ,78 # Ian Holst
              ,96 # Naren
              ,68 #Yue Xu
              ]


midterm_raw = [#20  # Kiran
              24 # Josh Freudenhammer
              ,16.5 # Steven HAll
              ,19 # Josh Kim 
              ,16.25 # Brandon N
              ,21 # Ian Harris
              ,17.5 # Max Perry
              ,24.5 # Ruvini
              ,22.75 # Ian Holst
              ,28.5 # Naren
              ,9, #Yue Xu
              ]

home_work_raw = [ #80
              68.7, #Joshua
              55.4, #Steven
              92.4,#Joshua 
              73.0,#Brandon
              92.6,# Ian Harris
              42.4,#Max
              79.1,#Ruvini
              95.6, #Ian Holst
              98.0, #Naren
              75.7,  # Yue
              ]

home_work_den = [ #80
              21, #Joshua
              30, #Steven
              15,#Joshua 
              30,#Brandon
              15,# Ian Harris
              31,#Max
              30,# 79.1,#Ruvini
              15, #Ian Holst
              35, #Naren
              30,  # Yue
              ]


home_work_num = [ #80
              9, #Joshua
              0, #Steven
              12,#Joshua 
              0,#Brandon
              13,# Ian Harris
              0,#Max
              0 ,# ,#Ruvini
              13, #Ian Holst
              32, #Naren
              0,  # Yue
              ]


home_work= []
hwTotal = 270
for i in range(len(final_raw)):
    hwPoints = home_work_raw[i]/100*hwTotal
    hwPointsCor = hwPoints - home_work_num[i]
    hwTotalCor = hwTotal - home_work_den[i]
    home_work_new = hwPointsCor / hwTotalCor*100
    print(home_work_raw[i],  "--->", home_work_new)
    home_work.append(home_work_new)



combined = []
for i in range(len(final_raw)):
    combined.append(round(  (0.4*final_raw[i]/115*100 + 0.2*midterm_raw[i]/53*100 + 0.4*home_work[i]),2))




average = np.average(combined)
rms = np.std(combined)
zScores = (combined - average)/rms


for i, name in enumerate(names):
    print(name,"...",round(zScores[i],2),"\t",combined[i])

final = np.array(final_raw)
midterm = np.array(midterm_raw)
homework = np.array(home_work)
#average = sum(grades)/len(grades_raw)
#average = round(np.average(final),1)



finalAve = np.average(final)
finalRMS = np.std(final)
zScoresFinal = (final - finalAve)/finalRMS


bins = np.linspace(0,100,20)

plt.hist(final, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.plot([finalAve,finalAve],[0,3],'r--')
plt.annotate("Mean = "+str(round(finalAve,1)), xy=(20, 2.5), xytext=(0,2.5),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )

plt.annotate("RMS ="+str(round(finalRMS,1)), xy=(20, 2.5), xytext=(0,2.2),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )

plt.xlabel("Final (out of 115)")
plt.savefig("FinalScores.pdf")
plt.savefig("FinalScores.png")
plt.close()


binsZ = np.linspace(-3,3,25)

plt.hist(zScoresFinal, bins=binsZ,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.xlabel("Normalized")
plt.savefig("FinalScoresNorm.pdf")
plt.savefig("FinalScoresNorm.png")
plt.close()






plt.hist(zScores, bins=binsZ,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')

plt.xlabel("Combined Normed")

plt.savefig("NormalizedGrades.pdf")
plt.savefig("NormalizedGrades.png")
plt.close()


plt.plot(home_work,final,"ko")
plt.ylabel("Final")
plt.xlabel("Homework")
#plt.plot(,"ko")
plt.savefig("CorrelationHW.pdf")
plt.savefig("CorrelationHW.png")
plt.close()


plt.plot(midterm,final,"ko")
plt.ylabel("Final")
plt.xlabel("MidTerm")
#plt.plot(,"ko")
plt.savefig("CorrelationMidTerm.pdf")
plt.savefig("CorrelationMidTerm.png")
plt.close()


binsCombined = np.linspace(20,90,20)
plt.hist(combined, bins=binsCombined,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
#plt.plot([21,21],[0,3],'r--')

plt.plot([average,average],[0,3],'r--')
plt.annotate("Mean = "+str(round(average,1)), xy=(20, 2.5), xytext=(20,2.5),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )

plt.annotate("RMS ="+str(round(rms,1)), xy=(20, 2.5), xytext=(20,2.2),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )

plt.savefig("Combined.pdf")
plt.close()




plt.plot(final,combined,"ko")
plt.xlabel("Final")
plt.ylabel("Combined")
#plt.plot(,"ko")
plt.savefig("CombinedVsFinal.pdf")
plt.savefig("CombinedVsFinal.png")
plt.close()

plt.plot(home_work,combined,"ko")
plt.xlabel("Homework")
plt.ylabel("Combined")
#plt.plot(,"ko")
plt.savefig("CombinedVsHW.pdf")
plt.savefig("CombinedVsHW.png")
plt.close()

plt.plot(midterm,combined,"ko")
plt.xlabel("MidTerm")
plt.ylabel("Combined")
#plt.plot(,"ko")
plt.savefig("CombinedVsMidTerm.pdf")
plt.savefig("CombinedVsMidTerm.png")
plt.close()

