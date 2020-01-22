import threading, time

def printfunc(names):
    for n in names:
        print(n)
        time.sleep(3)


params = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17],
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17]
]

j = 0
for i in range(0, len(params), 2):
    
    batch = params[i:i+2]
    threads_list = []
    for b in batch:
        print("Creating thread - {}".format(j))
        x = threading.Thread(target=printfunc, args=(b, ) )
        print("Starting thread - {}".format(j))
        x.start()
        threads_list.append(x)
        j+=1

    for i in threads_list:
        i.join()






