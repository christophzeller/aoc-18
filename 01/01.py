if __name__ == '__main__':
    with open('input.txt', 'r') as fp:
        lines = fp.readlines()
        numbers = [int(line) for line in lines]
        print(sum(numbers))
