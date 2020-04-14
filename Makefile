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

28:
	cd Week12_WeakInteraction//  && pdflatex lecture28.tex  && cd ..

27:
	cd Week12_WeakInteraction//  && pdflatex lecture27.tex  && cd ..

26:
	cd Week12_WeakInteraction/  && pdflatex lecture26.tex  && cd ..

h10s:
	cd Week12_WeakInteraction//  && pdflatex homework10_solutions.tex  && cd ..

h10:
	cd Week12_WeakInteraction//  && pdflatex homework10.tex  && cd ..

h9s:
	cd Week8and9_ColliderPhysics/  && pdflatex homework9_solutions.tex  && cd ..

h8s:
	cd Week8and9_ColliderPhysics/  && pdflatex homework8_solutions.tex  && cd ..




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