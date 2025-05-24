import tkinter as tk
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def set_volume(val):
    volume_level = float(val) / 100
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def get_current_volume():
    return int(volume.GetMasterVolumeLevelScalar() * 100)

root = tk.Tk()
root.title("Volume Controller")
root.geometry("320x140")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

label = tk.Label(root, text="System Volume", font=("Arial", 16), fg="white", bg="#1e1e1e")
label.pack(pady=15)

slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=260,
                  command=set_volume, bg="#2e2e2e", fg="white", troughcolor="#555",
                  highlightthickness=0)
slider.set(get_current_volume())
slider.pack()

root.mainloop()
