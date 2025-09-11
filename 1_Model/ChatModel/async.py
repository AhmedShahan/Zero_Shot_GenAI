# import time
# import asyncio 
# async def tea():
#     print("Making Tea")
#     time.sleep(3)
#     print("Deliver Tea")


# task1=tea()
# task2=tea()
# task3=tea()
# task4=tea()
# stime=time.time()
# etime=time.time()
# print(etime-stime)


import time
import asyncio

async def tea():
    print("Making Tea")
    await asyncio.sleep(3)   # Non-blocking delay
    print("Deliver Tea")

async def main():
    stime = time.time()
    
    # একসাথে সব task চালানো
    task1 = asyncio.create_task(tea())
    task2 = asyncio.create_task(tea())
    task3 = asyncio.create_task(tea())
    task4 = asyncio.create_task(tea())
    
    # সবগুলো শেষ হওয়া পর্যন্ত অপেক্ষা করা
    await task1
    await task2
    await task3
    await task4
    
    etime = time.time()
    print("Total time:", etime - stime)

asyncio.run(main())
