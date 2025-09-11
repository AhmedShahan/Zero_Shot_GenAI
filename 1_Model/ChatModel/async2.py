import asyncio
import time

async def tea():
    print("Making Tea")
    await asyncio.sleep(5)
    print("Deliver Tea")

async def coffee():
    print("Making Coffee")
    await asyncio.sleep(10)
    print("Deliver Coffee")

async def main():
    st = time.time()

    # তিনটা কাজ একসাথে শুরু
    tasks = [
        asyncio.create_task(tea()),
        asyncio.create_task(coffee()),
        asyncio.create_task(tea())
    ]

    # কে আগে শেষ হবে, সেটা ডাইনামিক ভাবে ধরতে চাই
    for finished in asyncio.as_completed(tasks):
        await finished  # যতক্ষণ না একেকটা task শেষ হয়
        print(f"Task finished at {time.time()-st:.2f} seconds")

    et = time.time()
    print("Total time:", et - st)

asyncio.run(main())
