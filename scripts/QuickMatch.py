# Author: Nick Knowles (knowlen@wwu.edu)
# Date: Spring 2016
# Western Washington University 
# Department of Computer Science


# notes:
# ** Script can hang on the random number loop (due to how it's 
#    assigning matches) -I wrote this when I was still learning 
#    Python & everything is brute force.
#    Just kill the process (ctrl+c) and run script again if it stalls. 
#
# ** File output when ran in Cygwin is wrong (no \n). 
#    Correct if ran through IDE though. 


import argparse
import os
from random import *

parser = argparse.ArgumentParser()
parser.add_argument("names_file", help="path to file containing names of students (copy/paste from canvas People page).")
parser.add_argument("out_dir", help="path to directory you want keys saved.")
args = parser.parse_args()



nameMap ={} #map ID token -> actual names
countMap ={} #map ID token -> count
peerMap = {} #map ID -> peer ID
count = 7608 #ID token start point
idStart = count # grading token: 76   

# input file pre-processing #
cmd = "sed -i '/^\s*$/d' " + args.names_file
os.system(cmd)
cmd = "tail -1 " + args.names_file
saved_last_line = os.popen(cmd).read()
cmd = "sed -i '$ d' " + args.names_file
os.system(cmd)
nameData = open(args.names_file)


for line in nameData:
    if "Student" in line or "Name" in line:
        #add the line below to HM
        nameMap[str(count)] = next(nameData)
        count+=1
nameData.close()

for x in range(idStart, count):
    countMap[str(x)] = 3
    peerMap[str(x)] =[]

for x in range(idStart, count):
    for y in range(0, 3): #1 person grades 3. 
        sampleId = randint(0,(count-1)-idStart) + idStart
        #random sample a student name without replacement > 3.  
        while ((countMap[str(sampleId)] < 1) or (sampleId in peerMap[str(x)]) or (x == sampleId)):
            sampleId = randint(0,(count-idStart)-1) + idStart

        peerMap[str(x)].append(sampleId)    
        countMap[str(sampleId)]-=1


cmd = "echo '" + saved_last_line + "' >> " + args.names_file
os.system(cmd)


out_file = args.out_dir 
if not out_file.endswith("/"):
    out_file = out_file + "/"
peerFile = open(out_file + "412PeerMap1.txt", "w")
keyFile = open(out_file + "412NameKey1.txt", "w")
testFile = open(out_file + "412testFile1.txt", "w")
for x in range(idStart, count):
    #z = "name: idNumber" eg; "Nick: 7698"
    z = (str(x) + ": " + nameMap[str(x)])
    keyFile.write(z)

    #y = "name \n [id, id, id]" 
    y = (nameMap[str(x)] + " "+ str((peerMap[str(x)])))
    peerFile.write(y)
    peerFile.write('\n\n')

    #test = "id: id, id, id" -check ctrl+f for any bugs
    w = (str(x) + ":  "+ str((peerMap[str(x)])))
    testFile.write(w)
    testFile.write('\n\n')
    
keyFile.close()
peerFile.close()
testFile.close()
#print(keyFile)
#print(peerFile)
#print(testFile)
cmd = "cat " + out_file + "*.txt"
os.system(cmd)
print("done")
