import wx

#MyFrame窗口
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython", size=(300, 180))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, label="左键测试程序\n请点击\"测试\"键")
        btn1 = wx.Button(parent=panel, id=10, label="测试1")
        btn2 = wx.Button(parent=panel, id=11, label="测试2")

        #设水平方向的盒子布局为hbox
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        #添加btn1和btn2到hbox
        hbox.Add(btn1, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)

        hbox.Add(btn2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        #设垂直方向的盒子布局为vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        #添加文本到vbox
        vbox.Add(self.statictext, proportion=1,
             flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP, border=30)
        #添加按钮(btn)至vbox
        vbox.Add(btn1, proportion=1, flag=wx.EXPAND|wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

    def on_click(self, event):
        self.statictext.SetLabelText("您的左键正常运行！")


#创建应用程序对象
app = wx.App()
#创建窗口对象
frm = MyFrame()
#显示
frm.Show()
#程序循环
app.MainLoop()
