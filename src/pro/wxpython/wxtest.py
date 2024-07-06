import wx

# 绑定触发函数
def btnFunc(event):
    print("123")
    print(event)

# 创建应用程序对象
app = wx.App()

# 创建窗口， None表示依附在谁上面，这里不依附 pos 距离左上角位置 px
frm = wx.Frame(None, size=(600, 800), pos=(100, 100), title='python title for test')

# 显示窗口 一闪而过
frm.Show()

# 创建面板
pl = wx.Panel(frm, size=(600, 800), pos=(0, 0))
pl.Show()

# 创建静态文本
staticText = wx.StaticText(pl, pos=(100, 100), label='Hello World')

# 创建按钮
btn = wx.Button(pl, pos=(100, 200), label='Click Me')
# 这里不调用show也可以展示欸
btn.Show()
# 事件处理，绑定按下按钮后的操作
frm.Bind(wx.EVT_BUTTON, btnFunc, btn)

# 窗口一直显示
app.MainLoop()
