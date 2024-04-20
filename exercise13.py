def main():
    print("How many fibonnaci numbers you want ? ")
    lenght = int(input())
    first = 0
    second = 1
    while lenght > 0:
        print(first + second)
        update = second
        second = first + second
        first = update
        lenght -=1

if __name__ == "__main__":
    main()