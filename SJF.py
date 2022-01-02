import time
#The proccese need to be in chronoligical order, so left is the firts arriving process.
#The first number is the process ID, the second number is the arrival time and the last the execution time.
process_list = [[0,0,5], [1,3,4], [2,4,7], [3,6,2]]
cpu_time = 1
k= 0
seconds_passed = 0
starttime= time.time()
active = False
active_programs= []
shortest_process= []
print("This is a small program to show how  shortest process firts works given the assumptions that there is no I/O and the execution times are known.")
while True:

    if len(process_list) == 0:
        #all processes are done
        print('\n')
        print("All processes are done, good job CPU!")
        print("It took the SJF algorithm " +str(seconds_passed) + " seconds.")
        break

    elif process_list[k][1] - seconds_passed <= 0:
        #active processes
        for i in range(len(process_list)):
            if process_list[i][1] <= seconds_passed and i not in active_programs:
                active_programs.append(process_list[i])
        if active == False:
            active= True
            for i in range(len(active_programs)):
                shortest_process.append(active_programs[i][2])
            k = shortest_process.index(min(shortest_process)) 
            shortest_process=[] 

        print("\n")
        print("Process ran by CPU " + str(active_programs[k]))
        if len(active_programs) > 1:
            indexed_list = active_programs[:k] + active_programs[k+1:]
            print("Arrived but waiting processes " + str(indexed_list))
        else:
            print("No arrived processes")
   
        active_programs= []
        
        #lowering time and deleting process if time =0
        if process_list[k][2] > 0:
            process_list[k][2] = float(process_list[k][2] - 1)
            if (process_list[k][2]) <=0 :
                del process_list[k]
                k=0
                print(str(seconds_passed) + " seconds have passed.")
                seconds_passed += 1
                time.sleep(1.0 - ((time.time() - starttime) % 1.0))
                active= False
                continue
    else:
        print("\n")
        print("no active processes")
    print(str(seconds_passed) + " seconds have passed.")
    seconds_passed += 1
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))