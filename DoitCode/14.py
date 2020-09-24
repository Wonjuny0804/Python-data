"""
문자열 압축하기

Input : aaabbccccca
Output : a3b2c6a1
"""
def supress(lists):
    length = []
    result = ""

    if len(lists) == 1:
        return 1
    
    for cut in range(1, len(lists) // 2 + 1):
        count = 1 
        tempStr = lists[:cut]
        for i in range(cut, len(lists), cut):
            if lists[i:i+cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = lists[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(lists))
        result = ""

    return min(length)

print(supress("aaabbbccccc"))