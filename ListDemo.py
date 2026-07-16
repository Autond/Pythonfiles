values= [1, 2, "apple",4, 5]
print(values[0])
print(values[3])

# List is a data type that allows multipl values and can be different data types
# to print the last values
print(values[-1])
print(values[1:3])# exclusive of last digit,do -1
values.insert(3,"banana")
print(values)
values.append("END")
print(values)
values[2]="orange"# update
del values[0]