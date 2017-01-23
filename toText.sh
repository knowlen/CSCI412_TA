#!/bin/bash

#a: nick knowles
#d: 04/30/2016

#file structure for this is:
#00pv>raw>allfiles
#1) extract everything to allfiles
#2) cd to allfiles 
#3) run this script


chmod 777 *.docx;
chmod 777 *.pdf;
chmod 777 *.txt;

files=*.pdf
for i in $files; do
	pdftotext $i;
done
mkdir ptexts;
mv *.txt ptexts;


soffice --headless --convert-to txt *.docx;
mkdir dtexts;
mv *.txt dtexts;

ls | wc;
ls dtexts | wc;
ls ptexts | wc;


cd ptexts; 
cat *.txt >> ./../../allp.txt;
cd ../dtexts;
cat *.txt >> ./../../alld.txt;
cd ./../..;
cat *.txt >> all.txt;


echo "Done! Converted files can be found in \"texts\" folder "

