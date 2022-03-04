'''
Jessica Davis
Lab4.py
Using Graphics, strings, loops, and encoding to create user interactive program.
This is my work and my work only. - Jessica Davis
'''


def weighted_average(in_file_name, out_file_name):
    class_avg = 0
    succesful = 0
    lines = in_file_name.readlines()
    for line in lines:
        weightsTotal = 0
        avg = 0
        total = 0
        attr = line.split(": ")
        name = attr[0]
        scores = attr[1].split(" ")
        for i in range(0, len(scores), 2):
            weightsTotal += int(scores[i])
        if weightsTotal == 100:
            succesful += 1
            for x in range(0, len(scores), 2):
                total += (int(scores[x]) * int(scores[x+1]))
            avg = total/100
            class_avg += avg
            result = "{}'s average: {:.1f}".format(name, avg)
        elif weightsTotal < 100:
            result = "{}'s average: Error: The weights are less than 100".format(name)
        elif weightsTotal > 100:
            result = "{}'s average: Error: The weights are more than 100".format(name)
        print(result, file=out_file_name)
    final = "Class avaerage: {:.1f}".format(class_avg/succesful)
    print(final, file=out_file_name)

if __name__ == '__main__':
    with open("lab7","r") as infile:
        with open("outcome.txt","w") as outfile:
            weighted_average(infile, outfile)

