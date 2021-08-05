import random
import string

if __name__ == '__main__':
    n = int(input('how many coupons do you want to generate'))
    x = int(input('what is the total length of your coupon (without prefix length'))
    prefix = input('what is your coupon prefix')


    for i in range(n):
        coupon = prefix
        coupon += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(x))
        print(coupon)