import asyncio
import time
async def tea():
    print("Making Tea")
    await asyncio.sleep(3)
    print("Deliver Tea")


async def coffee():
    print("Making Coffee")
    await asyncio.sleep(5)
    print("Deliver Coffee")

async def main():
    stime=time.time()

    task1=asyncio.create_task(tea())
    task2=asyncio.create_task(tea())
    task3=asyncio.create_task(coffee())


    await task3
    await task1
    await task2


    etime=time.time()
    print("Total Time: ",etime-stime)


asyncio.run(main())
