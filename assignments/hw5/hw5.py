"""
Name: <Jessica Davis>
<hw5>.py

Problem: <this exercise utilizes strings, list, indexing, slicing in order to create user interactive programs.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Jessica Davis>
"""


def name_reverse():
    user_input = input("Enter a name(First, Last): ")
    name_change = user_input.split(' ')
    print(str(name_change[-1]) + ', ' + str(name_change[0]))



def company_name():
    user_input = input('enter a domain: ')
    domain_name = user_input.split('.')
    print(str(domain_name[1]))


def initials():
    user_input = int(input("how many students in the class?: "))
    for i in range(1, user_input + 1):
        student_name = input('what is the name of student ' + str(i) + "?: ")
        name_split = student_name.split(' ')
        first_intital = str(name_split[0])
        second_intial = str(name_split[1])
        print(first_intital[0] + second_intial[0])


def names():
    user_names = input("Enter list of names (seperated by commmas): ")
    list_names = user_names.split(",")
    for name in list_names:
        split_names = name.split(' ')
        first_intial = str(split_names[-2])
        second_intial = str(split_names[-1])
        print(first_intial[0] + second_intial[0], end=" ")

def thirds():
    list_sen = []
    all_sens = []
    sentences = int(input("Enter the number of sentences: "))
    for i in range(1, sentences + 1):
        sen = input("Enter sentence " + str(i) + ": ")
        list_sen.append(sen)
    for sentence in list_sen:
        new_sentences = ''
        for i in range(0, len(sentence), 3):
            new_sentences += sentence[i]
        all_sens.append(new_sentences)
    for sens in all_sens:
        print(sens)


def word_average():
    user_input = input('Enter a sentence: ')
    word_split = user_input.split()
    average = sum(len(word) for word in word_split)/ len(word_split)
    print(average)


def pig_latin():
    sen = input("Enter a sentence to convert to pig latin: ")
    words = sen.split(" ")
    for word in words:
        moved_letter = word[0]
        word = word.replace(word[0], '')
        print(str(word) + moved_letter, end="ay ", sep=" ")


if __name__ == '__main__':
   # name_reverse()
    #company_name()
    #initials()
    #names()
   # thirds()
   # word_average()
    #pig_latin()


