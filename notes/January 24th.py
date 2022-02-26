
print("Hello, World!")

print("Hello", "world!")

print(2 + 3)

print(2.0 + 3.0)

print("2 + 3 =", 2 + 3)

print(2 * 3)

print(2 ** 3)

print(2 / 3)

for i in range(5):
    print(i * i)

for d in[3,1,4,1,5]:
    print(d, end=" ")

for i in range(4):
    print("Hello", end="!!!")

for i in range(7, 3, -1):
    print(i, 2**i)

def horsepower():
    watts = eval(input('enter a number of watts: '))
    hp = watts / 745.7
    print(hp)



def thirds():
    list_sen = []
    sentences = int(input("Enter the number of sentences: "))
    for i in range(1, sentences + 1):
        sen = input("Enter sentence " + str(i) + ": ")
        for j in range(0, len(sen), 3):
            third_chr = sen[i]
            pull_letters = sen[0:3]


def pull_letters():
    sentences = int(input("Enter the number of sentences: "))
    for i in range(1, sentences + 1):
        sen = input("Enter sentence " + str(i) + ": ")
        for j in range(0, len(sen), 3):
            pull = sentences[0:3]
    print(pull)




def third():
    counter = 0
    terms = eval(input("Enter the number of sentences:"))
    for i in range(terms) :
        output = ' '
        counter = counter + 1
        sentence = input("Enter Sentence {}:".format(counter))
        for j in range(0, len(sentence), 3):
            thirds = sentence[j]
            output = output + thirds
    print (output)





third()