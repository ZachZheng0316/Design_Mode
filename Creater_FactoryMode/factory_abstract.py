# 青蛙
class Frog(object):
    def __init__(self, name):
        ```
        Params：
            name: 青蛙的名称
        ```
        self.name = name

    def __str__(self):
        return self.name

    # 青蛙与障碍物之间的交互
    def interact_with(self, obstacle):
        ```
        Params:
            obstacle: 虫子实例对象
        ```
        print('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))

#虫子
class Bug(object):
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'

# 巫师
class Wizard(object):
    def __init__(self, name):
        ```
        Params：
            name: 巫师的名字
        ```
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        ```
        Params:
            obstacle: 怪兽实例对象
        ```
        print("{} the Wizard battles against {} and {}!".format(self, obstacle, obstacle.action()))

# 怪兽
class Ork(object):
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'

# 抽象工厂: 青蛙世界/动物世界
class AbstractFactory(object):
    def __init__(self, game_mode):
        # 游戏模式:根据游戏模式的不同，产生不同的种类的角色
        ```
        Params:
            game_mode: 游戏模式,可选值为`frog`、`wizard`
        ```
        self.game_mode = game_mode;

    def __str__(self):
        return '\n\n\t-------' + self.game_mode + 'Frog World ------'

    # 正面角色工厂
    def make_character(self, hore_name):
        ```
        Params:
            hore_name: 正面角色的名字
        ```
        if 'frog' == self.game_mode:
            return Frog(hore_name)
        elif 'wizard':
            return Wizard(hore_name)
        else:
            raise ValueError("Cannot create character {}".format(hore_name))

    # 负面角色工厂
    def make_obstacle(self):
        if 'frog' == self.game_mode:
            return Bug()
        elif 'wizard' == self.game_mode:
            return Ork()
        else:
            raise ValueError("Cannot create obstacle {}")

# 游戏入口
class GameEnvironment:
    def __init__(self, absfactory, name):
        ```
        Params:
            absfactory: 抽象工厂类实例；
            name: 正面角色的名称；
        ```
        self.hero = absfactory.make_character(name) # 正面角色实例
        self.obstacle = absfactory.make_obstacle()  # 反面角色实例

    # 游戏的交互
    def play(self):
        self.hero.interact_with(self.obstacle)

# 提示用户返回一个有效的年龄
def validate_age(name):
    try:
        age = input("Welcome {}. How old are you? ".format(name))
        age = int(age)
    except ValueError as err:
        print("Age {} is invalid, Please try again...".format(age))
        return (False, age)
    return (True, age)

def main():
    name = input("Hello, What's your name? ")

    # 直到输入有效的年龄
    valid_input = False;
    while not valid_input:
        valid_input, age = validate_age(name)

    # 根据年龄选择游戏模式
    game_mode = "frog" if age < 12 else "wizard"

    # 启动游戏
    absfactory = AbstractFactory(game_mode) # 抽象工厂实例
    environment = GameEnvironment(absfactory, name)
    environment.play()

if __name__ == '__main__':
    main()

