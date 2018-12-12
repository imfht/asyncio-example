# This is from http://gunhanoral.com/python/2017/07/04/async-port-check.html
import asyncio


async def check_port(ip, port, loop):
    conn = asyncio.open_connection(ip, port, loop=loop)
    try:
        reader, writer = await asyncio.wait_for(conn, timeout=3)
        return ip, port, True
    except:
        return ip, port, False


async def check_port_sem(sem, ip, port, loop):
    async with sem:
        return await check_port(ip, port, loop)


async def run(dests, ports, loop):
    sem = asyncio.Semaphore(1000)  # Change this value for limitation
    tasks = [asyncio.ensure_future(check_port_sem(sem, d, p, loop)) for d in dests for p in ports]
    responses = await asyncio.gather(*tasks)
    for i in responses:
        if i[2]:
            print('open', i[0], i[1])
    return responses


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(['123.125.115.110'], range(1, 1000), loop))
    loop.close()
