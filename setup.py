from cx_Freeze import setup, Executable

base = None    

executables = [Executable("SiMaba.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Si MABA",
    options = options,
    version = "1.0",
    description = 'Game by Teknik Komputer',
    executables = executables
)