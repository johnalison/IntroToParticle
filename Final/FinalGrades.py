# Detailed problem by problem break down
# https://docs.google.com/spreadsheets/d/1cG-qH2vXRKDGHq8PzlV82spaq9uhJzEla_rXIVfAO58/edit#gid=0

import matplotlib.pyplot as plt

import numpy as np
import matplotlib

final_raw = [42.,#Grayson 
             34. ,#Katherine
             45. ,#Kevin
             51. ,#Nick
             43. ,#Aileen
             30. ,#Dez 
             45. ,#Trevor
             ]


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
home_work = [92.92,#Grayson 
             63.75,#Katherine
             78.75,#Kevin
             90.42,#Nick
             84.58,#Aileen
             38.96,#Dez 
             92.29,#Trevor
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



final    = np.array(final_raw)
midTerm2 = np.array(midterm2_raw)
midTerm1 = np.array(midterm1_raw)
homework = np.array(home_work)

average = round(np.average(final),1)
rms = round(np.std(final),1)
print(average,"+/-",rms)


bins = np.linspace(0,65,15)
print( bins)



plt.hist(final, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.plot([average,average],[0,3],'r--')
plt.annotate("Mean = "+str(average), xy=(20, 2.5), xytext=(3,2.5),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )

plt.annotate("RMS ="+str(rms), xy=(20, 2.5), xytext=(3,2.2),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )
plt.xlim(0, 65)
plt.xlabel("Grades (out of 65)")
plt.savefig("Grades.pdf")
plt.savefig("Grades.png")
plt.close()

zScores = (final - average)/rms
#print(zScores)
#print(np.average(zScores),np.std(zScores))


binsZ = np.linspace(-3,3,25)

plt.hist(zScores, bins=binsZ,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.xlabel("Grades Curved")

plt.savefig("NormalizedGrades.pdf")
plt.savefig("NormalizedGrades.png")
plt.close()




plt.plot(final,home_work,"ko")
plt.xlim(0, 65)
plt.ylim(0, 100)

plt.xlabel("Final (XX/65)")
plt.ylabel("Homework (%)")
#plt.plot(,"ko")
plt.savefig("CorrelationHW.pdf")
plt.savefig("CorrelationHW.png")
plt.close()


plt.plot(final,midTerm1,"ko")
plt.xlim(0, 65)
plt.ylim(0, 50)

plt.xlabel("Final (XX/65)")
plt.ylabel("MidTerm1 (XX/50)")
#plt.plot(,"ko")
plt.savefig("CorrelationMidTerm1.pdf")
plt.savefig("CorrelationMidTerm1.png")
plt.close()


plt.plot(final,midTerm2,"ko")
plt.xlim(0, 65)
plt.ylim(0, 60)

plt.xlabel("Final (XX/65)")
plt.ylabel("MidTerm2 (XX/60)")
#plt.plot(,"ko")
plt.savefig("CorrelationMidTerm2.pdf")
plt.savefig("CorrelationMidTerm2.png")
plt.close()




#
#binsCombined = np.linspace(0,100,50)
#plt.hist(combined, bins=binsCombined,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
##plt.plot([21,21],[0,3],'r--')
#plt.savefig("Combined.pdf")
#
#for i in range(len(midTerm2)):
#    print( midTerm2[i],round(zScores[i],2), combined[i])
#    # print( zScores)
#    # print( combined)


combinedGrades = []
for i in range(len(midterm2_raw)):
    midTerm1 = midterm1_raw[i]/50*100
    midTerm2 = midterm2_raw[i]/60*100
    final    = final_raw[i]/65*100
    homework  = home_work[i]
    combined = 0.4*homework + 0.2 * midTerm1+ 0.2*midTerm2 + 0.2*final
    print(str(i),"==> ",homework,midTerm1,midTerm2,final,"==",combined)

    combinedGrades.append(combined)
print(midterm2_raw)
print(home_work)
print(combinedGrades)
combinedGrades=np.array(combinedGrades)

bins = np.linspace(0,100,30)
plt.hist(combinedGrades, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.xlabel("Grades %")
plt.savefig("CombinedGrades.pdf")
plt.savefig("CombinedGrades.png")

plt.close()

averageCombined = round(np.average(combinedGrades),1)
rmsCombined = round(np.std(combinedGrades),1)
print(averageCombined,"+/-",rmsCombined)

zScoresCombined = (combinedGrades - averageCombined)/rmsCombined

bins = np.linspace(-3,3,30)
plt.hist(zScoresCombined, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.xlabel("Normalized Scores")
plt.savefig("CombinedGradesNorm.pdf")
plt.savefig("CombinedGradesNorm.png")

plt.close()
