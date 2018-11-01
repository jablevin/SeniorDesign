from time import sleep
import os
import datetime

filename = raw_input()
location = raw_input()
copy_location = raw_input()

now = datetime.datetime.now()

wait_time = 60 #seconds
check = False
iteration = 0
# Finding when the run is complete
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


#Finding all K-eff
state_line = {}
counter = 1
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
    if lines[i].startswith('******************************* STATE_'):
        state_line[counter] = i
        counter += 1

k_eff = {}
for i in list(state_line.keys()):
    if i != list(state_line.keys())[len(state_line)-1]:
        upper_line = state_line[i+1]
    else:
        upper_line = len(lines)
    for j in range(state_line[i], upper_line):
        if 'k-eff' in lines[j]:
            k_eff[i] = float(lines[j][12:])


# Finding minimum DNB ratio
DNB_list = []
for file_ in range(1, 38):
    with open(location + 'deck.37.' + str(file_) + '.dnb.out', 'r') as search:
        lines = search.readlines()
        counter = 1
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()

    for i in range(len(lines)):
        if 'DNBR' in lines[i]:
            for j in range(27):
                DNB_list.append(float(lines[j+i+1][60:71]))
    search.close()
    del lines


with open(copy_location + 'DNB.out','w') as f:
	f.write(str(now) + '\n')
	f.write('MDNBR:' + str(min(DNB_list)) + '\n')
    for i in list(state_line.keys()):
        f.write('State ' + str(i) + ':  ' + str(k_eff[i]) + '\n')

f.close()
