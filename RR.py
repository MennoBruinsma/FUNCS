import time
#The procceses need to be in chronoligical order, so left is the firts arriving process.
#The first number is the process ID, the second number is the arrival time and the last the execution time.
process_list = [[0,0,8],[1,0,6],[2,0,4]]
cpu_time = 1
starttime= time.time()
k= 0
seconds_passed = 0
start_system = True
active_programs= []

print("This is a small program to show how round robin works given the assumptions that there is no I/O and the execution times are known.")
while True:

    if len(process_list) == 0:
        #all processes are done
        print('\n')
        print("All processes are done, good job CPU!")
        print("It took the RR algorithm " +str(seconds_passed) + " seconds.")
        break

    elif process_list[0][1] - seconds_passed <= 0:
        #active processes
        for i in range(len(process_list)):
            if process_list[i][1] <= seconds_passed and i not in active_programs:
                active_programs.append(process_list[i])
        if len(process_list) == 1:
            k=0
        print('\n')
        print("Process ran by CPU " + str(active_programs[k]))
        if len(active_programs) > 1:
            indexed_list = active_programs[:k] + active_programs[k+1:]
            print("Arrived but waiting processes " + str(indexed_list))
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
                seconds_passed += cpu_time
                time.sleep(cpu_time - ((time.time() - starttime) % cpu_time))
                continue
        if k < len(process_list) -1:
            if process_list[k+1][1] - seconds_passed <= 0:
                k += 1
        elif k == len(process_list) -1:
            k = 0
    else:
        #no active processes
        print("\n")
        print("no active processes")
    print(str(seconds_passed) + " seconds have passed.")
    seconds_passed += cpu_time
    time.sleep(cpu_time - ((time.time() - starttime) % cpu_time))

