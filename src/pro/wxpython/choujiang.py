import random

import wx


def getNameStr(nameLst: list) -> str:
    if len(nameLst) == 0:
        return ""
    str = "参与抽奖的人为:  "
    for name in nameLst:
        str += name
        if name != nameLst[len(nameLst) - 1]:
            str += ',  '
    return str


class MyFrame(wx.Frame):
    nameLst = ['李白', '吴家芳', '杜甫', '白居易', '十步杀一人']

    def click2choose(self, event):
        print("抽奖")
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.nameScroll, self.timer)
        self.timer.Start(100)

    def nameScroll(self, event):
        print("停止抽奖")
        self.staicName.SetLabelText(random.choice(self.nameLst))

    def click2stop(self, event):
        self.timer.Stop()

    def __init__(self, fsize=(600, 800), fpos=(100, 100), ppos=(0, 0), ftitle='python wx 实战'):
        # super(MyFrame, self).__init__(*args, **kwds)
        # 窗口
        wx.Frame.__init__(self, None, title=ftitle, pos=fpos, size=fsize)
        # 面板 - - self 是 frame 哦
        panel = wx.Panel(self, size=fsize, pos=ppos)
        # 按钮
        self.btn = wx.Button(panel, label='开始抽奖', pos=(250, 650))
        self.btn2 = wx.Button(panel, label='结束抽奖', pos=(250, 700))

        self.Bind(wx.EVT_BUTTON, self.click2choose, self.btn)
        self.Bind(wx.EVT_BUTTON, self.click2stop, self.btn2)

        self.SetBackgroundColour('pink')
        self.fontStyle = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.staicText = wx.StaticText(panel, label=getNameStr(self.nameLst))
        self.staicName = wx.StaticText(panel, label="幸运者是谁？", pos=(0, 350), size=(600, 12), style=wx.TE_CENTER)

        self.staicText.SetFont(self.fontStyle)
        self.staicName.SetFont(self.fontStyle)


if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()

    myframe = MyFrame()
    myframe.Show()

    # 窗口一直显示
    app.MainLoop()
