def fl_list(list):
    num_list = []
    num_list.append(list[0])
    num_list.append(list[(len(list)-1)])
    print(num_list)

def main():
    a = [2,5, 10, 15, 20, 25, 1]
    fl_list(a)

if __name__ == "__main__":
    main()