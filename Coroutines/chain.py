"""
The below is true chaining, even the results. Though we're not really doing anything with them. Just printing.
"""

import asyncio
import random
import time

# The below functions are simply chaining themselves together

# COR takes int, returns str
async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result

# COR takes pargs int/str, returns str
async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    return result

# COR takes parg int, returns nada
async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")

# COR takes pargs
async def main(*args):
    """According to call, called 3 times"""
    await asyncio.gather(*(chain(n) for n in args))

# return no results, just time things
if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args)) # simply wait for all procs to finish and mark time
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
