# -*- coding: utf-8 -*-
"""
时间：2016年04月23日14:38:55
ORM==>Obiect Relational Mapping （对象-关系映射）
就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表。
这样，写代码就更简单，不用直接操作SQL语句。
需要写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
"""

# 首先定义Field类，它负者保存数据库表的字段名和字段类型：
class Field(object):

	def __init__(self, name, coulume_type): # coulume 列
		self.name = name
		self.coulume_type = coulume_type

	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__, self.name)

# 在Field的基础上，进一步定义各种类型的Field，如StringField，IntegerField等等：
class StringField(Field):

	def __init__(self, name): # super调用父类的方法初始化
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

# 之后就是较为复杂的ModelMetaclass：
class ModelMetaclass(type):

	def __new__(cls, name, bases, attrs):
		if name=="Model":
			return type.__new__(cls, name, bases, attrs)
		print('Found model: %s' % name)
		mappings = dict() # 创建一个字典
		for k, v in attrs.items():
			if isinstance(v, Field): # 判断对象类型
			    print('Found mapping: %s ==> %s' % (k, v)) # 字典对应
			    mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		attrs['__table__'] = name # 假设表名和类名一致
		return type.__new__(cls, name, bases, attrs)

# 最后是基类Model
class Model(dict, metaclass=ModelMetaclass):

	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute `%s`" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def sava(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))


# testing code:
class User(Model):
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')

u = User(id='11', name='Mick', email="test@163.com", password='password')
u.sava()




