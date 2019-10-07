# 事件类
class Event:

    def __init__(self, name):
        """
        Params:
            - name: 事件名称
        """
        self.name = name

    def __str__(self):
        return self.name

# 节点基类
class Widget:

    def __init__(self, lastNode = None):
        """
        Params:
            - lastNode: 对上一个节点的引用
        """
        self.lastNode = lastNode

    # 处理事件的机制
    def handle(self, event):
        """
        Params:
            - event: 表示事件
        """
        # 与事件对应的处理函数
        handler = 'handle_{}'.format(event)

        # 判断此处理函数是否存在
        if hasattr(self, handler):
            # 如果存在处理此 handler，则执行
            method = getattr(self, handler)
            method(event)
        # 判断前节点是否存在
        elif self.lastNode:
            self.lastNode.handle(event)
        # 判断当前实例有没有处理此事件的handler
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):

    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):

    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):

    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()   # MainWindow.__init__(mw, lastNode=None)
    sd = SendDialog(mw) # SendDialog.__init__(sd, lastNode = mw)
    msg = MsgText(sd)   # MsgText.__init__(msg, lastNode = sd)

    # for循环模拟责任链事件请求机制
    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)

        # 责任链模式
        print('\nSending event **{}** to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event **{}** to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event **{}** to MsgText'.format(evt))
        msg.handle(evt)

if __name__ == '__main__':
    main()
