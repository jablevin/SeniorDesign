from time import sleep
import os
import datetime

filename = raw_input()
location = raw_input()
copy_location = raw_input()

now = datetime.datetime.now()

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

    if iteration >= 360:
        break

    sleep(wait_time)



DNB_list = []
for file_ in range(1, 38):
    with open(location + 'deck.37.' + str(file_) + '.dnb.out', 'r') as search:
        lines = search.readlines()
        state_line = {}
        counter = 1
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()

    for i in range(len(lines)):
        if 'DNBR' in lines[i]:
            for j in range(27):
                DNB_list.append(float(lines[j+i+1][60:71]))
    search.close()
    del lines

print min(DNB_list)

with open(copy_location + 'DNB.out','w') as f:
	f.write(str(now) + '\n')
	f.write('MDNBR:' + str(min(DNB_list)) + '\n')

f.close()
