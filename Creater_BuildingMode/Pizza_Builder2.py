# coding: utf-8


class Pizza:

    def __init__(self, builder):
        # builder:建造者实例
        self.garlic = builder.garlic # 大蒜
        self.extra_cheese = builder.extra_cheese # 芝士

    def __str__(self):
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes' if self.extra_cheese else 'no'
        info = ('Garlic: {}'.format(garlic), 'Extra cheese: {}'.format(cheese))
        return '\n'.join(info)

    # 建造者
    class PizzaBuilder:

        def __init__(self):
            self.extra_cheese = False
            self.garlic = False

        # 添加大蒜
        def add_garlic(self):
            self.garlic = True
            return self # 返回的是实例对象

        # 添加芝士
        def add_extra_cheese(self):
            self.extra_cheese = True
            return self# 返回的是实例对象

        # 建造
        def build(self):
            return Pizza(self) # 返回Pizza类实例

if __name__ == '__main__':
    pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()
    print(pizza)
    
