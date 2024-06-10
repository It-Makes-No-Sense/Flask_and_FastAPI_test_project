import asyncio


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def prinf_letters():
    for letter in ('a', 'b', 'c', 'd', 'e', 'f'):
        print(letter)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(prinf_letters())
    await task1
    await task2


asyncio.run(main())
