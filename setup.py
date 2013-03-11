"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['VidiiUStreamer.py']
DATA_FILES = ['template.html', 'images', 'config.txt','loading.ts','settings.html','films.html','tmp','NUL','ffmpeg']
OPTIONS = {'argv_emulation': True,
 'iconfile': './images/vidiiu-icon.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)