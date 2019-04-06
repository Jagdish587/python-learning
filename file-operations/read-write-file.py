from sys import argv

from os.path import exists

script , from_file , to_file = argv

print(f"I am {script} file")
print(f"from file = {from_file}")
print(f"to file = {to_file}")

in_file = open(from_file,'r')
out_file = open(to_file,'w+')

in_data = in_file.read()
out_file.write(in_data)

print("Done writing file ")
in_file.close()
out_file.close()