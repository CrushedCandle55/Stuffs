import wx
import math

class Calculator(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Calculator", size=(400, 600))
        self.panel = wx.Panel(self)
        self.create_widgets()
        self.Show()

    def create_widgets(self):
        # 创建菜单栏
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        mode_menu = wx.Menu()
        unit_menu = wx.Menu()
        menubar.Append(file_menu, "&File")
        menubar.Append(mode_menu, "&Mode")
        menubar.Append(unit_menu, "&Unit")
        self.SetMenuBar(menubar)

        # 创建文件菜单项
        exit_item = file_menu.Append(wx.ID_EXIT, "E&xit", "Exit the program")

        # 创建模式菜单项
        simple_mode_item = mode_menu.Append(wx.ID_ANY, "Simple Mode", "Switch to Simple Mode")
        scientific_mode_item = mode_menu.Append(wx.ID_ANY, "Scientific Mode", "Switch to Scientific Mode")

        # 创建单位菜单项
        length_item = unit_menu.Append(wx.ID_ANY, "Length", "Convert Length")
        temperature_item = unit_menu.Append(wx.ID_ANY, "Temperature", "Convert Temperature")

        # 绑定事件处理函数
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
        self.Bind(wx.EVT_MENU, self.on_simple_mode, simple_mode_item)
        self.Bind(wx.EVT_MENU, self.on_scientific_mode, scientific_mode_item)
        self.Bind(wx.EVT_MENU, self.on_convert_length, length_item)
        self.Bind(wx.EVT_MENU, self.on_convert_temperature, temperature_item)

        # 创建文本框
        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_RIGHT)

        # 创建数字按钮
        grid_sizer = wx.GridSizer(rows=4, cols=4, gap=(5, 5))
        for label in ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "C", "+"]:
            button = wx.Button(self.panel, label=label)
            grid_sizer.Add(button, 0, wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, self.on_button_click, button)

        # 创建布局
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text_ctrl, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizer(sizer)

    def on_exit(self, event):
        self.Close()

    def on_simple_mode(self, event):
        pass # TODO: 切换到简化计算器模式

    def on_scientific_mode(self, event):
        pass # TODO: 切换到科学计算器模式

    def on_convert_length(self, event):
        pass # TODO: 切换到长度单位换算器

    def on_convert_temperature(self, event):
        pass # TODO: 切换到温度单位换算器

    def on_button_click(self, event):
        button = event.GetEventObject()
        label = button.GetLabel()
        value = self.text_ctrl.GetValue()

        if label == "C":
            value = ""
        elif label == "=":
            try:
                value = str(eval(value))
            except:
                value = "Error"
        else:
            value += label

        self.text_ctrl.SetValue(value)

if __name__ == "__main__":
    app = wx.App()
    calculator = Calculator()
    app.MainLoop()
