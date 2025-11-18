import os
import sys
obsoluct_path = os.path.abspath(os.curdir)
sys.path.insert(0, obsoluct_path)
import core.coreMain as cc

interface_messages = cc.CoreMain()

if __name__ == "__main__":
    #Presentation Interface to the user
    interface_messages.layoutWelcome
