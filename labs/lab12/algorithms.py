

def read_data(filename):
    file = open(filename, 'r')
    read = file.readline()
    split = read.split()
    i = 0
    list = []
    while read:
        while i < len(split):
            num = eval(split[i])
            list.append(num)
            i = i + 1
        read = file.readline()
        split = read.split()
        i = 0
    return list

def is_in_linear(search_val, values):
    if search_val in values:
        return True
    else:
        return False
   # while read is open:








    # reads values and returns a list
#def is_in_linear(search_val, values):
        # PERFORMS LINEAR SEARCH. GO THROUGH LIST AND SEARCH FOR PARTICULAR VALUE


