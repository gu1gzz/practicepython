def test_prime(num):
    sqr = int(num**0.5)
    for i in range(2,(sqr+1)):
        if num%i == 0:
            print("This number is not prime")
            return
    print("This number is a prime")


def main():
    user_input = int(input("Please enter a number: "))
    test_prime(user_input)

if __name__ == "__main__":
    main()