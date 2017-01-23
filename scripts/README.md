Scripts Directory
---------------------


##### Generating anonymous peer review matches 
Copy/paste the People page (from "Name"-\>bottom of webpage) of the class Canvas into a text editor (Vim or Mousepad recommended), save to file.  
Pass this file and an output directory to **QuickMatch.py**,  
> **$**./QuickMatch.py names\_file output\_dir   

This will create 3 files which represent 1 student-\>3 student pairings, and the randomized key value assigned to each student. 


##### Pre-processing survey forms
Please unzip all surveys into one centralized folder. **toText.sh** will do most of the pre-processing required to make the other scripts work. Namely, it will convert all .pdf and .docx files to .txt, then concatenate everything into one large .txt file. It also sets up a file structure within the directory you give it that can be utilized by the other scripts.    

##### Grading
Grading is done with pvgrader.py and parser.py. 

####Documentation
* *toText.sh*   
*This script converts all .pdf and .docx files of a specified directory (input\_directory) into .txt, and concatinates all peer evaulations into one text file.*    
Usage `$./toText.sh input_directory`  
Arguements/Flags: [-h], input\_directory  
input\_directory: Path to the folder containing   

* *QuickMatch.py*   
*Creates anonymous student pairings for peer review, as well as an assigned key value for each student.*      
Usage: `$python QuickMath.py names_file out_dir`     
Arguements/Flage: names\_file, out\_dir   

* *parser.py*   
Usage: `$python parser.py`  
Arguements/Flage:    

* *pvgrader.py*  
Usage:    
Arguements/Flage:  

