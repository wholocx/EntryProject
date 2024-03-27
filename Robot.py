import asyncio
import argparse

async def robotFunc(start_num):
    i = start_num
    while True:
        print(i)
        i = i + 1
        await asyncio.sleep(1)

parser = argparse.ArgumentParser(description="Введите начальное значение")
parser.add_argument("start_num", help="starting number")
args = parser.parse_args()
asyncio.run(robotFunc(args.start_num))
