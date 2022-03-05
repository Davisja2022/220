"""
Name: <Jessica Davis>
<Hw7>.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

def number_words(in_file_name, out_file_name):
    count = 0
    lines = in_file_name.readlines()
    for line in lines:
        words = line.split(" ")
        for word in words:
            count += 1
            print(str(count)+ " " + word, file = out_file_name)

def hourly_wages(in_file_name, out_file_name):
    lines = in_file_name.readlines()
    for line in lines:
        attributes = line.split(" ")
        attributes[2] = float(attributes[2]) + 1.65
        result = "{} {} {:.2f}".format(attributes[0], attributes[1], attributes[2]*float(attributes[3]))
        print(result, file=out_file_name)


def calc_check_sum(isbn):
    result = 0
    if "-" in isbn:
        newISBN =isbn.replace("-","")
    else:
        newISBN = isbn
    for i in range(len(newISBN), 0, -1):
        result += (int(newISBN[len(newISBN)-i]) * i)
    print(result)

def send_message(file_name, friend_name):
    with open(file_name, "r") as infile:
        fileName = "{}.txt".format(friend_name)
        with open(fileName, "w") as outfile:
            allLines = infile.readlines()
            for line in allLines:
                print(str(line), end="", file=outfile)

def encode(user_input, user_input2):
    answer = "".join(chr(ord(c)+ int(user_input2)) for c in user_input)
    return answer

def send_safe_message(file_name, friend_name, key):
    with open(file_name, "r") as infile:
        fileName = "{}.txt".format(friend_name)
        with open(fileName, "w") as outfile:
            allLines = infile.readlines()
            for line in allLines:
                ans = encode(str(line), key)
                print(ans, end="", file=outfile)

def encode_better():
    user = input("Enter word: ")
    user2nd = input("Enter key: ")
    shift_list = []
    ch_list = []

    answer = ""

    for keys in user2nd:
        shift_list.append(keys)
    for ch in user:
        ch_list.append(ch)

    for i in range(len(user)):
        shift = (ord(shift_list[i % len(shift_list)]) - 65) % 58
        answer += chr((ord(ch_list[i]) + shift - 58))


    return(answer)

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    with open(file_name, "r") as inp:
    txt = inp.read().replace("\n", "")
    with open(pad_file_name, "r") as key_text:
        shift = key_text.readline()
        fileName = "{}.txt".format(friend_name)
        with open(fileName, "w") as outfile:
            encrypt = encode_better(txt, shift)
            print(encrypt, end="", file=outfile)


if __name__ == '__main__':
    # input_file = input("Enter a text file with a sentence(s): ")
    # with open(input_file, "r") as infile:
    #     with open('demo.txt','w') as outfile:
    #         number_words(infile, outfile)
    # with open("hourly_wages.txt","r") as infile:
    #     with open('output_P2.txt','w') as outfile:
    #         hourly_wages(infile,outfile)
    # isbnInput = input("Enter ISBN #: ")
    # calc_check_sum(isbnInput)
    name = input("Enter a friends' name: ")
    infile = input("Enter a file name: ")
    user= input("Enter a key: ")
    # send_message(infile, name)
    # send_safe_message(infile, name, user)
    friend = input("E")
    fileIn = input("Enter a file name that has a message: ")
    friend = input("Enter a friends' name: ")
    send_uncrackable_message(fileIn, friend, 'pad.txt')


