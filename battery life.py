from tkinter import*
from tkinter import ttk
import psutil
from psutil._common import BatteryTime
import datetime
import time

root=Tk()

root.title("battery")
root.geometry("500x250")
root.overrideredirect(True)
root.config(bg="black")

style=ttk.Style(root)
style.layout("ProgressBarStyle",
             [("Horizontal.Progressbar.trough",
               {"children":[("Horizontal.Progressbar.pbar",
                             {"side":"right","sticky":"ns"})],
                "sticky":"nsew"}),
              ("Horizontal.Progressbar.label",{"sticky":""})])

bar=ttk.Progressbar(root,maximum=100,style="ProgressBarStyle")
bar.place(relx=0.5,rely=0.2,anchor=CENTER)

batterylife=Label(root,font="arial 15 bold",bg="black",fg="white")
batterylife.place(relx=0.5,rely=0.5,anchor=CENTER)

def convertTime(seconds):
    getTime=time.gmtime(seconds)
    time_remain=time.strftime("%H:%M:%S",getTime)
    return time_remain

def getBatteryLife():
    battery=psutil.sensors_battery()
    bar["value"]=battery.percent
    style.configure("ProgressBarStyle",text=str(battery.percent)+" %")
    battery_left=convertTime(battery.secsleft)
    if battery.secsleft==BatteryTime.POWER_TIME_UNLIMITED:
        batterylife["text"]="unplugged the battery \n and return to the code again"

    elif battery.secsleft==BatteryTime.POWER_TIME_UNKNOWN:
        batterylife["text"]="battery life not detected \n please run the code again"

    else:
        batterylife["text"]="battery life : "+battery_left
        root.after(1000,getBatteryLife)
        
getBatteryLife
root.mainloop()
