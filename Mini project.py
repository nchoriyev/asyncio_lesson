import asyncio
from datetime import datetime

async def worker(name, sekund):
    """
    Bu loyihada ishlchilarning sekundga qarab chiqishini ko'rishimiz mumkin
    :param name:
    :param sekund:
    :return:
    """
    print(f'{name}jon ishini boshlayabdi... {datetime.now()}')
    await asyncio.sleep(sekund)
    print(f'{name}jon ishini tugatdi. {datetime.now()}')


async def main():
    workers = [
        {"name": "Nodirbek", "sekund": 2},
        {"name": "Oqil", "sekund": 1},
        {"name": "bobomurod", "sekund": 3}
    ]

    await asyncio.gather(*(worker(worker_info['name'], worker_info['sekund']) for worker_info in workers))


if __name__ == "__main__":
    asyncio.run(main())
