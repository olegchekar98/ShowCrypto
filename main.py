from settings import crypto_dict
import asyncio


async def main():
    while True:
        crypto_dict['bitcoin'].printing()
        crypto_dict['ethereum'].printing()
        crypto_dict['ripple'].printing()
        await asyncio.sleep(300)


task = asyncio.Task(main())
loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass

