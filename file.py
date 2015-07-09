f = open("filetemp.txt", "a")
f.write("Hello World! Good bye World! \n Hello Again!")

f = open("filetemp.txt", "r")
filebody = f.read()
line = f.readline()

f.close()
