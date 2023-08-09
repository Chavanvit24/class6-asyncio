import asyncio
import time

async def example(message):
    print(f"{time.ctime()} - start of :", message)
    await asyncio.sleep(1)
    print(f"{time.ctime()} - end of :", message)

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = example("First call")
    second_awaitable = example("Second all")
    # Wait for corountines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())

#Wed Aug  9 13:08:37 2023 - start of : First call
#Wed Aug  9 13:08:38 2023 - end of : First call
#Wed Aug  9 13:08:38 2023 - start of : Second all
#Wed Aug  9 13:08:39 2023 - end of : Second all