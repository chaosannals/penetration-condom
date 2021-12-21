import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", 'sys'],
    "excludes": ["tkinter"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Penetration Condom",
    version="0.1",
    description="yet a penetration test tool.",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "app.py",
            base=base,
            icon='app.ico'
        )
    ]
)
