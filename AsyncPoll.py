import asyncio

from AsyncSpider import fetch


class AsyncPoll:
    def __init__(self):
        self.que = asyncio.Queue()

    def run(self):
        pass

    async def spider_sem(self, async_function):
        while not self.que.empty():
            url = await self.que.get()
            response = await async_function(url)
            if response[1]:
                print(url, response[0])

    async def map(self, domains, async_function, max_process=10):
        for i in domains:
            await self.que.put(i)
        tasks = [asyncio.ensure_future(self.spider_sem(async_function)) for url in range(max_process)]
        responses = await asyncio.gather(*tasks)
        for i in range(len(domains)):
            pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    poll = AsyncPoll()
    target_urls = ['http://163.com', 'http://sdu.edu.cn', 'http://qq.com', 'http://sjtu.edu.cn', 'http://fht.im',
                   'http://no_such_xnxnxnxnxxn.com', 'http://qq.com', 'http://qq.com', 'http://qq.com', 'http://qq.com',
                   'http://qq.com']
    loop.run_until_complete(poll.map(target_urls, async_function=fetch))
