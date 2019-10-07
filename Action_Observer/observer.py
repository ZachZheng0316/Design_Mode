#!/bin/bash

# 发布者
class Publisher(object):
    def __init__(self):
        self.observers = [] # 观察者列表

    # 添加观察者
    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    # 移除观察者
    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    # 通知观察者
    def notify(self):
        # 逐个通知观察者数据发生变化
        [observer.subscribe(self) for observer in self.observers]

# 改进的发布者
class DefaultFormatter(Publisher):

    def __init__(self, name):
        """
        Params:
            - name: 指定类实例名称
        """
        super().__init__()
        self.name = name    # 设置实例名称，方便跟踪其状态
        self._data = 0      # 设置私有变量

    def __str__(self):
        """
        Func:
            使用 printf(类实例)会调用此函数
        """
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        """
        Func:
            发生赋值操作时会调用此函数，例如：
            dfTest = DefaultFormatter("dfTest")
            dfTest.data = 3 # 等效 dfTest.data(new_value = 3)
        """
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()

# 十六进制观察者
class HexFormatter:
    def __init__(self):
        self._data = hex(0)

    def subscribe(self, publisher):
        """
        Params:
            - publisher: 指向实例对象的指针
        """
        self._data = hex(publisher._data)
        print("{}: '{}' has now hex data = {}".format(type(self).__name__, publisher.name, self._data))

# 二进制观察者
class BinaryFormatter:
    def __init__(self):
        self._data = bin(0)

    def subscribe(self, publisher):
        """
        Params:
            - publisher: 指向实例对象的指针
        """
        self._data = bin(publisher._data)
        print("{}: '{}' has now bin data = {}".format(type(self).__name__, publisher.name, self._data))

def main():
    # 申请一个发布者
    PublisherTest = DefaultFormatter('PublisherTest')
    print(PublisherTest)

    print()
    print("添加十六进制格式订阅者")
    hf = HexFormatter() # 申请一个订阅者
    PublisherTest.add(hf) # 向发布者添加订阅者
    PublisherTest.data = 3 # 等效为PublisherTest.data(new_value = 3)
    print(PublisherTest)

    print()
    print("添加二进制格式订阅者")
    bf = BinaryFormatter() # 申请一个订阅者
    PublisherTest.add(bf) # 在发布者中添加订阅者
    PublisherTest.data = 21 # 等效为PublisherTest.data(new_value = 21)
    print(PublisherTest) # 打印发布者信息

    print()
    print("移除十六进制格式订阅者")
    PublisherTest.remove(hf) # 移除一个订阅者
    PublisherTest.data = 40 # 等效为PublisherTest.data(new_value = 40)
    print(PublisherTest) # 打印发布者的信息

    print()
    print("移除十六进制格式订阅者、添加二进制格式订阅者")
    PublisherTest.remove(hf) # 移除一个订阅者
    PublisherTest.add(bf) # 添加一个订阅者
    PublisherTest.data = 'hello' # 等效为PublisherTest.data(new_value = 'hello')
    print(PublisherTest) # 打印订阅者信息

    print()
    PublisherTest.data = 15.8 # 等效为PublisherTest.data(new_value = 15.8)
    print(PublisherTest) # 打印订阅者信息

if __name__ == '__main__':
    main()
