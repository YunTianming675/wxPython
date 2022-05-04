from cProfile import label
from time import sleep
from matplotlib import style
import wx

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Your quote: ", pos=(20, 30))

        # 一个文本控件，该控件将显示此程序的事件响应是如何工作的
        self.logger = wx.TextCtrl(self, pos=(350, 20), size=(200, 300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # button控件
        self.button = wx.Button(self, label="Save", pos=(200, 325))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        # 文本控件，可编辑的，只有一行的版本
        self.lblname = wx.StaticText(self, label="Your name: ", pos=(20, 60))
        self.editname = wx.TextCtrl(self, value="Enter here your name", pos=(190, 60), size=(140, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # combobox Control
        self.sampleList = ["friends", "advertising", "web search", "Yellow Pages"]
        self.lblhear = wx.StaticText(self, label="How did you hear from us ?", pos=(20, 90))
        self.edithear = wx.ComboBox(self, pos=(190, 90), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.edithear)

        # Checkbox
        self.insure = wx.CheckBox(self, label="Do you want Insured Shipment ?", pos=(20, 180))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # Radio Boxes
        radioList = ["blue", "red", "yellow", "orange", "green", "purple", "navy blue", "black", "gray"]
        rb = wx.RadioBox(self, label="What color would you like ?", pos=(20, 210), choices=radioList, majorDimension=3, style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

    
    def EvtRadioBox(self, event):
        self.logger.AppendText("EvtRadioBox: %d\n" % event.GetInt())

    def EvtComboBox(self, event):
        self.logger.AppendText("EvtComboBox: %s\n" % event.GetString())

    def OnClick(self, event):
        self.logger.AppendText("Click on object with ID: %d\n" % event.GetId())
    
    def EvtText(self, event):
        self.logger.AppendText("EvtText: %s\n" % event.GetString())

    def EvtChar(self, event):
        self.logger.AppendText("EvtChar: %d\n" % event.GetKeyCode())
        event.Skip()
    
    def EvtCheckBox(self, event):
        self.logger.AppendText("EvtCheckBox: %d\n" % event.GetId())


app = wx.App(False)
frame = wx.Frame(None, size=(600, 480))
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
