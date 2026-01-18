-import wx

#设label
lb = " "


#设定窗口
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="字符鉴别", size=(300, 180))
        panel = wx.Panel(parent=self)
        #设字符输入框为tc1
        self.tc1 = wx.TextCtrl(panel)
        #设文本标签为self.statictext
        self.statictext = wx.StaticText(parent=panel, label=lb)
        #设按钮为btn
        btn = wx.Button(parent=panel, label="确定")
        self.Bind(wx.EVT_BUTTON, self.on_click, btn)

        tc = wx.StaticText(panel, label="请输入要鉴别的字符，x.0会被识别成整数")

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(tc, flag=wx.EXPAND|wx.ALL, border=10)
        vbox.Add(self.tc1, flag=wx.EXPAND|wx.ALL, border=10)
        vbox.Add(btn, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        vbox.Add(self.statictext, flag=wx.EXPAND|wx.ALL, border=10)

        panel.SetSizer(vbox)

    def on_click(self):
        type_of_tc1 = format(self.tc1.GetValue())
        try:
            type_of_tc1 = float(type_of_tc1)
            a = 2
        except ValueError:
            a = 1
        if a == 1 and not type_of_tc1 == "None" and not type_of_tc1 == "True" and not type_of_tc1 == "False":
            type_of_tc1 = "该字符为类型：\"字符串\""
        elif a == 1 and type_of_tc1 == "None" or a == 1:
            type_of_tc1 = "该字符为类型：\"空值\""
        elif a == 1 and type_of_tc1 == "True" or type_of_tc1 == "False":
            type_of_tc1 = "该字符为类型：\"布尔值\""
        elif float(type_of_tc1) - int(float(type_of_tc1)) == 0:
            type_of_tc1 = "该字符为类型：\"整数\""
        elif float(type_of_tc1) - int(float(type_of_tc1)) >= 0.0:
            type_of_tc1 = "该字符为类型：\"浮点数\""

        self.statictext.SetLabelText(str(type_of_tc1))


#创建应用程序对象
app = wx.App()
#创建窗口对象
frm = MyFrame()
#显示
frm.Show()
#程序循环
app.MainLoop()
