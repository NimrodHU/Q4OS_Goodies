#---Q4OS Goodies---

#---Modules---

from tkinter import *
import os

#---Definitions---

def q4osWelcome():
    os.system('/usr/bin/welcome-screen.exu')

def q4osAddRepo():
    os.system('sudo qrepoadd --gui')

def q4osInstApp():
    os.system('/usr/bin/swcentre.exu')

def q4osUpdateMan():
    os.system('/opt/program_files/q4os-update-manager/bin/updatemgr.exu')

def q4osUpdateManConf():
    os.system('/opt/program_files/q4os-update-manager/bin/um_config.exu')

def q4osDeskProf():
    os.system('/usr/bin/swprofiler.exu')

def q4osLookSwitcher():
    os.system('opt/program_files/lookswitcher/bin/switch_q4osui.sh')
    

#---Graphical Interface---

root = Tk()

root.title("Q4OS Goodies")

labelWelcome = Label(root, text="Welcome to Q4OS Goodies!", font="Helvetica 12 bold")
labelWelcome.pack(fill=BOTH)

labelExp = Label(root, text="A tool that makes easier to access\ncertain management tools of Q4OS.")
labelExp.pack(fill=BOTH)

buttonWelcome = Button(root, text="Welcome screen", command=q4osWelcome)
buttonWelcome.pack(fill=BOTH)

buttonAddRepo = Button(root, text="Add repository", command=q4osAddRepo)
buttonAddRepo.pack(fill=BOTH)

buttonInstApp = Button(root, text="Install applications", command=q4osInstApp)
buttonInstApp.pack(fill=BOTH)

buttonUpdateMan = Button(root, text="Update manager", command=q4osUpdateMan)
buttonUpdateMan.pack(fill=BOTH)

buttonUpdateManConf = Button(root, text="Update manager configurations", command=q4osUpdateManConf)
buttonUpdateManConf.pack(fill=BOTH)

buttonDeskProf = Button(root, text="Desktop profiler", command=q4osDeskProf)
buttonDeskProf.pack(fill=BOTH)

buttonLookSwitcher = Button(root, text="Look Switcher", command=q4osLookSwitcher)
buttonLookSwitcher.pack(fill=BOTH)

root.mainloop()
