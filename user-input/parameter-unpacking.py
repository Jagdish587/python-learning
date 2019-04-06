from sys import argv

file_name , first_num , second_num, third_num = argv

print("file name = "+file_name)
print("first_num = "+first_num)
print("second_num = "+second_num)
print("third_num = "+third_num)

sum = int(first_num ) + int (second_num)+ int (third_num)

print("total = ",sum)