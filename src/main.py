import os
import sys
obsoluct_path = os.path.abspath(os.curdir)
sys.path.insert(0, obsoluct_path)
import core.coreMain as cc
import register.register as rr
import controllers.accountControllers as ca

accounts = ca.ControllersAccount()
interface_messages = cc.CoreMain()
interface_menu = rr.Register()
# import controllers.accountControllers as ca
# accounts = ca.ControllersAccount()
# create_accounts = ca.ControllersAccount()

if __name__ == "__main__":
    #Only verify if account was created
    # id_user = accounts.selectAccount('cainhu-victor@hotmail.com')
    # print(f"id_user {id_user[0]}")
    #Presentation Interface to the user
    interface_messages.layoutWelcome
    #Call the menus
    interface_messages.menu
