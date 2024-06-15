# ------------------------- CHANGELOG --------------------------- #
# v0.1 - 12/08/2022
#       Initial release: Simplistic Mining Calculator.
#
# v0.2 - 14/08/2022
#       Layout bugs fixed.
#       Adjusted Ergo Logo.
#       Added function to save Miner Results to a json file.
#       The function "_call" was split into multiple functions.
#
# v.03 - 17/08/2022:
#       Created README.md with an explanation on how to use this calculator and additional notes.
#       Added new button with Ergo Platform banner that redirects to the website ErgoPlatform.org.
#       Change "Calculate" button from text to an Ergo Logo image.
#       Refactored the code to be able to work with the new folder structure (easier to update/maintain)
#       Corrected the input field "Network Hash".
#       Added API functionality to the "Price", "Network Hashrate" and "Block Rewards", powered by TokenJay.App and WhatToMine.com
#
# -------------------------- MODULES ---------------------------- #
from Ergo_Mining_Calc.views import gui


# ---------------------------- MAIN ------------------------------ #
start: gui.Ergo = gui.Ergo()
