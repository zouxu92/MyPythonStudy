# -*- coding:utf-8 -*-
# python对协程的支持是通过generator实现的
'''
2016年04月24日10:29:05
在generator中我们可以使用for循环来迭代，不断调用next()获取yield语句返回的下一个值
但Python的yield不但可返回一个值，它还可以接受调用者发出的参数。
'''

# 生产者与消费者的例子

def consumer(): # 消费者 
	r = ''
	while True:
		n = yield r      # 第一次接受send(None) 直接返回
		print('test')
		if not n:
			return
		print('[CONSUMER(消费者)] Consuming %s ...' % n)
		r = '200 OK'

def produce(c): # 生产者
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCE(生产者)] Producing %s...' % n)
		r = c.send(n)
		print('[PRODUCE] Consumer return: %s' % r)
	c.close()


c = consumer()
produce(c)
'''
注意到consumer函数是一个generator，把一个consumer传入produce后：
1.首先调用c.send(None)启动生成器；
2.然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
3.consumer通过yield拿到消息，处理，又通过yield把结果传回；
4.produce拿到consumer处理的结果，继续生产下一条消息；
5.produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
执行结果：
[PRODUCE(生产者)] Producing 1...
test
[CONSUMER(消费者)] Consuming 1 ...
[PRODUCE] Consumer return: 200 OK
[PRODUCE(生产者)] Producing 2...
test
[CONSUMER(消费者)] Consuming 2 ...
[PRODUCE] Consumer return: 200 OK
[PRODUCE(生产者)] Producing 3...
test
[CONSUMER(消费者)] Consuming 3 ...
[PRODUCE] Consumer return: 200 OK
[PRODUCE(生产者)] Producing 4...
test
[CONSUMER(消费者)] Consuming 4 ...
[PRODUCE] Consumer return: 200 OK
[PRODUCE(生产者)] Producing 5...
test
[CONSUMER(消费者)] Consuming 5 ...
[PRODUCE] Consumer return: 200 OK


'''



