import os
#open(), paramters: filename, and mode
#4 different modes

f = open("demofile.txt")
f = open("demofile.txt", "rt") #Same as above
f.close()

#read() "r" - read
f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open("demofile.txt", "r")
print(f.read(5))
f.close()

#readline()
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()

#loop
f = open("demofile.txt", "r")
for x in f:
    print(x)
f.close()

#write() "a" - append
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f.close()

#"w" - write (overwrite the entire file)
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt", "r")
print(f.read())
f.close()

#Create a new File "x" - create
f = open("myfile.txt", "x")

#Delete a file
#os.remove("myfile.txt")
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")

#Delete a folder (only empty folder)
os.rmdir("myfolder")