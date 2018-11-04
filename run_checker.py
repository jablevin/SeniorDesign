from time import sleep
import os
import datetime
# d = 'C:/Users/Jacob Blevins/Documents/Classes/SeniorDesign/core_runs/core2/'

filename = raw_input()
location = raw_input()
copy_location = raw_input()


# filename = d + 'smr_7x7.out'
# location = d
# copy_location = d

now = datetime.datetime.now()

wait_time = 1 #seconds
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
    if iteration >= 1:
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


with open(copy_location + 'Output.out','w+') as f:
    f.write(str(now) + '\r\n')
    f.write('MDNBR: ' + str(min(DNB_list)) + '\r\n')
    f.write('k-eff -------------' + '\r\n')
    for i in list(state_line.keys()):
        f.write('State ' + str(i) + ': ' + str(k_eff[i]) + '\r\n')

f.close()
