def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0 :
            is_prime = False
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


n = int(input("What is your number? "))
prime_checker(n)
