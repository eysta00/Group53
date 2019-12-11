# This file will run the program as a whole
# Main -> UI files -> Logic Layers -> Data layers (IO)
#            ^              <-             <-
from UI.MenuUI import MenuUI
main = MenuUI()
main.showMainMenu()