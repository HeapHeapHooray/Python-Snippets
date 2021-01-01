import tkinter as tk
from threading import Thread


tcl = None
tcl_thread = None

def loop_tcl():
    global tcl
    tcl = tk.Tk()
    tcl.withdraw()
    tcl.mainloop()

def initialize():
    global tcl
    global tcl_thread
    
    if tcl_thread != None:
        print("Already Initialized!")
        return

    tcl_thread = Thread(target=loop_tcl,daemon=True)
    tcl_thread.start()
    while tcl == None:
        pass
    print("TCL Runtime Initialized!")

def create_window() -> tk.Toplevel:
    return tk.Toplevel(width=300,height=300)

initialize()

    
