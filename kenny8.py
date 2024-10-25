def find_perfect_num(limit):
    print(f'The perfect numbers below {limit} are:')
    for num in range(2,limit):
        divisors_sum=0
        for i in range(1,num):
            if num % i ==0:
                divisors_sum +=i
        if divisors_sum==num:
            print(num)

user_limit = int(input("Enter your number's limit: "))
find_perfect_num(user_limit)
