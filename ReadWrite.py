file = open('test.txt')
# Read all contents of a file

#print(file.read(5)) # reads the byte from the file ,nect line is treated as 1 space

#print(file.readline()) #read 1 line
#print(file.readline())
#file.close()


# print all the contents of the file line by line using readline method

#line=file.readline()

#while line!="":
 #   print(line)
  #  line = file.readline()
#file.close()

#another way to readline

for line in file.readlines(): #stores it in the list format
    print(line)

file.close()