import time
#The procceses need to be in chronoligical order, so left is the firts arriving process.
#The first number is the process ID, the second number is the arrival time and the last the execution time.
process_list = [[0,0,5.5],[1,4,6],[2,5,4]]
cpu_time = 1
starttime= time.time()
k= 0
seconds_passed = 0
start_system = True
active_programs= [] 
print("This is a small program to show how first in first out works given the assumptions that there is no I/O and the execution times are known.")
while True:

    if len(process_list) == 0:
        #all processen are done
        print("All processes are done, good job CPU!")
        print("It took the FIFO algorithm " +str(seconds_passed) + " seconds.")
        break

    elif process_list[0][1] - seconds_passed <= 0:
        #active processen
        for i in range(len(process_list)):
            if process_list[i][1] <= seconds_passed and i not in active_programs:
                active_programs.append(process_list[i])
        if len(process_list) == 1:
            k=0
        print("\n")
        print("Process ran by CPU " + str(active_programs[0]))
        if len(active_programs) > 1:
            print("Arrived but waiting processes " + str(active_programs[1:]))
        else:
            print("No arrived processes")
        active_programs= []
        
        if process_list[k][2] > 0:
            process_list[k][2] = float(process_list[k][2] - 1)
            if (process_list[k][2]) <=0 :
                del process_list[k]
                if k > 1:
                    k-=1
                print(str(seconds_passed) + " seconds have passed.")
                seconds_passed += 1
                time.sleep(1.0 - ((time.time() - starttime) % 1.0))
                continue
        elif k == len(process_list) -1:
            k = 0
    else:
        #no active processes
        print('\n')
        print("no active processes")
    print(str(seconds_passed) + " seconds have passed.")
    seconds_passed += 1
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))