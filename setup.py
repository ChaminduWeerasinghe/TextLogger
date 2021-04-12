import sys
from cx_Freeze import setup, Executable
import os

# Dependencies are automatically detected, but it might need fine tuning.
projectLocation = os.path.dirname(os.curdir)
build_exe_options = {
    "packages": ["os", "tkinter", "pynput.keyboard", "Windows.PssUI","Windows.PopUI","Helper.Res",'multiprocessing'],
    "include_files": [(os.path.join(projectLocation,'','logo.ico'),"logo.ico"),(os.path.join(projectLocation,'','logo.xbm'),"logo.xbm"),(r"C:/Users/chami/AppData/Local/Programs/Python/Python39/DLLs/tcl86t.dll","tcl86t.dll"),(r"C:/Users/chami/AppData/Local/Programs/Python/Python39/DLLs/tk86t.dll","tk86t.dll")]
}
# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Keypress Logger",
        version = "0.1",
        description = "Data Collection Applicaton!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("TextLogger.py", base=base)])