import os

filename = 'deck.37.1.dnb.out'
DNB_list = []
for file_ in range(1, 38):
    # with open('C:/Users/Jacob Blevins/Documents/Classes/Senior_Design/core_runs/core2/deck.37.' + str(file_) + '.dnb.out', 'r') as search:
    with open(location + str(file_) + '.dnb.out', 'r') as search:
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

min(DNB_list)
