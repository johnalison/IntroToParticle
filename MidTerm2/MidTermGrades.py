# Detailed problem by problem break down
# https://docs.google.com/spreadsheets/d/1cG-qH2vXRKDGHq8PzlV82spaq9uhJzEla_rXIVfAO58/edit#gid=0

import matplotlib.pyplot as plt

import numpy as np
import matplotlib

midterm2_raw = [49.,#Grayson 
                19. ,#Katherine
                42. ,#Kevin
                51. ,#Nick
                31. ,#Aileen
                21. ,#Dez 
                53. ,#Trevor
                ]


midterm1_raw = [40.5,#Grayson 
              15.  ,#Katherine
              35.  ,#Kevin
              44.  ,#Nick
              26.  ,#Aileen
              25.  ,#Dez 
              30.  ,#Trevor
              ]


# in %
home_work = [92.7,#Grayson 
             60.45,#Katherine
             78.64,#Kevin
             90.91,#Nick
             85.45,#Aileen
             35,#Dez 
             93.41,#Trevor
             ]


# 2019
#grades_raw = [#20  # Kiran
#              24 # Josh Freudenhammer
#              ,16.5 # Steven HAll
#              ,19 # Josh Kim 
#              ,16.25 # Brandon N
#              ,21 # Ian Harris
#              ,17.5 # Max Perry
#              ,24.5 # Ruvini
#              ,22.75 # Ian Holst
#              ,28.5 # Naren
#              ,9, #Yue Xu
#              ]
## in %
#home_work = [ #80
#              62.5 #Joshua
#              ,42.4 #Steven
#              ,90.7 #Joshua 
#              ,54.8 #Brandon
#              ,92.7 # Ian Harris
#              ,24,#Max
#              62.5,#Ruvini
#              80, #Ian Holst
#              100, #Naren
#              59,  # Yue
#              ]

combined = []
for i in range(len(midterm2_raw)):
    print(str(i)+"==> "+str(round((midterm2_raw[i]/50*100 + home_work[i])/2,2)))
    combined.append(round((midterm2_raw[i]/50*100 + home_work[i])/2,2))
print(midterm2_raw)
print(home_work)
print(combined)



grades2 = np.array(midterm2_raw)
grades1 = np.array(midterm1_raw)
homework = np.array(home_work)

average = round(np.average(grades2),1)
rms = round(np.std(grades2),1)
print(average)


bins = np.linspace(0,60,15)

plt.hist(grades2, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.plot([average,average],[0,3],'r--')
plt.annotate("Mean = "+str(average), xy=(20, 2.5), xytext=(3,2.5),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )

plt.annotate("RMS ="+str(rms), xy=(20, 2.5), xytext=(3,2.2),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )

plt.xlabel("Grades (out of 60)")
plt.savefig("Grades.pdf")
plt.savefig("Grades.png")
plt.close()

zScores = (grades2 - average)/rms
#print(zScores)
#print(np.average(zScores),np.std(zScores))


binsZ = np.linspace(-3,3,25)

plt.hist(zScores, bins=binsZ,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.xlabel("Grades Curved")

plt.savefig("NormalizedGrades.pdf")
plt.savefig("NormalizedGrades.png")
plt.close()


plt.plot(grades2,home_work,"ko")
plt.xlim(10, 60)

plt.xlabel("MidTerm2 (XX/60)")
plt.ylabel("Homework (%)")
#plt.plot(,"ko")
plt.savefig("CorrelationHW.pdf")
plt.savefig("CorrelationHW.png")
plt.close()


plt.plot(grades2,home_work,"ko")
plt.xlim(0, 60)
plt.ylim(0, 100)

plt.xlabel("MidTerm2 (XX/60)")
plt.ylabel("Homework (%)")
#plt.plot(,"ko")
plt.savefig("CorrelationHW.pdf")
plt.savefig("CorrelationHW.png")
plt.close()


plt.plot(grades2,grades1,"ko")
plt.xlim(0, 60)
plt.ylim(0, 50)

plt.xlabel("MidTerm2 (XX/60)")
plt.ylabel("MidTerm1 (XX/50)")
#plt.plot(,"ko")
plt.savefig("CorrelationMidTerm1.pdf")
plt.savefig("CorrelationMidTerm1.png")
plt.close()


#
#binsCombined = np.linspace(0,100,50)
#plt.hist(combined, bins=binsCombined,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
##plt.plot([21,21],[0,3],'r--')
#plt.savefig("Combined.pdf")
#
#for i in range(len(grades2)):
#    print( grades2[i],round(zScores[i],2), combined[i])
#    # print( zScores)
#    # print( combined)
