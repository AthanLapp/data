import time
start_time = time.time()
fhand1 = open('group1.csv')
fhand2 = open('group2.csv')
columns1=[]
data1=[]
count1 = 0
for line in fhand1:
    columns1 = line.split(",")
    break
for line in fhand1:
    data1.append(line.split(","))
    count1+=1
columns2=[]
data2=[]
count2 = 0
for line in fhand2:
    columns2 = line.split(",")
    break
for line in fhand2:
    data2.append(line.split(","))
    count2 +=1
columnsNumber1 = len(columns1)
columnsNumber2 = len(columns2)
dataLines1 = count1
dataLines2 = count2
columns=[]
columns=columns1
columns[5] = columns[5].rstrip("\n")
columns.append(columns2[5])
currentLine = 0
taken = []
for currentLine in range(0,dataLines2):
    taken.append(data2[currentLine].pop(8))
    taken.append(data2[currentLine].pop(7))
    taken.append(data2[currentLine].pop(6))

i=0
for i in range(0,3*dataLines2,3):
    taken[i]=taken[i].rstrip("\n")
concacinated = []
for i in range(0,3*dataLines2,3):
    concacinated.append(taken[i]+"/"+taken[i+1]+"/"+taken[i+2])
    
popped=[]
for i in range(0,dataLines2):
    popped=data2[i].pop(5)
    data2[i].append(concacinated[i])
    data2[i].append(popped)
for i in range(0,dataLines1):
    data1[i][-1] = data1[i][-1].rstrip("\n")
    data1[i].append("Null")
    
data=[]
data=data+data1+data2

fout = open("grouped.csv", "w")
columnsOutput=""
for i in range(0,len(columns)):
    columnsOutput = columnsOutput+columns[i]+","
columnsOutput=columnsOutput.rstrip(",")+"\n"
fout.write(columnsOutput)

line=0
lineOutput=""
for line in range(0, len(data)):
    for i in range(0,len(columns)):
        lineOutput=lineOutput+data[line][i]+","
    lineOutput=lineOutput.rstrip(",")+"\n"
fout.write(lineOutput)
fout.close()

print("--- %s seconds ---" % (time.time() - start_time))
    
