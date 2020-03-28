31:
	cd Week12_WeakInteraction/  && pdflatex lecture31.tex  && cd ..

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