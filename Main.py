# This file will run the program as a whole
# Main -> UI files -> Logic Layers -> Data layers (IO)
#            ^              <-             <-
from MenuUI import MenuUI
main = MenuUI()
main.showMainMenu()