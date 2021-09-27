def divide(dividend, divisor):
    """
    Function to divide using bitwise operators

    ...

    Parameters
    ----------
    dividend : int
        the integer used to divide into
    divisor  : int
        the integer used to divide with

    Returns
    -------
    quotient (without fractions)
    """
    MIN_INT = pow(-2, 31)
    MAX_INT = pow(2, 31) - 1
    negative = neg_pos(dividend, divisor)
    dividend, divisor = abs(dividend), abs(divisor)

    # Max/Min 32bit
    if divisor == 1:
        if negative:
            return -dividend if MIN_INT < -dividend else MIN_INT
        else:
            return dividend if MAX_INT > dividend else MAX_INT

    # Edge cases
    if dividend < divisor:
        num = 0
    elif dividend == divisor:
        num = 1
    else:
        num = binary_helper(abs(dividend), abs(divisor))

    return num if not negative else -num


def binary_helper(dividend, divisor):
    Q = 1
    CD = divisor

    # Our Return
    if dividend < divisor:
        return 0
    elif dividend == divisor:
        return 1

    while CD < dividend:
        Q = Q << 1
        CD = CD << 1

    # Account for misstep
    CD = CD >> 1
    Q = Q >> 1

    # The magic
    return Q + binary_helper((dividend - CD), divisor)


def neg_pos(dividend, divisor):
    # Both neg or pos == pos
    # One neg == neg Yikes
    dv = dividend > 0
    dr = divisor > 0
    if dv and dr:
        return False
    if not dv and not dr:
        return False

    return True


def divide_helper(dividend, divisor, count):
    # SLOW and RT heavy with large dividends
    if dividend < divisor:
        return count
    return divide_helper((dividend - divisor), divisor, count + 1)


#print(divide(10, 3)) # 3
print(divide(-10, 3)) # -3
print(divide(0, 1)) # 0
print(divide(7, -3)) # -2
print(divide(1, 1)) # 1
print(divide(-1, -1)) # 1
print(divide(-1, 1)) # -1
dv = -2147483648
dr = -1 # -1
dv = -2147483648
dr = 1 # 
print(divide(dv, dr))
# Do this with binary
# 5 >> 1 == 5 // 2
