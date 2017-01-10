
from cx_Freeze import setup, Executable


build_option = {
            "packages": [],
            "includes": [],
            "excludes": []
        }
setup(name="psd_unpack",
      version="1.0.0",
      description="author: minu jeong",
      options={
        "build_exe": build_option
      },
      executables=[
        Executable("entry.py", base="Win32GUI")
      ])
