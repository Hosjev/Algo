# Uses pointers O(n)
def move_zeros_to_left(A):
  if len(A) < 1:
    return

  lengthA = len(A)
  write_index = lengthA - 1
  read_index = lengthA - 1

  # Remove zeroes
  while(read_index >= 0):
    if A[read_index] != 0:
      A[write_index] = A[read_index]
      print(A)
      write_index -= 1

    read_index -= 1

  print(write_index)
  # Add them back in
  while(write_index >= 0):
    A[write_index]=0;
    write_index-=1
    
v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print("Original Array:", v)

move_zeros_to_left(v)

print("After Moving Zeroes to Left: ", v)
