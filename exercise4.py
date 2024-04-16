def main():
    user_number = int(input("Please enter a number: "))
    list_divisor = []
    list_range = list(range(1,user_number+1))
    for number in list_range:
        if user_number % number == 0:
            list_divisor.append(number)
    print(list_divisor)
if __name__ == "__main__":
    main()