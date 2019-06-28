# -*- coding: utf-8 -*-
import os
from PyQt5.QtCore import QSettings


def import_settings():
    """
    Imports settings from settings.ini file.
    If the file doesn't exist it creates it.

    :return QSettings: The QSettings object containing settings from the settings.ini file
    """
    if os.path.exists('settings.ini'):
        return QSettings('settings.ini', QSettings.IniFormat)
    else:
        f = open('settings.ini', 'w+')
        write_default_settings(f)
        f.close()
        return QSettings('settings.ini', QSettings.IniFormat)


def write_default_settings(f):
    f.write('[General]\n')
    f.write('match_logs_directory=\n')
