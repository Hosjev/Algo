
def decToBinary(num):
    if num > 1:
        # Floor divide (whole number adjusted left) then
        # hit number again on callback with modulus (remainder of division on left)
        # With binary (2), it's always 0 or 1
        decToBinary( num // 2 )
    #print(f"...following stack: {num}")
    print(num % 2, end="")


def decimalToBinary(n):
    # Use built-in function and return pretty output
    binaryStr = bin(n).replace("0b", "")
    if len(binaryStr) != 8:
        binaryStr = binaryStr.zfill(8)
    return binaryStr[0:4] + " " + binaryStr[4:8]


if __name__ == "__main__":
    # All of these convert integers to 8 bits, not 32
    decToBinary(17)
    print("")
    print(decimalToBinary(17))

    print(decimalToBinary(10))
    print(decimalToBinary(4))

    # 10 & 4: 1010/100 -0
    # 10 | 4: 1010/100 -14
    # 10 ^ 4: 1010/100 -14
    # Four should have preceding zero
    if 10 & 4:
        print("Passed bitwise AND")
    if 10 | 4:
        print("Passed bitwise OR")

    print(20 >> 1) # shift bits for 20 once to right (decrease)
    print(20 >> 2)
    print(20 >> 3)
    print(20 >> 4)
    print(20 >> 5)
    print(20 << 1) # shift bits once to left (increase)
    print(20 << 2)
    print(1 << 20)

    print("\nStarting count from 0:\n")
    for x in range(130):
        if len(str(x)) == 1:
            print(f"Bit string for {x} is: {decimalToBinary(x):>20}")
        else:
            print(f"Bit string for {x} is: {decimalToBinary(x):>19}")
    print("\n")
