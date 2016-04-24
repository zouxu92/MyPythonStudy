# -*-coding:utf-8 -*-
# 时间：2016年04月24日13:53:15
# 用Task封装两个coroutine

import threading
import asyncio

@asyncio.coroutine
def hello():
	print('Hello world(%s)' % threading.currentThread())
	yield from asyncio.sleep(1)
	print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



