import asyncio
from datetime import datetime


async def task_1():
    print(f"Task 1 started at {datetime.now()}")
    await asyncio.sleep(1)
    print(f"Task 1 ended at {datetime.now()}")


async def task_2():
    print(f"Task 2 started at {datetime.now()}")
    await asyncio.sleep(1)
    print(f"task 2 ended at {datetime.now()}")


async def task_3():
    print(f"Task 3 started at {datetime.now()}")
    await asyncio.sleep(3)
    print(f"Task 3 ended at {datetime.now()}")


async def task_4():
    print(f"Task 4 started at {datetime.now()}")
    await asyncio.sleep(4)
    print(f"Task 4 ended at {datetime.now()}")


async def task_5():
    print(f"Task 5 started at {datetime.now()}")
    await asyncio.sleep(2)
    print(f"Task 5 ended at {datetime.now()}")


async def task_6():
    print(f"task 6 started at {datetime.now()}")
    await asyncio.sleep(1)
    print(f"Task 6 ended at {datetime.now()}")


async def task_7():
    print(f"Task 7 started at {datetime.now()}")
    await asyncio.sleep(3)
    print(f"task 7 ended at {datetime.now()}")


async def task_8():
    print(f"ask 8 started at {datetime.now()}")
    await asyncio.sleep(4)
    print(f"Task 8 ended at {datetime.now()}")


async def main_asyncio():
    await asyncio.gather(task_1(), task_2(), task_3(), task_4(),task_5(), task_6(), task_7(), task_8())


if __name__ == "__main__":
    start_time = datetime.now()
    print(start_time)
    asyncio.run(main_asyncio())
    end_date = datetime.now()
    print(f"{end_date}")
    print(f"Umumiy date: {end_date-start_time}")
