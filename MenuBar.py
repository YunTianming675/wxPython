import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()  # 添加底部状态栏

        filemenu = wx.Menu()  # 添加一个菜单对象

        filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "Exit", "Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # 菜单栏接收一个菜单对象
        self.SetMenuBar(menuBar)
        self.Show(True)


app = wx.App(False)
frame = MainWindow(None, "Sample Editor")
app.MainLoop()
