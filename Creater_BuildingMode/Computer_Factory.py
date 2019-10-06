# coding: utf-8

MINI14 = '1.4GHz Mac mini'

# 工厂模式产生类实例
class AppleFactory:

    # 防止实例化
    class MacMini14: 

        def __init__(self):
            self.memory = 4  # 单位为GB
            self.hdd = 500  # 单位为GB
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = ('Model: {}'.format(MINI14),
                    'Memory: {}GB'.format(self.memory),
                    'Hard Disk: {}GB'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gpu))
            return '\n'.join(info)

    # 工厂函数
    def build_computer(self, model):
        if (model == MINI14):
            return self.MacMini14()
        else:
            print("I dont't know how to build {}".format(model))

if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)
