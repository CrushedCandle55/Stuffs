# 項目名稱：ttscalcu
import os
from text_to_speech import save
from playsound import playsound
import wx
import time
import pyaudio
import wave
app = wx.App

folder = os.path.exists("file_for_ttscalcu")
# determine whether the file is created or not
if not folder:
    # if not created, create the file
    os.makedirs("file_for_ttscalcu")

# Recording parameter
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "file_for_ttscalcu/recording_sound.wav"
audio = pyaudio.PyAudio()

ttscalcu_rs = None
lang = None
choose_lang = None
click_on_record = 1

"""
# wxPython windows creating
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="ttscalcu", size=(300, 200))
        panel = wx.Panel(parent=self)
        # Text of Question
        self.statictext = wx.StaticText(parent=panel,;..;........................................................................................................................................................................................................
                                        label="        ,l  请选择朗读语言\n          請選擇朗讀語言"
                                              "\nPlease Choose the language", pos=(110, 20))
        # Create button
        button_english = wx.Button(parent=panel, id=10, label="English")
        button_chinese = wx.Button(parent=panel, id=11, label="中文")

        # create BoxSizer of Hrzt
        horiz = wx.BoxSizer(wx.HORIZONTAL)
        horiz.Add(button_chinese, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        horiz.Add(button_english, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # create BoxSizer of VTC
        vert = wx.BoxSizer(wx.VERTICAL)
        vert.Add(self.statictext, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE | wx.TOP, border=10)
        vert.Add(horiz, proportion=1, flag=wx.CENTER)

        panel.SetSizer(vert)

        # Set effect of button
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

    def on_click(self, event):
        global lang
        global choose_lang
        event_id = event.GetId()
        print(event_id)
        # Choose English for language
        if event_id == 10:
            global lang
            global choose_lang
            self.statictext.SetLabelText("You choose: English")
            lang = "en"
            time.sleep(5)
            wx.Frame.Close(self)

        # Choose Chinese for language
        else:
            self.statictext.SetLabelText("你选择了：中文")
            lang = "zh"
            time.sleep(5)
            wx.Frame.Close(self)


app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()
"""

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="ttscalcu", size=(300, 200))
        self.on_record = None
        panel = wx.Panel(parent=self)
        # Text of Question
        self.statictext = wx.StaticText(parent=panel,
                                        label="点击下方按钮开始朗读算式\n點擊下方按鈕開始朗讀算式"
                                              "\nClick the button below for starting read the question")

        # Let recording_icon image be a button
        record = wx.Button(parent=panel, label="开始朗读 開始朗讀 Start Speaking")
        self.Bind(wx.EVT_BUTTON, self.on_click, record)

        # create BoxSizer of Hrzt
        horiz = wx.BoxSizer(wx.HORIZONTAL)
        horiz.Add(self.statictext, proportion=1, flag=wx.EXPAND | wx.TOP, border=5)
        horiz.Add(record, proporation=1, flag=wx.EXPAND | wx.BOTTOM, border=5)

    def on_click(self, event):
        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                          rate=RATE, input=True,
                          frames_per_buffer=CHUNK)
        print("recording...")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("finished recording")

        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        wavefile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wavefile.setnchannels(CHANNELS)
        wavefile.setsampwidth(audio.get_sample_size(FORMAT))
        wavefile.setframerate(RATE)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()

app2 = wx.App()
frm2 = MyFrame()
frm2.Show()
app2.MainLoop()

# text turn to speech
text = str(ttscalcu_rs)
# language
language = str(lang)
# Path of the file
output_file = "file_for_ttscalcu/ttscalcurs.mp3"

save(text, language, file=output_file)

playsound(str(output_file))
