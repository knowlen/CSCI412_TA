#!/bin/bash
# Author: Nick Knowles (knowlen@wwu.edu)
# Date: 04/30/2016
# Western Washington University 
# Department of Computer Science

if [ $1 == "-h" ]; then
    echo "usage: totext.sh target_directory"
    echo "target_directory: The folder containing files to be converted."
    echo "                  Make sure to unzip everything!."
    exit 0
fi

DIR=$1
if [[ $DIR != */ ]]; then
    DIR=$DIR/
    echo "     "$DIR
fi
chmod 770 $DIR
chmod 770 $DIR*.docx;
chmod 770 $DIR*.pdf;
chmod 770 $DIR*.txt;

WORKING=$DIR'text_conversion/'

mkdir $WORKING

cp $DIR/*.pdf $WORKING
cp $DIR/*.docx $WORKING
cp $DIR/*.txt $WORKING

cd $WORKING

files=*.pdf
for i in $files; do
	pdftotext $i;
done

mkdir pdf_texts;
mv *.txt pdf_texts;


soffice --headless --convert-to txt *.docx;
mkdir doc_texts;
mv *.txt doc_texts;

ls | wc;
ls doc_texts | wc;
ls pdf_texts | wc;


cd pdf_texts; 
cat *.txt >> ./../../all_pdfs.txt;
cd ../doc_texts;
cat *.txt >> ./../../all_docs.txt;
cd ./../..;
cat *.txt >> all.txt;


echo "Done! Converted files can be found in $WORKING "
exit 1
