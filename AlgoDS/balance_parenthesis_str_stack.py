from stack import Stack

def balance_par_str_with_stack(str1):
    s = Stack()
    balanced = True
    index = 0

    while index < len(str1) and balanced:
        symbol = str1[index]

        if symbol == "(":
            s.push(symbol)
        else:
            s.pop()

        
    if balanced and s.isEmpty():
        return True
    else:
        return False

if __name__=="__main__":
    print(balance_par_str_with_stack('((()))'))
    print(balance_par_str_with_stack('(()'))
        