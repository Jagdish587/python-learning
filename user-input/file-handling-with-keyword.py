from sys import argv

script = argv

print(f"My script is {script}")


with open('with-code-sample.txt', 'r') as filePtr:
    data = filePtr.read()
    print(data)

with open('with-code-sample.txt', 'a+') as filePtr:
    data = filePtr.write("I am from code\n")


with open("with-code-sample.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split('c')
        print(word)
