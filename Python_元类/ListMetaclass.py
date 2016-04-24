# -*- coding: utf-8 -*-
'''
2016年04月23日14:20:59
metaclass自定义的MyList增加一个add方法
'''

# 定义ListMetaclass，默认习惯，metaclass的类名总是以Metaclass结尾
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

 # 有了ListMetaclass，定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass

 class MyList(list, metaclass=ListMetaclass):
 	pass

 '''
说明：当类传入关键字参数metaclass时，Python解释器在创建MyList时，要通过
ListMetaclass.__new__() 来创建。

__new__()方法接收到的参数依次是：
当前准备创建的类的对象；
类的名字；
类继承的父类集合；
类的方法集合。

 '''
