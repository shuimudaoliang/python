# core -->coregui-->coregui$user-->BEC(boundary边界,edge极限,corner边角情况)

import datetime
import winsound
import time
from tkinter import *
import os
# from multiprocessing import Process
import threading

# 获取当前时间：
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 设置闹钟
# alarm_h = '13'
# alarm_m = '49'

# alarm_h = input("闹钟的几时：")
# alarm_m = input("闹钟的几分：")



# 闹钟声音
def play_source():
    music =  'Good Time.wav'
    winsound.PlaySound(music, winsound.SND_ALIAS)

#UI_界面
def make_app():
    _font = ['Hack',14,'bold']
    app = Tk()
    eh = StringVar()
    em = StringVar()
    Label(app,name='lb',text='当前时间:',font=_font).pack()
    Label(app,name='lt',text=(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),font=_font).pack()
    Label(app,name='lalarm',text='设置闹钟：',font=_font).pack()
    Label(app,name='ljs', text='几时', font=_font).pack()
    eh.set(datetime.datetime.now().strftime('%H'))
    Entry(app,name='eh',textvariable=eh).pack()
    em.set(datetime.datetime.now().strftime('%M'))
    Label(app,name='lsf', text='几分', font=_font).pack()
    Entry(app,name='em',textvariable=em).pack()
    Button(app,name='bks', text='开始', command=daoji_time).pack()
    Button(app,name='bcz',text='重置',command=reset_time).pack()
    app.geometry('300x300')
    return app
#更新UI 内容
def ui_alarm():
    # 以线程方式执行更新时间
    def _update_time():
        app.children['lt']['text'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
    def _upstart_button():
        bks = app.children['bks']
        timer = [t for t in threading.enumerate() if t.name =='utimer']
        if timer and flag == 1 :
            bks['state'] = 'disabled'
        else:
            bks['state'] = 'normal'
    def _update_jifen():
        pass
    def _main():
        while True:
            _update_time()
        _upstart_button()
    t = threading.Thread(target=_main, name='utimer')
    t.start()

#开始闹钟倒计时
def daoji_time():
    def _init():
        flag = 1  # 控制循环
        while flag:
            timer = [t for t in threading.enumerate() if t.name =='utimer']
            if timer and flag == 1 :
                app.children['bks']['state'] = 'disabled'
            else:
                bks['state'] = 'normal'
            now_h = datetime.datetime.now().strftime('%H')
            now_m = datetime.datetime.now().strftime('%M')
            if now_h == app.children['eh'].get() and now_m == app.children['em'].get():
                play_source()
                print("时间到了")
                flag = 0
                break
        # print(flag)
    t = threading.Thread(target=_init, name='daoji_timer')
    t.start()

# 重置闹钟时间
def reset_time():
    app.children['bks']['state'] = 'normal'


if __name__ == '__main__':
    app = make_app()
    app.after(0, ui_alarm)
    app.mainloop()
