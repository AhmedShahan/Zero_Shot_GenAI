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
        (asyncio.create_task(tea()), "Tea Task"),
        (asyncio.create_task(coffee()), "Coffee Task"),
        (asyncio.create_task(tea()), "Tea Task 2")
    ]

    # কে আগে শেষ হবে, সেটা ডাইনামিক ভাবে ধরতে চাই
    for finished in asyncio.as_completed([task for task, name in tasks]):
        result = await finished  # যতক্ষণ না একেকটা task শেষ হয়
        # Find which task finished
        for task, name in tasks:
            if task.done() and not hasattr(task, '_printed'):
                task._printed = True
                print(f"Task {name} finished at {time.time()-st:.2f} seconds")
                break

    et = time.time()
    print("Total time:", et - st)

asyncio.run(main())