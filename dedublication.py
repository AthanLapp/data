import time

start_time = time.time()

fhand1 = open('dedublication.csv')
columns1=[]
data1=[]
lines1 = 0
for line in fhand1:
    columns1 = line.split(",")
    break
for line in fhand1:
    data1.append(line.split(","))
    lines1+=1
column=0
for line in range(0,lines1):
    data1[line][-1] = data1[line][-1].rstrip("\n")
duplicates = []
col = 0
col2 = 0
sim = 0
sims = 0
cont = False
j = 0

def compareString(string1,string2):
    comp=0
    string1.upper()
    string2.upper()

    if((string1=="")or(string2=="")):
        return 0
    string1=list(string1)
    string2=list(string2)
    i=0
    if(len(string1) >= len(string2)):
        for i in range(len(string2),len(string1)):
            string2.append("")
    else:
        for i in range(len(string1),len(string2)):
            string1.append("")
    for i in range(0,len(string1)):
        if string1[i] == string2[i]:
            comp+=1
    comp=comp/(i)*100
    return round(comp)

i=0
#for line in range(0,1000):
for line in range(0,line1):
    cont = False
    for line2 in range(line+1,line1): #,1000)
        cont = False
        for col in range(1,len(columns1)-1):
            if cont: continue
            sims=0
            sim=0
            sim=compareString(data1[line][col],data1[line2][col])
            if(col==4):
                sim=0
            if (sim>80):
                cont=True
                count=0
                for j in range(1,len(columns1)-1):
                    sims+= compareString(data1[line][j],data1[line2][j])
                    count+=1
                sims = sims/count
                if sims >53 :
                    duplicates.append(data1[line])
                    duplicates.append(data1[line2])
                    duplicates.append(sims)
        
columns=columns1

columnsOutput=""
for i in range(0,len(columns)):
    columnsOutput = columnsOutput+columns[i].rstrip("\n")+","
columnsOutput=columnsOutput.rstrip(",")+"\n"

line=0
lineOutput=""
i=0
j=0
for line in duplicates:
    if type(line) == int or type(line) == float:
        lineOutput=lineOutput+str(line)+","
    else:
        for word in line:
            if word == "\n":
                continue
            lineOutput=lineOutput+str(word)+","
    lineOutput=lineOutput.rstrip(",")+"\n"
fout = open("dedublicatedWhole.csv", "w")
fout.write(columnsOutput)
fout.write(lineOutput)
fout.close()


print("--- %s seconds ---" % (time.time() - start_time))
