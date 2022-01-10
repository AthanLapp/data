import time
import multiprocessing

start_time = time.time()

def mainz(data1,lencol,linestart,linestop,end,return_dict):
	start_time_function = time.time()
	col = 0
	col2 = 0
	sim = 0
	sims = 0
	cont = 0
	j = 0
	for line in range(linestart,linestop):
		cont = False
		for line2 in range(line+1,end): #,lines1)
			cont = False
	return_dict[data1] = (time.time() - start_time_function)
	print("--- function",data1,"took",(time.time() - start_time_function),"seconds ---")

def main():	
	time1=1.0
	time2=2.0
	time3=3.0
	time4=4.0
	start1=0
	end=20000
	end1=2680
	start2=end1
	end2=5846
	start3=end2
	end3=9989
	start4=end3
	end4=end
	loopn=0
	limit=0.02
	step=1
	while (abs(time2 - time1) > limit) or (abs(time3 - time2) > limit) or (abs(time4 - time3) > limit):
		loopn+=1
		print("Loop no: ",loopn)
		manager = multiprocessing.Manager()
		return_dict1 = manager.dict()
		return_dict2 = manager.dict()
		return_dict3 = manager.dict()
		return_dict4 = manager.dict()
		p1 = multiprocessing.Process(target = mainz, args=(1,1,start1,end1,end,return_dict1))
		p2 = multiprocessing.Process(target = mainz, args=(2,1,start2,end2,end,return_dict2))
		p3 = multiprocessing.Process(target = mainz, args=(3,1,start3,end3,end,return_dict3))
		p4 = multiprocessing.Process(target = mainz, args=(4,1,start4,end4,end,return_dict4))
		p1.start()
		p2.start()
		p3.start()
		p4.start()
		p1.join()
		p2.join()
		p3.join()
		p4.join()
		time1=return_dict1.values()[0]
		time2=return_dict2.values()[0]
		time3=return_dict3.values()[0]
		time4=return_dict4.values()[0]
		print("Time taken to execute each function: ", time1, time2, time3, time4)
		print("--- Total running time: %s seconds ---" % (time.time() - start_time))
		cont1=False
		cont2=False
		if (time1-time2>limit):
			end1-=step
			start2-=step
			cont1=True
		if (time2-time3>limit):
			if cont1 == False:
				end2-=step
				start3-=step
				cont2 = True
		if (time3-time4>limit):
			if cont2==False:
				end3-=step
				start4-=step
		if (time2-time1>limit):
			end1+=step
			start2+=step
			cont1=True
		if (time3-time2>limit):
			if cont1==False:	
				end2+=step
				start3+=step
				cont2=True
		if (time4-time3>limit):
			if cont2==False:
				end3+=step
				start4+=step
	print('Found limits for each function in ascending order:', start1,end1,start2,end2,start3,end3,start4,end4)


if __name__ == '__main__':
	main()