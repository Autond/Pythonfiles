# instead of writing file= open('test.txt') and file.close()

#prefer with open(test.txt') as file:

# read the file and store all the lines in a list
# reverse the list
# write the list back to file
with open('test.txt','r') as reader:# file opened in read mode
    content= reader.readlines()
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)






