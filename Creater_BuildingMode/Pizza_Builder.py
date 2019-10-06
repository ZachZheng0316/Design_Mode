# coding: utf-8

from enum import Enum
import time

# Ｐizza的过程: [队列,预备,烘焙,准备]
PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
# Pizza的面团: [薄、厚]
PizzaDough = Enum('PizzaDough', 'thin thick')
# Pizza的配料：[番茄、奶油]
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
# Pizza的装饰:[玛格丽特、双层玛格丽特、培根、火腿、蘑菇、红皮洋葱、牛油果]
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')

STEP_DELAY = 3          # 考虑是示例，单位为秒

# 产品是Pizza
class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None   # 生面团
        self.sauce = None   # 配料
        self.topping = []   # 在糕点上装饰配料

    def __str__(self):
        return self.name

    # 模拟生面团制作过程: 输入面团的名称，并把面团制作好
    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))

# 两个建造者类的接口函数都是相同的
# 玛格丽特比萨建造者
class MargaritaBuilder:

    def __init__(self):
        self.pizza = Pizza('margarita') # 建造玛格丽特Pizza
        self.progress = PizzaProgress.queued # 记录制作的步骤
        self.baking_time = 5 # 烘焙时间

    # 准备面团
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    # 准备配料
    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    # 添加配料的过程
    def add_topping(self):
        print('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.append([i for i in
                                   (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarrella, oregano)')

    # 烘焙的过程
    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')

# 奶油披萨建造者
class CreamyBaconBuilder:

    def __init__(self):
        self.pizza = Pizza('creamy bacon') # 奶油熏肉披萨
        self.progress = PizzaProgress.queued
        self.baking_time = 7 # 烘焙时间

    # 准备面团的过程
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    # 准备配料过程
    def add_sauce(self):
        print('adding the crème fraîche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the crème fraîche sauce')

    # 添加配料过程
    def add_topping(self):
        print('adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon')
        self.pizza.topping.append([t for t in
                                   (PizzaTopping.mozzarella, PizzaTopping.bacon,
                                    PizzaTopping.ham, PizzaTopping.mushrooms,
                                    PizzaTopping.red_onion, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano)')

    # 烘焙过程
    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')

# 指挥者：服务员
class Waiter:

    def __init__(self):
        self.builder = None

    # 构建比萨
    def construct_pizza(self, builder):
        # builder是建造者实例
        self.builder = builder # 在建造的时候创建builder对象
        [step() for step in (builder.prepare_dough,
                             builder.add_sauce, builder.add_topping, builder.bake)]
    # 打印比萨的信息
    @property
    def pizza(self):
        return self.builder.pizza

# 确保用户的输入是有效的
def validate_style(builders):
    """
    builders:建造者类字典
    """
    try:
        pizza_style = input('What pizza would you like, [m]argarita or [c]reamy bacon? ')
        # 选择建造者类，创建建造者实例
        builder = builders[pizza_style]()
        # valid_input = True
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return (False, None)
    return (True, builder)


def main():
    # 建造者类字典
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)

    # 选择建造者类，并创建建造者实例
    valid_input = False
    while not valid_input:
        # 根据用户选择，创建建造者实例
        valid_input, builder = validate_style(builders)
    print()

    waiter = Waiter() # 指挥者类实例
    waiter.construct_pizza(builder) # 建造Pizza
    pizza = waiter.pizza
    print()
    print('Enjoy your {}!'.format(pizza))

if __name__ == '__main__':
    main()
    
