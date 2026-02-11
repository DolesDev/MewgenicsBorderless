import win32gui
import win32con
import win32api
import time

# Small script to give Mewgenics borderless fullscreen
# MIT License - Doles - Feb. 2026


def make_borderless():
    print("Searching for Mewgenics...")
    while True:
        # 1. Look for the Mewgenics window. Should be called "Mewgenics!"
        hwnd = win32gui.FindWindow(None, "Mewgenics!")
        
        if hwnd:
            print("Mewgenics found! Applying borderless fix...")
            
            # 2. Strip them borders
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
            style &= ~win32con.WS_CAPTION
            style &= ~win32con.WS_THICKFRAME
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

            # 3. Force to screen size
            width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
            height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
            
            # tell the OS to refresh the window style immediately
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, width, height, win32con.SWP_FRAMECHANGED)
            
            print("Meow. Enjoy the cats.")
            break
            
        time.sleep(2) # check every 2 seconds

if __name__ == "__main__":
    make_borderless()