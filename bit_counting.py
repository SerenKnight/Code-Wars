def count_bits(n):
    binary = bin(n)
    count = 0
    for i in binary:
        if i == "1":
            count += 1
    print(count)
    #print(bin(n).count("1"))
count_bits(12345)