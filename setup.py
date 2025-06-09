from setuptools import setup

APP = ['main.py']
DATA_FILES = ['tomato.png']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': None,  # Optional: use .icns file later
    'packages': ['tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)