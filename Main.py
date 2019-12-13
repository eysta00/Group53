# This file will run the program as a whole
# Main -> UI files -> Logic Layers -> Data layers (IO)
#            ^              <-             <-
from UI.MenuUI import MenuUI
main = MenuUI()
program = ""
while program != "quit_run": # This way, when you input "q" instead of returning None it returns "quit_run" string and the program doesnt stop at ex. listing employees.
    program = main.showMainMenu()