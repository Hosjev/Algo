def is_palindrome(num: int):
    # Immediately deal with edge case
    if len(str(num)) <= 1:
        return True

    pointer_left = 0
    pointer_right = len(str(num)) - 1

    while not pointer_left >= pointer_right:
        if str(num)[pointer_left] != str(num)[pointer_right]:
            return False
        else:
            # Advance pointers
            pointer_left += 1
            pointer_right -= 1


    # Finally, return true
    return True


print(is_palindrome(121212121212121))
print(is_palindrome(21212121212121))
print(is_palindrome(2))
