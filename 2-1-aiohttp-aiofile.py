# pip install aiofiles==0.7.0
# pip install aiohttp==3.7.4.post0

import sys
import asyncio
import time

import aiohttp
import aiofiles


async def write_genre(file_name):
    """
    Uses genrenator from binaryjazz.us to write a random genre to the
    name of the given file
    """
    async with aiohttp.ClientSession() as session:
        async with session.get("http://binaryjazz.us/wp-json/genrenator/v1/genre") as respone:
            genre = await respone.json()
    async with aiofiles.open(file_name, "w") as new_file:
        print(f"{time.ctime()} Writing '{genre}' to '{file_name}'...")
        await new_file.write(genre)


async def main():
    task = []

    print(f"{time.ctime} - Starting...")
    start = time.time()
    for i in range(5):
        task.append(write_genre(f"./asyncout/new_file{i}.txt"))

    await asyncio.gather(*task)
    end = time.time()
    print(f"Time to complete asynio read/write:{round(end-start),2} second")


if __name__ == "__main__":
    # On Windows, this finishes successfully, but throws 'RuntimeError: Event loop is closed'
    # The following lines fix this
    # Source: https://github.com/encode/httpx/issues/914#issuecomment-622586610
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())