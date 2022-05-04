import os
import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname = ""

        wx.Frame.__init__(self, parent, title=title, size=(200, -1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filename = wx.Menu()
        menuOpen = filename.Append(wx.ID_OPEN, "Open", "Open a file to edit")
        menuAbout = filename.Append(wx.ID_ABOUT, "About", "Information about this program")
        menuExit = filename.Append(wx.ID_EXIT, "Exit", "Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filename, "File")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)  # 在底部状态栏上再加入一个Box，并指定Box内的组件为横向排列
        self.buttons = []
        for i in range(0, 6):  # 将6个button加入到Box中
            self.buttons.append(wx.Button(self, -1, "Button &" + str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        # 使用一些Sizers进行布局
        # 将sizer2和control放入到一个BoxSizer中
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        # Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "A sample editor in wxPython", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close(True)

    def OnOpen(self, e):
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
