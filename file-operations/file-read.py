from sys import argv
script, filename = argv

txt = open(filename,'a+')
txt.seek(0,0)
print(txt.read())
txt.seek(0,0)

print(txt.read())


txt.close()