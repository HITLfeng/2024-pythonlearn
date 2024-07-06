import wx


class MyFrame(wx.Frame):
    def __init__(self, fsize=(600, 800), fpos=(100, 100), ppos=(0, 0), ftitle='python wx 实战'):
        # super(MyFrame, self).__init__(*args, **kwds)
        # 窗口
        wx.Frame.__init__(self, None, title=ftitle, pos=fpos, size=fsize)
        # 面板 - - self 是 frame 哦
        panel = wx.Panel(self, size=fsize, pos=ppos)


# 创建应用程序对象
app = wx.App()

myframe = MyFrame()
myframe.Show()

# 窗口一直显示
app.MainLoop()
