"""
DashInsert Function
if there are relays of odd numbers insert "-"
when even numbers "*"

"""
def DashInsert(numbers):

    end = numbers

    for i in range(0, len(end)-1):
        if int(end[i]) % 2 == int(end[i+1]) % 2:
            front = end[:i+1]
            if int(end[i]) % 2 == 1:
                front = front + "-"
            else:
                front = front + "*"
            end = end[i+1:]
haha = "4546793"
print(DashInsert(haha))

print(3%1)
print(3/1)