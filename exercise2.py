def main():
    number = int(input("Please, enter a number: "))
    if (number%4) == 0:
        print("Your number is a multiple of 4")
    elif (number%2) == 0:
        print("Your number is an even")
    else:
        print("Your number is an odd")

    number = int(input("Please enter an other number: "))
    div = int(input("Please enter a number that you want for divide: "))

    if (number % div) == 0:
        print(f"{number} can be divided evenly by {div}")
    else:
        print(f"{number} can't be divided evenly by {div}")


if __name__ == "__main__":
    main()