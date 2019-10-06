# coding: utf-8

#电脑
class Computer:

    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None      # 单位为GB
        self.hdd = None         # 单位为GB
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)

# 建造者
class ComputerBuilder:

    def __init__(self):
        self.computer = Computer('AG23385193') # 设置序列号

    #　配置内存
    def configure_memory(self, amount):
        self.computer.memory = amount

    # 配置hdd
    def configure_hdd(self, amount):
        self.computer.hdd = amount

    # 配置gpu
    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model

# 指挥者
class HardwareEngineer:

    def __init__(self):
        self.builder = None

    # 在建造的时候，才创建建造者对象
    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]
    @property
    def computer(self):
        return self.builder.computer


def main():
    # 申请一个指挥者
    engineer = HardwareEngineer()
    # 指挥者配置电脑
    engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
    # 返回实例对象
    computer = engineer.computer #得到一个电脑实例
    print(computer)

if __name__ == '__main__':
    main()
    
