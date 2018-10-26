from time import sleep


filename = raw_input()

print filename

wait_time = 10 #seconds
check = False
iteration = 0
while not check:
    iteration += 1
    try:
        with open(filename, 'r') as search:
            lines = search.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].rstrip()
                if lines[i].startswith('     = Timing results'):
                    index = 0
                    for j in lines[i+5]:
                        index += 1
                        if j == ':':
                            print 'Total Time:', lines[i+5][index-3:21]
                            check = True
                            break
    except:
        pass

    if iteration >= 30:
        break

    sleep(wait_time)
