"""The order of this output is the heart of async IO. Talking to each of the calls to count() is a single event loop, or coordinator. When each task reaches await asyncio.sleep(1), the function yells up to the event loop and gives control back to it, saying, “I’m going to be sleeping for 1 second. Go ahead and let something else meaningful be done in the meantime.

Before
Before
Before
After
After
After
coroutines/counter.py executed in 1.00

Instead of how a truly synchronous code block executes: do something--sleep for 1 second and block, etc.
"""

import asyncio
import time

async def count(cs: int):
    print("Before")
    await asyncio.sleep(cs)
    print("After")

async def main():
    await asyncio.gather(*(count(i) for i in range(1,4)))

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:.2f}")
