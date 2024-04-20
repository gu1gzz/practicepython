def reversename (str):
    new_string = str.split()[::-1]
    reverse_string = []
    for i in new_string:
        reverse_string.append(i)
    reverse_string = " ".join(reverse_string)
    print(reverse_string)


    

def main():
    print("Enter a string: ")
    user_string = input()
    reversename(user_string)

if __name__ == "__main__":
    main()