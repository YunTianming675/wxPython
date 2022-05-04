import os
import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()  # 创建底部状态栏

        # 设置一个Menu
        filemenu = wx.Menu()

        # 添加两个菜单选项
        menuAbout = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", "Terminate the program")
        menuOpen = filemenu.Append(wx.ID_OPEN, "Open", "Open a file")

        # 创建一个MenuBar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File")  # 将Menu(filemenu)放进MenuBar(menuBar)里
        self.SetMenuBar(menuBar)  # 将MenuBar(menuBar)添加到Frame(主窗口)中

        # 设置事件
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.Show(True)
    
    # 事件的回调方法
    def OnAbout(self, e):
        # 弹出一个消息对话框，此对话框只有一个OK按钮
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()  # 将此对话框显示
        dlg.Destory()  # 销毁此对话框

    def OnExit(self, e):
        self.Close(True)  # 关闭Frame
    
    def OnOpen(self, e):
        self.dirname = ""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), "r")
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()
