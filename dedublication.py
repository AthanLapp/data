import time
#from fuzzywuzzy import fuzz

# fuzz.WRatio('geeks for geeks', 'Geeks For Geeks')


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
    if string1 == "" or string2 == "":
        return 0
    comp=0
    string1=string1.upper()
    string2=string2.upper()
    if string1 in string2 or string2 in string1:
        return 100
    string1=list(string1)
    string2=list(string2)
    i=0
    if len(string1)>len(string2):
        for i in range(0,(len(string1)-len(string2))+2):
            string2.append("")
    stringL = len(string1)
    i=0
    for i in range(0,stringL):
        if i <stringL-1:
            if string1[i] == string2[i] or string1[i] == string2[i+1] :
                comp+=1
        else:
            if string1[i] == string2[i]:
                comp+=1
    comp=comp/stringL
    return comp
i=0
#for line in range(0,lines1):
for line in range(0,500):
    duplicates.append(data1[line])
    duplicates.append(0)
    cont = False
    for col in range(1,len(columns1)-1):
        for line2 in range(line+1,500): #,lines1)
            sims=0
            for col2 in range(1,len(columns1)-1):
                sim = compareString(data1[line][col],data1[line2][col2])
                if sim > 27:
                    duplicates.append(data1[line2])
                    cont=True
                    for j in range(1,len(columns1)-1):
                        sims+= compareString(data1[line][j],data1[line2][j])
                    sims = round(sims/(len(columns1)-2))
                    duplicates.append(sims)
                    cont=True
                    continue
                if cont: continue
        if cont: continue

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
fout = open("deduplicated.csv", "w")
fout.write(columnsOutput)
fout.write(lineOutput)
fout.close()


print("--- %s seconds ---" % (time.time() - start_time))
