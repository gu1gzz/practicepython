def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = list(filter(lambda x: x%2==0,a))

if __name__ == "__main__":
    main()