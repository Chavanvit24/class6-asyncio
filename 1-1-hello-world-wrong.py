#when do coroutine start running
import asyncio
import time

async def print_after(massage, dalay):
    """Print a massage after the specified delay (in seconds)"""
    await asyncio.sleep(dalay)
    print(f'{time.ctime()} - {massage}')
    
    
async def main ():
    #Start coroutine twice (hopefully they start!)
    frist_awaitable = print_after('world!',2)
    second_awaitable = print_after('hello', 1)
    
    #wait for coroutine to finish
    await frist_awaitable
    await second_awaitable
asyncio.run(main())