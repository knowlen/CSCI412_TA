# Author: Nick Knowles (knowlen@wwu.edu)
# Date: 04/30/2016
# Western Washington University 
# Department of Computer Science


nameMap = {}
count = {}
file = open('nameKey.txt', 'r')
x = file.read().split('\n')
file.close()
for i in range(0, len(x)-1): 
	nameMap[str(i)] = x[i][6:]
	count[x[i][6:]] = 0


file = open('all.txt', 'r')
allpv = file.read().split('\n')
file.close()
for i in range(0, len(x)-1):
	for j in range(0, len(allpv)-1):
		lastname = nameMap[str(i)].split(' ')
		if(lastname[0] in allpv[j] or lastname[1] in allpv[j]):
			count[nameMap[str(i)]] += 1 
print(count)

print("------------------------------   0")
for i in range(0, len(x)-1):
	if(count[nameMap[str(i)]] == 0):
		print(nameMap[str(i)])

print("------------------------------   1")
for i in range(0, len(x)-1):
        if(count[nameMap[str(i)]] == 1):
		print(nameMap[str(i)])


print("------------------------------  2")
for i in range(0, len(x)-1):
	if(count[nameMap[str(i)]] == 2):
		print(nameMap[str(i)])


print("------------------------------  3")
for i in range(0, len(x)-1):
        if(count[nameMap[str(i)]] == 3):
                print(nameMap[str(i)])


print("----- count: ", str(len(x)-1), "-------" )

for i in range(0, len(x)-1):
	print(nameMap[str(i)])


