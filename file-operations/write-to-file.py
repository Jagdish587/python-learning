from sys import argv

script , file_name =  argv

print(f"Hi I am {script} file ")
print(f"Hi I am reading {file_name} file ")

txt = open(file_name,'w')

txt.truncate()

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

print("Done Writing..!!")

txt.close()