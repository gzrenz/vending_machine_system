import PySimpleGUI as sg

from vending_machine1 import vending_machine
from accounts import Accounts

"""Initialize fields"""
# Accounts
global accs
accs = Accounts("accounts.json")
# Vending Machine
global vm
vm = vending_machine("items.json")
username = ''
password = ''

#PROGRESS BAR

def vending_machine_system():
    layout = [
        [sg.T("Write Item Name:", size=(15, 1)), sg.I(key="-ITEM_NAME-", font="None 15", size=(25, 1)),
         sg.T("Write Item Price:", size=(15, 1)), sg.I(key="-PRICE-", font="None 15", size=(10, 1)),
         sg.T("Write Item Amount:", size=(15, 1)), sg.I(key="-AMOUNT-", font="None 15", size=(10, 1))],
        [sg.Table(values='', headings=["Index", "Item", "Price", "Amount"], key="-TABLE-", size=(500, 10), auto_size_columns=False,
                  col_widths=[5, 30, 15, 15], vertical_scroll_only=False, justification="l", font="None 15"),
         ],
        [sg.B("Add", button_color="green", size=(10, 1)), sg.B("Delete", key="-DEL-", button_color="red"),
         sg.B("Refresh"), sg.Exit()],
    ]

    counter = 1
    items = []
    for item in vm.items:
        items += [[counter, item, str(vm.items[item]["price"]), str(vm.items[item]["amount"])]]
        counter += 1
    window = sg.Window('GX Vending Machine', layout)


    while True:
        event, values = window.read()
        window['-TABLE-'].update(items)
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "Refresh":
            ...
        elif event == "Add":
            print(event, values)
            name = values['-ITEM_NAME-']
            price = values['-PRICE-']
            amount = values["-AMOUNT-"]
            item = [[counter,name, price, amount]]
            items += item
            window["-TABLE-"].update(items)
            window["-ITEM_NAME-"].update('')
            window["-PRICE-"].update('')
            window["-AMOUNT-"].update('')
            vm.add_item(name, amount, price)
            counter += 1
        elif event == '-DEL-':
            if values["-TABLE-"]:
                print(values['-TABLE-'][0][1])
                indx = values["-TABLE-"][0]
                del items[indx]
                window["-TABLE-"].update(items)
                counter -= 1

def progress_bar():
    sg.theme('LightBlue2')
    layout = [[sg.Text('Creating your account...')],
            [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
            [sg.Cancel()]]

    window = sg.Window('Working...', layout)
    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()


def login_signup():
    global username, password
    sg.theme('LightBlue2')
    layout = [
        [sg.Text("Username", size =(15, 1), font=16), sg.InputText(key='-username-', font=16)],
        [sg.Text("Password", size =(15, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
        [sg.Button("Log in"), sg.Button("Sign up"), sg.Button("Cancel")],
        [sg.Text("Username not found", visible=False, key="-user_not_found-")],
        [sg.Text("Password incorrect", visible=False, key="-password_incorrect-")],
        [sg.Text("Username already taken", visible=False, key="-username_already_taken-")]
    ]

    window = sg.Window("Account", layout)

    while True:

        event,values = window.read()
        window['-username-'].update('')
        window['-password-'].update('')
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            window.close()
            break
        else:
            if event == "Log in":
                password = values['-password-']
                username = values['-username-']
                if username not in accs.accounts:
                    window['-user_not_found-'].update(visible=True)
                else:
                    if password != accs.accounts[username]["password"]:
                        window['-password_incorrect-'].update(visible=True)
                        break
                    else:
                        window.close()
                        vending_machine_system()
                        break

            elif event == "Sign up":
                password = values['-password-']
                username = values['-username-']
                if username in accs.accounts:
                    window['-username_already_taken-'].update(visible=True)
                else:
                    progress_bar()
                    accs.accounts.update({username : {'balance' : 0, 'password' : password}})
                    accs.refresh()

login_signup()


# create_account()


# def login():
#     global username,password
#     sg.theme("LightBlue2")
#     layout = [[sg.Text("Log In", size =(15, 1), font=40)],
#             [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-usrnm-', font=16)],
#             [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-pwd-', password_char='*', font=16)],
#             [sg.Button('Ok'),sg.Button('Cancel')]]
#
#     window = sg.Window("Log In", layout)
#
#     while True:
#         event,values = window.read()
#         if event == "Cancel" or event == sg.WIN_CLOSED:
#             break
#         else:
#             if event == "Ok":
#                 if values['-usrnm-'] == username and values['-pwd-'] == password:
#                     sg.popup("Welcome!")
#                     break
#                 elif values['-usrnm-'] != username or values['-pwd-'] != password:
#                     sg.popup("Invalid login. Try again")
#
#     window.close()
# login()