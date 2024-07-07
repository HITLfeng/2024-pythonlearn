import wx

class MyFrame2(wx.Frame):
    def __init__(self):
        # 窗口
        wx.Frame.__init__(self, None, title='计算器', pos=(100, 100), size=(500, 800))
        # 面板 - - self 是 frame 哦
        self.panel = wx.Panel(self, pos=(0, 0), size=(500, 800))
        self.entry = wx.TextCtrl(self.panel, pos=(10, 10), size=(470, 30), style=wx.TE_RIGHT)

        # 创建按钮
        self.btn_clear = wx.Button(self.panel, label='C', pos=(10, 50), size=(100, 100))
        self.btn_div = wx.Button(self.panel, label='/', pos=(120, 50), size=(100, 100))
        self.btn_mul = wx.Button(self.panel, label='*', pos=(230, 50), size=(100, 100))
        self.btn_back = wx.Button(self.panel, label='<-', pos=(340, 50), size=(100, 100))

        self.btn_7 = wx.Button(self.panel, label='7', pos=(10, 160), size=(100, 100))
        self.btn_8 = wx.Button(self.panel, label='8', pos=(120, 160), size=(100, 100))
        self.btn_9 = wx.Button(self.panel, label='9', pos=(230, 160), size=(100, 100))
        self.btn_sub = wx.Button(self.panel, label='-', pos=(340, 160), size=(100, 100))

        self.btn_4 = wx.Button(self.panel, label='4', pos=(10, 270), size=(100, 100))
        self.btn_5 = wx.Button(self.panel, label='5', pos=(120, 270), size=(100, 100))
        self.btn_6 = wx.Button(self.panel, label='6', pos=(230, 270), size=(100, 100))
        self.btn_add = wx.Button(self.panel, label='+', pos=(340, 270), size=(100, 100))

        self.btn_1 = wx.Button(self.panel, label='1', pos=(10, 380), size=(100, 100))
        self.btn_2 = wx.Button(self.panel, label='2', pos=(120, 380), size=(100, 100))
        self.btn_3 = wx.Button(self.panel, label='3', pos=(230, 380), size=(100, 100))
        self.btn_equal = wx.Button(self.panel, label='=', pos=(340, 380), size=(100, 210))

        self.btn_0 = wx.Button(self.panel, label='0', pos=(10, 490), size=(210, 100))
        self.btn_point = wx.Button(self.panel, label='.', pos=(230, 490), size=(100, 100))

        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.On_btn_clear, self.btn_clear)
        self.Bind(wx.EVT_BUTTON, self.On_btn_div, self.btn_div)
        self.Bind(wx.EVT_BUTTON, self.On_btn_mul, self.btn_mul)
        self.Bind(wx.EVT_BUTTON, self.On_btn_back, self.btn_back)
        self.Bind(wx.EVT_BUTTON, self.On_btn_7, self.btn_7)
        self.Bind(wx.EVT_BUTTON, self.On_btn_8, self.btn_8)
        self.Bind(wx.EVT_BUTTON, self.On_btn_9, self.btn_9)
        self.Bind(wx.EVT_BUTTON, self.On_btn_sub, self.btn_sub)
        self.Bind(wx.EVT_BUTTON, self.On_btn_4, self.btn_4)
        self.Bind(wx.EVT_BUTTON, self.On_btn_5, self.btn_5)
        self.Bind(wx.EVT_BUTTON, self.On_btn_6, self.btn_6)
        self.Bind(wx.EVT_BUTTON, self.On_btn_add, self.btn_add)
        self.Bind(wx.EVT_BUTTON, self.On_btn_equal, self.btn_equal)
        self.Bind(wx.EVT_BUTTON, self.On_btn_0, self.btn_0)
        self.Bind(wx.EVT_BUTTON, self.On_btn_point, self.btn_point)
        self.Bind(wx.EVT_BUTTON, self.On_btn_1, self.btn_1)
        self.Bind(wx.EVT_BUTTON, self.On_btn_2, self.btn_2)
        self.Bind(wx.EVT_BUTTON, self.On_btn_3, self.btn_3)

    def On_btn_clear(self, event):
        self.entry.Clear()

    def On_btn_div(self, event):
        self.entry.AppendText('/')

    def On_btn_mul(self, event):
        self.entry.AppendText('*')
    def On_btn_back(self, event):
        text = self.entry.GetValue()
        self.entry.SetValue(text[:-1])
    def On_btn_7(self, event):
        self.entry.AppendText('7')
    def On_btn_8(self, event):
        self.entry.AppendText('8')
    def On_btn_9(self, event):
        self.entry.AppendText('9')
    def On_btn_sub(self, event):
        self.entry.AppendText('-')
    def On_btn_4(self, event):
        self.entry.AppendText('4')
    def On_btn_5(self, event):
        self.entry.AppendText('5')
    def On_btn_6(self, event):
        self.entry.AppendText('6')
    def On_btn_add(self, event):
        self.entry.AppendText('+')
    def On_btn_1(self, event):
        self.entry.AppendText('1')
    def On_btn_2(self, event):
        self.entry.AppendText('2')
    def On_btn_3(self, event):
        self.entry.AppendText('3')
    def On_btn_equal(self, event):
        text = self.entry.GetValue()
        result = str(eval(text))
        self.entry.SetValue(result)
    def On_btn_0(self, event):
        self.entry.AppendText('0')
    def On_btn_point(self, event):
        self.entry.AppendText('.')

if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()

    myframe = MyFrame2()
    myframe.Show()

    # 窗口一直显示
    app.MainLoop()
