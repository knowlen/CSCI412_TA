# Author: Nick Knowles
# Date: Spring 2016
# Western Washington University 


# this script was used to facilitate anonymous
# peer-review matchups for CSCI412 Spring
# quarter 2016.

# dev notes:
#** Script will sometimes hang on the
#   random number loop (due to how it's 
#   assigning matches; sometimes last
#   IDs left will not break loop).
#   Solution = kill and run again if stalls
#   more than a few seconds. 
#** File output when ran in Cygwin is
#   wrong (no \n). Correct in IDLE though. 
import argparse
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
nameData = open(args.names_file)
for line in nameData:
    if("Student" in line):
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
os.systemn(cmd)
print("done")
