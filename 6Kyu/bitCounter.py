def count_bits(num):
    return bin(num).count('1')

if __name__ == '__main__':
    print(count_bits(1234))
