import argparse 
import os

parser = argparse.ArgumentParser()
parser.add_argument("a", nargs="*")
args = parser.parse_args()
query = ""



nameMap ={} #map ID token -> actual names
countMap ={} #map ID token -> count
reviewMap = {} #map ID -> review
# 7608 to 7645 = ID token start point
# grading token: 76

    #get name mapping 
file = open('nameKey.txt', 'r') #open file
x = file.read().split('\n')
file.close() #close file
for i in range(0, len(x)-1): 
    nameMap[x[i][0:4]] = x[i][6:]


for j in range(7608, 7645):
    reviewMap[str(j)] = ""

    #  get reviews
file = open('dappend', 'r') 
x = file.read().split('\n')
file.close()
file = open('pappend', 'r')
y = file.read().split('\n')
file.close()
for j in range(7608, 7645):
    for i in range(0, len(x)-2):
        if(str(j) in x[i]):
            reviewMap[str(j)] += '\n'
            reviewMap[str(j)] += x[i-2]
            reviewMap[str(j)] += x[i-1]
            reviewMap[str(j)] += ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n"
            while(("76" not in x[i+1]) and ("Evaluator Name" not in x[i+1]) and i<len(x)-2):
                i = i+1;
                reviewMap[str(j)] += x[i]
                reviewMap[str(j)] += '\n'
    for k in range(0, len(y)-2):
        if(str(j) in y[k]):
            reviewMap[str(j)] += '\n'
            reviewMap[str(j)] += y[k-2]
            reviewMap[str(j)] += y[k-1]
            reviewMap[str(j)] += ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n"
            
            while("76" not in y[k+1] and k<len(y)-2 and "Evaluator Name" not in y[k+1]):
                k = k+1;
                reviewMap[str(j)] += y[k]
                reviewMap[str(j)] += '\n'


reviewsFile = open("anote.txt", "w")
for j in range(7608, 7645):
    reviewsFile.write("\n *******************************************")
    reviewsFile.write(str(j))
    reviewsFile.write(': ')
    reviewsFile.write(nameMap[str(j)])
    reviewsFile.write('\n')
    x = reviewMap[str(j)].split('\n')
    b = [0, 0, 0, 0, 0]
    for i in range(0, len(x)-2):
        if("(select one and delete one)?" in x[i]):
            if(b[0] == 0):
                reviewsFile.write("\nEvaluation: ")
                b[0] = 1;
            reviewsFile.write("\n-")
            reviewsFile.write(x[i+1])

    for i in range(0, len(x)-2):
        if("What did the student do well?" in x[i]):
            if(b[1] == 0):
                reviewsFile.write("\n\nPraise: ")
                b[1] = 1;
            reviewsFile.write("\n-")
            while("Awesomeness:" not in x[i+1] and "Is this submission awesome?" not in x[i+1] and i < len(x)-2):
                i = i+1
                reviewsFile.write(x[i])

    for i in range(0, len(x)-2):
        if("Was it awesome? This can be blank." in x[i]):
            if(b[2] == 0):
                reviewsFile.write("\n\nAwesomeness: ")
                b[2] = 1;
            reviewsFile.write("\n-")
            while("Requirements:" not in x[i+1] and "fulfil the requirements?" not in x[i+1]):
                i = i+1
                reviewsFile.write(x[i])


    for i in range(0, len(x)-2):
        if("constrains? Please be specific." in x[i]):
            if(b[3] == 0):
                reviewsFile.write("\n\nRequirements: ")
                b[3] = 1;
            reviewsFile.write("\n-")
            while("Suggestions and criticism:" not in x[i+1]) and "that could be better about the app?" not in x[i+1]:
                i = i+1
                reviewsFile.write(x[i])

    for i in range(0, len(x)-2):
        if("UI? Please be specific." in x[i]):
            if(b[4] == 0):
                reviewsFile.write("\n\nSuggestions and criticism: ")
                b[4] = 1;
            reviewsFile.write("\n-")
            while("Peer Evaluation Form" not in x[i+1] and "Evaluator Name:" not in x[i+1] and i < len(x)-2):
                i = i+1
                reviewsFile.write(x[i])






reviewsFile.close()
print(reviewsFile)
    
#for line in nameData:
#    if("Student" in line):
#        #add the line below to HM
#        nameMap[line[4]] = next(nameData)
#        count+=1
#nameData.close()
