# asyncio-example
Here show how to send concurrency requests via python3.5 built in asyncio.

## Update 
Add Async Poll. Can be found at AsyncPoll.py . The old version create looots of coroutines and cost looots of memorys without Async poll. 
# Usage
Require Python3.5+. Tested on Python3.7.

Create a virtual environment and install dependence. If you do not know what is virtual environment. Have a look at [https://docs.python-guide.org/dev/virtualenvs/](https://docs.python-guide.org/dev/virtualenvs/).
It is easy to learn and could help you a lot.
```bash
pip3 install requirements.txt
```
Then run the examples.
```bash
python AsyncPortScan.py 
python AsyncSpider.py
python AsyncSubDomainFuzz.py
```
# Thanks

- [http://gunhanoral.com/python/2017/07/04/async-port-check.html](http://gunhanoral.com/python/2017/07/04/async-port-check.html)    
