f:
	cd Final/ && pdflatex Final.tex && cd ..

h12:
	cd Week14_Neutrinos//  && pdflatex homework12.tex  && cd ..

m2s:
	cd MidTerm2/  && pdflatex Midterm2_solutions.tex  && cd ..

m2:
	cd MidTerm2/  && pdflatex Midterm2.tex  && cd ..

36:
	cd Week14_Neutrinos/  && pdflatex lecture36.tex  && cd ..

35:
	cd Week14_Neutrinos/  && pdflatex lecture35.tex  && cd ..

34:
	cd Week14_Neutrinos/  && pdflatex lecture34.tex  && cd ..

33:
	cd Week14_Neutrinos/  && pdflatex lecture33.tex  && cd ..

32:
	cd Week14_Neutrinos/  && pdflatex lecture32.tex  && cd ..

31:
	cd Week12_WeakInteraction/  && pdflatex lecture31.tex  && cd ..

30:
	cd Week12_WeakInteraction/  && pdflatex lecture30.tex  && cd ..

29:
	cd Week12_WeakInteraction//  && pdflatex lecture29.tex  && cd ..

28:
	cd Week12_WeakInteraction//  && pdflatex lecture28.tex  && cd ..

27:
	cd Week12_WeakInteraction//  && pdflatex lecture27.tex  && cd ..

26:
	cd Week12_WeakInteraction/  && pdflatex lecture26.tex  && cd ..

h11:
	cd Week12_WeakInteraction//  && pdflatex homework11.tex  && cd ..

h10s:
	cd Week12_WeakInteraction//  && pdflatex homework10_solutions.tex  && cd ..

h10:
	cd Week12_WeakInteraction//  && pdflatex homework10.tex  && cd ..

h9s:
	cd Week8and9_ColliderPhysics/  && pdflatex homework9_solutions.tex  && cd ..

h9:
	cd Week8and9_ColliderPhysics/  && pdflatex homework9.tex  && cd ..

h8s:
	cd Week8and9_ColliderPhysics/  && pdflatex homework8_solutions.tex  && cd ..

h8:
	cd Week8and9_ColliderPhysics/  && pdflatex homework8.tex  && cd ..

21:
	cd Week8and9_ColliderPhysics/  && pdflatex lecture21.tex  && cd ..

22:
	cd Week8and9_ColliderPhysics/  && pdflatex lecture22.tex  && cd ..

23:
	cd Week8and9_ColliderPhysics/  && pdflatex lecture23.tex  && cd ..

24:
	cd Week8and9_ColliderPhysics/  && pdflatex lecture24.tex  && cd ..

25:
	cd Week8and9_ColliderPhysics/  && pdflatex lecture25.tex  && cd ..

14:
	cd Week6_FeynmanDiagrmas/ && pdflatex lecture14.tex && cd ..

15:
	cd Week6_FeynmanDiagrmas/ && pdflatex lecture15.tex && cd ..

16:
	cd Week6_FeynmanDiagrmas/ && pdflatex lecture16.tex && cd ..

h6:
	cd Week6_FeynmanDiagrmas/ && pdflatex homework6.tex && cd ..

h6s:
	cd Week6_FeynmanDiagrmas/ && pdflatex homework6_solutions.tex && cd ..

17:
	cd Week7_SoftGluons/ && pdflatex lecture17.tex && cd ..

18:
	cd Week7_SoftGluons/ && pdflatex lecture18.tex && cd ..

19:
	cd Week7_SoftGluons/ && pdflatex lecture19.tex && cd ..

20:
	cd Week7_SoftGluons/ && pdflatex lecture20.tex && cd ..

h4:
	cd Week4_Particles/ && pdflatex homework4.tex && cd ..

h4s:
	cd Week4_Particles/ && pdflatex homework4_solutions.tex && cd ..

h5:
	cd Week5_Lagrangians/ && pdflatex homework5.tex && cd ..

h5s:
	cd Week5_Lagrangians/ && pdflatex homework5_solutions.tex && cd ..

11:
	cd Week5_Lagrangians/ && pdflatex lecture11.tex && cd ..

12:
	cd Week5_Lagrangians/ && pdflatex lecture12.tex && cd ..

13:
	cd Week5_Lagrangians/ && pdflatex lecture13.tex && cd ..

8:
	cd Week4_Particles/ && pdflatex lecture8.tex && cd ..

9:
	cd Week4_Particles/ && pdflatex lecture9.tex && cd ..

10:
	cd Week4_Particles/ && pdflatex lecture10.tex && cd ..

h3s:
	cd Week3_Quantum/ && pdflatex homework3_solutions.tex && cd ..

h3:
	cd Week3_Quantum/ && pdflatex homework3.tex && cd ..

6:
	cd Week3_Quantum/ && pdflatex lecture6.tex && cd ..

7:
	cd Week3_Quantum/ && pdflatex lecture7.tex && cd ..

h2s:
	cd Week2_SpaceTime/ && pdflatex homework2_solutions.tex && cd ..

h2:
	cd Week2_SpaceTime/ && pdflatex homework2.tex && cd ..

3:
	cd Week2_SpaceTime/ && pdflatex lecture3.tex && cd ..

4:
	cd Week2_SpaceTime/ && pdflatex lecture4.tex && cd ..

5:
	cd Week2_SpaceTime/ && pdflatex lecture5.tex && cd ..

h1s:
	cd Week1_IntroUnits/ && pdflatex homework1_solutions.tex && cd ../

h1:
	cd Week1_IntroUnits/ && pdflatex homework1.tex && cd ../


2:
	cd Week1_IntroUnits/ && pdflatex lecture2.tex && cd ../

1:
	cd Week1_IntroUnits/ && pdflatex lecture1.tex && cd ../

m1:
	cd MidTerm/ && pdflatex Midterm1.tex && cd ../

m1s:
	cd MidTerm/ && pdflatex Midterm1_solutions.tex && cd ../

m2:
	cd MidTerm2/ && pdflatex Midterm2.tex && cd ../

m2s:
	cd MidTerm2/ && pdflatex Midterm2_solutions.tex && cd ../

f:
	cd Final/ && pdflatex Final.tex && cd ../

syllabus: 
	pdflatex Syllabus.tex

clean:
	rm -rf Week*/lecture*.log
	rm -rf Week*/lecture*.aux
	rm -rf Week*/lecture*.bcf
	rm -rf Week*/lecture*.xml
	rm -rf Week*/lecture*.out

	rm -rf Week*/homework*.log
	rm -rf Week*/homework*.aux
	rm -rf Week*/homework*.bcf
	rm -rf Week*/homework*.xml
	rm -rf Week*/homework*.out