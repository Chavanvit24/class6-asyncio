import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified delay (in second)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")   


async def main():
    # Use asyncio.gather to run two coroutines concurrently:
    await asyncio.gather(
        print_after("World!", 2),
        print_after("Hello", 1)
    ) 

asyncio.run(main())

#Wed Aug  9 13:15:47 2023 - Hello
#Wed Aug  9 13:15:48 2023 - World!