import asyncio
import socket

import aiodns


async def check_domain(domain, loop):
    resolver = aiodns.DNSResolver(loop=loop)
    try:
        result = await resolver.gethostbyname(domain, socket.AF_INET)
        print(domain, result.name, result.addresses)
    except:
        return
    return result


async def check_domain_sem(sem, domain, loop):
    async with sem:
        return await check_domain(domain, loop)


async def task_manager(domains, loop):
    sem = asyncio.Semaphore(1000)  # Change this value for limitation
    sub_domains = []
    for sub in open('./txt/subdomains-top1mil-20000.txt').readlines():
        for domain in domains:
            sub_domains.append('%s.%s' % (sub[:-1], domain))
    tasks = [asyncio.ensure_future(check_domain_sem(sem, sub_domain, loop)) for sub_domain in sub_domains]
    responses = await asyncio.gather(*tasks)
    for i in responses:
        if i:
            print(i)


if __name__ == '__main__':
    domains = ['qq.com', 'baidu.com']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task_manager(domains, loop))
