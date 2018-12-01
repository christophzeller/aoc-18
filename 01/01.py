if __name__ == '__main__':
    with open('input.txt', 'r') as fp:
        lines = fp.readlines()
        numbers = [int(line) for line in lines]
        print(sum(numbers))

        frequencies = set([0])
        current_frequency = 0
        found_duplicate = False
        while not found_duplicate:
            for n in numbers:
                current_frequency += n
                if current_frequency in frequencies:
                    found_duplicate = True
                    print(current_frequency)
                    break
                frequencies.add(current_frequency)
