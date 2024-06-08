import asyncio
from datetime import datetime


async def task_1():
    """
    Bunda vaqtdan tashqari shartning tugallanganligiga ham bog'liq
    :return:
    """
    print(f"Task 1 started at {datetime.now()}")
    await asyncio.sleep(1)
    print(f"Task 1 ended at {datetime.now()}")
    await task_4()
    print(f"task 1 completed")


async def task_2():
    print(f"Task 2 started at {datetime.now()}")
    await asyncio.sleep(5)
    print(f"task 2 ended at {datetime.now()}")
    print(f"task 2 completed")


async def task_3():
    print(f"Task 3 started at {datetime.now()}")
    await asyncio.sleep(3)
    print(f"Task 3 ended at {datetime.now()}")
    await task_2()
    print(f"task 3 completed")


async def task_4():
    print(f"Task 4 started at {datetime.now()}")
    await asyncio.sleep(2)
    print(f"Task 4 ended at {datetime.now()}")
    await task_3()
    print(f"task 4 completed")


async def main_asyncio():
    await asyncio.gather(task_1(), task_2(), task_3(), task_4())


if __name__ == "__main__":
    start_time = datetime.now()
    print(start_time)
    asyncio.run(main_asyncio())
    end_date = datetime.now()
    print(f"{end_date}")
    print(f"Umumiy date: {end_date - start_time}")
