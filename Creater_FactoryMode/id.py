#!/bin/env/bash

class A(object):
    pass

if __name__ == '__main__':
    a = A()
    b = A()

    print(id(a) == id(b)) # a,b是不同的实例
    print(a, b)
    
