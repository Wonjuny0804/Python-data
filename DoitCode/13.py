"""
DashInsert Function
if there are relays of odd numbers insert "-"
when even numbers "*"

"""
def DashInsert(numbers):


    while divide(numbers) == 0,__:


def divide(numbers):
    if len(numbers) == 1:
        return 0
    for i in range(1, len(numbers)):
        if int(numbers[i-1) % 2 == int(numbers[i]) % 2:
            result = numbers[:i]
            if int(numbers[i-1]) % 2 == 1: # when ti's odd number
                result += "-"
                break
            else: # when even number
                result += "*"
                break
        
    return result, numbers[i:]
haha = "4546793"
print(DashInsert(haha))

print(3%1)
print(3/1)