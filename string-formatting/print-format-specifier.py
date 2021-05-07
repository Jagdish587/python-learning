from string import Template

name = "Jagdish"
age = 26
salary = 35000.56

print("Hello my name is %s , my age id %d and salary is %.3f " %(name, age, salary))
print("Hello my name is %s " %name)
print("Hello my age is %d " %age)
print("Hello my salary is %30.2f " %salary)

mydict = {'quantity': 6, 'item': 'bananas', 'price': 1.74}
print(' %(item)s %(quantity)d %(price)f ' %mydict)

errno = 50159747054
name = 'Bob'

print("Hey %s , there is an %x errno " %(name, errno))
print("Hello {} you got error {:x} ".format(name, errno))

a = 5
b = 15

result = f"sample output gives you {a + b} ok "
print(result)

a = 5
b = 25

def my_fstringfunc():
    return f"sample output gives you {a + b} "

print(my_fstringfunc())

Student = [('Ram',90), ('Ankit',78), ('Bob',92)]
t = Template('Hi $name, you have got $marks marks')
 
for i in Student:
     print (t.substitute(name = i[0], marks = i[1]))



template = Template('$name is the $job')
string = template.substitute({'name' : 'Raju Kumar',
                      'job' :'TCE'})
print(string)

