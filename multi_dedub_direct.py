import time
from multiprocessing import Process

start_time = time.time()

duplicates1 = []
duplicates2 = []

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

def mainz1(data1,lencol,linestart,linestop,end):
	duplicates1=[]
	col = 0
	col2 = 0
	sim = 0
	sims = 0
	cont = False
	j = 0
	fout1 = open("dedublicated20000_1.csv", "w")
	for line in range(linestart,linestop):
		cont = False
		for line2 in range(line+1,end): #,lines1)
			cont = False
			for col in range(1,lencol-1):
				if cont: continue
				sims=0
				sim=0
				sim=compareString(data1[line][col],data1[line2][col])
				if(col==4):
					sim=0
				if (sim>80):
					cont=True
					count=0
					for j in range(1,lencol-1):
						sims+= compareString(data1[line][j],data1[line2][j])
						count+=1
					sims = sims/count
					if sims >60 :
						fout1.write(str(data1[line]).lstrip("[").rstrip(",]")+"\n")
						fout1.write(str(data1[line2]).lstrip("[").rstrip(",]")+"\n")
						fout1.write(str(sims)+"\n")
	fout1.close()
	print("--- function 1 took %s seconds ---" % (time.time() - start_time))


def mainz2(data1,lencol,linestart,linestop,end):
	duplicates2=[]
	col = 0
	col2 = 0
	sim = 0
	sims = 0
	cont = False
	j = 0
	fout2 = open("dedublicated2000_2.csv", "w")
	for line in range(linestart,linestop):
		cont = False
		for line2 in range(line+1,end): #,lines1)
			cont = False
			for col in range(1,lencol-1):
				if cont: continue
				sims=0
				sim=0
				sim=compareString(data1[line][col],data1[line2][col])
				if(col==4):
					sim=0
				if (sim>80):
					cont=True
					count=0
					for j in range(1,lencol-1):
						sims+= compareString(data1[line][j],data1[line2][j])
						count+=1
					sims = sims/count
					if sims >60 :
						fout2.write(str(data1[line]).lstrip("[").rstrip(",]")+"\n")
						fout2.write(str(data1[line2]).lstrip("[").rstrip(",]")+"\n")
						fout2.write(str(sims)+"\n")
	fout2.close()
	print("--- function 2 took %s seconds ---" % (time.time() - start_time))


def main():	
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
	columns=columns1
	columnsOutput=""
	for i in range(0,len(columns)):
		columnsOutput = columnsOutput+columns[i].rstrip("\n")+","
	columnsOutput=columnsOutput.rstrip(",")+"\n"
	col = 0
	col2 = 0
	sim = 0
	sims = 0
	cont = False
	j = 0
	i=0
	p1 = Process(target = mainz1, args=(data1,len(columns1),0,5870,20000))
	p2 = Process(target = mainz2, args=(data1,len(columns1),5870,20000,20000))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	fhand = open('dedublicated20000_1.csv')
	fout = open("dedublicated20000multi.csv", "w")
	fout.write(columnsOutput)
	for line in fhand:
		fout.write(line)
	fhand = open('dedublicated20000_2.csv')
	for line in fhand:
		fout.write(line)
	fout.close()
	print("--- Total running time: %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
	main()