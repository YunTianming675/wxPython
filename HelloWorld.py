import wx

app = wx.App(False)  # False：不将标准输出/标准错误重定向到窗口
frame = wx.Frame(None, wx.ID_ANY, "Hello World")  # 顶层视图
frame.Show(True)

app.MainLoop()
