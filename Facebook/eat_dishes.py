from typing import List
# Write any import statements here

class Kaitzen:
    def getMaximumEatenDishCount(self, N: int, D: List[int], K: int) -> int:
        from queue import Queue
        # Use FIFO queue
        variety = Queue(maxsize=K)
        dishes = int()

        for i in D:
            if i not in variety.__dict__["queue"]:
                if variety.full():
                    variety.get() # Trash it
                variety.put(i)
                dishes += 1
        return dishes


if __name__ == "__main__":
    N = 6
    D = [1, 2, 3, 3, 2, 1]
    D = [1, 2, 1, 2, 1, 2, 1]
    K = 1
    print(Kaitzen().getMaximumEatenDishCount(N, D, K))
