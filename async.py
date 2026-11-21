import asyncio


async def task_a():
    print('Task A is started')
    await asyncio.sleep(2)
    print('Task A is finished')


async def task_b():
    print('Task B is started')
    await asyncio.sleep(1)
    print('Task B is finished')


async def main():
    await asyncio.gather(task_a(), task_b())

asyncio.run(main())
