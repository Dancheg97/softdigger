import asyncio


async def waiter_function(name: str):
    for i in range(5):
        print(f"{name} on step {i}")
        await asyncio.sleep(1)


asyncio.run(waiter_function("frodo"))
asyncio.run(waiter_function("gimli"))
