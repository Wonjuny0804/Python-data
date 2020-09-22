"""
DashInsert Function
if there are relays of odd numbers insert "-"
when even numbers "*"

"""
def DashInsert(numbers):

    lst = numbers

    for now in range(1,len(numbers)):
        if int(numbers[now]) % 2 == int(numbers[now-1]) % 2:
            if int(numbers[now]) % 2 == 1:
                lst = lst[:now] + "-" + lst[now:]
            else:
                lst = lst[:now] + "*" + lst[now:]
        numbers = lst
    return lst

haha = "4546793"
print(DashInsert(haha))

print(3%1)
print(3/1)