from Modules.menu import Menu
from Modules.fileArrange import fileArrange
from Modules.rename import rename

def Main():
  Menu(rename, fileArrange)
  
Main()