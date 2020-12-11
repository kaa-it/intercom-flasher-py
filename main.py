# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import parted
import sys

from PySide6.QtWidgets import QApplication, QWidget
#from PySide6 import QtGui

# import gi
#
# gi.require_version("Gtk", "3.0")
# from gi.repository import Gtk

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def testUSB():
    devices = [dev.path for dev in parted.getAllDevices()]
    print(devices)
    usb = parted.getDevice('/dev/sdb')
    print(usb)
    disk = parted.newDisk(usb)
    partitionsDesc = [(part.type, part.number) for part in disk.partitions]
    print(disk.partitions[0])
    # print(disk.partitions[1])
    print(partitionsDesc)
    print(disk.partitions[0].fileSystem.type)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Прошивка домофона")
    window.show()

    app.exec_()

    # Gtk.ListStore(str)
    #
    # win = Gtk.Window()
    # win.connect("destroy", Gtk.main_quit)
    # win.show_all()
    # Gtk.main()

