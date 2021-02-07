"""
This little script illustrates asyncio gather and await by throttling the range: 0, 1, 2 with the makerandom calls with (10-0-1) = 9, (10-1-1) = 8, (10-2-1) = 7. Thereby making the random calls for 0--the await btw tries to get to 10 is one second; the await for 1 is 2 seconds but the threshold is lower (8), meaning it can reach 9 and finish; the await for 2 is 3 seconds but the threshold is even lower (7), meaning it can reach 8 and finish. These *could* finish at the same time-ish. Or these numbers even the odds of a 1st finisher. (and yet zero is consistently finishing last) :(

"""

import asyncio
import random

# ANSI colors
c = (
    "\033[0m",   # End of color [0]
    "\033[36m",  # Cyan         [1]
    "\033[91m",  # Red          [2]
    "\033[35m",  # Magenta      [3]
)

# args are var idx is INT, threshold is INT def to 6 and annotated
# ex: 1st call is idx: 0, threshold: 10-0-1=9
# this is my coroutine
async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10) # includes possible 10
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

# main is called to do makerandom 3 times, providing
# args 0, 10-0-1=9 (at least always <=9) / 1, 10-1-1=8, then 2
async def main():
    res = await asyncio.gather(*(makerandom(i, 10-i-1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
