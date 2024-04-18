def main():
    user_string = input("Please enter a string: ")
    if user_string == user_string[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

if __name__ == "__main__":
    main()