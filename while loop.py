#when you  have to run the condition untill it becomes false
it=4

while (it>1):
    if it!=3:
        print(it)
    it=it-1

print("while loop ended")
print("*************break keyword->breaks the execution*************************")

bt=5

while bt>1:
    if bt==3:
        break

    print(bt)
    bt=bt-1
print("*******continue-> stops that iteration only*******************************************")

ct=10
while ct>1:
    if ct==9:
        ct=ct-1
        continue
    if ct==3:
        break
    print(ct)
    ct=ct-1




