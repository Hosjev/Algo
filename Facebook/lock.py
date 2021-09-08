from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  
  current = 1
  winning_time = int()
  for destination in C:
    # current - dest = forward; N-dest + current = reverse
    temp = min(abs(current-destination), N-destination+current)
    winning_time += temp
    current = destination 

  return winning_time


if __name__ == "__main__":
    N = 3
    M = 3
    C = [1, 2, 3]

    print(getMinCodeEntryTime(N, M, C))
