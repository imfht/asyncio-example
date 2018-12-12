import asyncio

import aiohttp

from Util import get_logger, get_title, auto_decode

logger = get_logger("spider")


async def fetch(url):
    """
    fetch a url and return result
    if no Exceptions occurred, will return (html title, True).
    if any Exceptions occurred ,will return (error msg, False)
    :param url: a url
    :return: title, status
    """
    logger.debug("start fetch %s" % url)
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, ssl=False) as response:
                body = await response.content.read(-1)
                return get_title(auto_decode(body)), True
        except Exception as e:
            error_msg = e.__class__.__name__
            logger.warn("%s - %s" % (url, error_msg))
            return error_msg, False


async def spider_sem(sem, url):
    async with sem:
        return await fetch(url)


async def run(urls, loop):
    sem = asyncio.Semaphore(5)  # Change this value for limitation
    tasks = [asyncio.ensure_future(spider_sem(sem, url)) for url in urls]
    responses = await asyncio.gather(*tasks)
    for i in range(len(urls)):
        if responses[i][1]:  # if success, print...
            logger.info("URL: %s, TITLE: %s" % (urls[i], responses[i][0]))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    target_urls = ['http://163.com', 'http://sdu.edu.cn', 'http://qq.com', 'http://sjtu.edu.cn', 'http;//fht.im',
                   'http://no_such_xnxnxnxnxxn.com']
    loop.run_until_complete(run(target_urls, loop))
