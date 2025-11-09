import core.coreMain as interface
import os
import sys
obsoluct_path = os.path.abspath(os.curdir)
sys.path.insert(0, obsoluct_path)
import controllers.accountControllers as ca
accounts = ca.ControllersAccount()
create_accounts = ca.ControllersAccount()

if __name__ == "__main__":
    accounts.selectAccount
    create_accounts.createAccount('CAIO', 'CAIO@HOTMAIL.COM', '12345678932')
    # accounts.createAccount
#     interface_message.layoutWelcome
#     interface_menu.menu

