# coding: utf-8

import copy
from collections import OrderedDict

class Book:
    def __init__(self, name, authors, price, **rest):
        '''rest的例子有：出版商，长度，标签，出版日期'''
        self.name = name
        self.authors = authors
        self.price = price      # 单位为美元
        self.__dict__.update(rest)

    def __str__(self):
        mylist = [] # 存储属性信息
        # 使字典固定顺序
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


# 克隆类
class Prototype:

    def __init__(self):
        # 定义克隆集合,　存储需要克隆的对象
        self.objects = dict()

    # 登记要克隆的对象
    def register(self, identifier, obj):
        """
        Ａrguments:
        identifier:需要克隆对象的标识；
        obj:需要克隆的对象
        """
        self.objects[identifier] = obj



    # 在克隆集合中删除指定对象
    def unregister(self, identifier):
        del self.objects[identifier]

    # 返回克隆后的对象
    def clone(self, identifier, **attr):
        found = self.objects.get(identifier) # 根据标识获取对象
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found) # clone 对象
        obj.__dict__.update(attr)  # 更新副本的参数
        return obj


def main():
    # 创建一个原始对象
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'), price=118, publisher='Prentice Hall',
              length=228, publication_date='1978-02-22', tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99,
                         length=274, publication_date='1988-04-01', edition=2)

    # 显示克隆对象的信息
    for i in (b1, b2):
        print(i)
    print('ID b1 : {} != ID b2 : {}'.format(id(b1), id(b2)))

if __name__ == '__main__':
    main()
    
