def main():
    list_of_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    new_list = []
    for number in list_of_numbers:
        if number < 5:
            new_list.append(number)
    print(new_list)
    new_list = []
    user_number = int(input("Please enter a number: "))
    for number in list_of_numbers:
        if number < user_number:
            new_list.append(number)
    print(new_list)
    
if __name__ == "__main__":
    main()