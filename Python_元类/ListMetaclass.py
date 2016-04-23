# -*- coding: utf-8 -*-
'''
2016年04月23日14:20:59
metaclass自定义的MyList增加一个add方法
'''

# 定义ListMetaclass，默认习惯，metaclass的类名总是以Metaclass结尾
class ListMetaclass(type):
