# 模拟数据库
quotes = ('A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 'Facts are stubborn things.')

# 模型
class QuoteModel:

    # 从数据库中读取名人名言
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value

# 视图
class QuoteTerminalView:

    # 显示名人名言
    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))

    # 显示错误
    def error(self, msg):
        print('Error: {}'.format(msg))

    # 选择名人名言
    def select_quote(self):
        return input('Which quote number would you like to see?')

# 控制器
class QuoteTerminalController:

    def __init__(self):
        self.model = QuoteModel()       # 模型实例
        self.view = QuoteTerminalView() # 视图实例

    def run(self):
        valid_input = False

        # 调用视图模型获取用户选择
        while not valid_input:
            n = self.view.select_quote() # 提供交互
            try:
                n = int(n)
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(n))
            else:
                valid_input = True

        # 把数据传递给模型
        quote = self.model.get_quote(n)

        # 视图显示数据
        self.view.show(quote)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()
