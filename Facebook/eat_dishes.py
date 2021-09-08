from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here

  dish_set = set()
  dishes_eaten = 0

  for dish in D:
    if not dish in dish_set:
      dishes_eaten += 1
      dish_set.add(dish)
    if len(dish_set) > K: dish_set.pop()

  return dishes_eaten


N = 6
D = [1, 2, 3, 3, 2, 1]
#D = [1, 2, 1, 2, 1, 2, 1]
K = 2
print(getMaximumEatenDishCount(N, D, K))
