# FOR SIGN_UP.HTML 

from pyscript import display, document
from js import window



def username_verification(e):
    document.getElementById('output').innerHTML = ' '

    username = document.getElementById('username').value
    username_length = len(username)
    username_has_number = any(char.isdigit() for char in username)
    username_has_special = any(not char.isalnum() for char in username)



    if username_length < 10:
        display(f'Username TOO SHORT. Add at least {10 - username_length} more character/s to continue.', target='output')
    elif not username_has_number:
        display(f'Username must contain AT LEAST ONE NUMBER.', target='output')
    elif not username_has_special:
        display(f'Username must contain AT LEAST ONE SPECIAL CHARACTER.', target='output')
    else:
        return(True)
    
    # added special characters and numbers to the username 


def password_verification(e):
    document.getElementById('output').innerHTML = ' '

    password = document.getElementById('password').value
    password_length = len(password)
    password_has_number = any(char.isdigit() for char in password)
    password_has_letter = any(char.isalpha() for char in password)
    password_has_special = any(not char.isalnum() for char in password)

# added special characters to the password 

    if password_length < 10:
        display(f'Your password is too short. Add at least {10 - password_length} more character/s to proceed.', target='output')
    elif not password_has_letter:
        display(f'Password must contain AT LEAST ONE LETTER.', target='output')
    elif not password_has_number:
        display(f'Password must contain AT LEAST ONE NUMBER.', target='output')
    elif not password_has_special:
        display(f'Password must contain AT LEAST ONE SPECIAL CHARACTER.', target='output')
    else:
        return(True)


def account_creation(e):
    document.getElementById('output').innerHTML = ' '

    if username_verification(e) == True and password_verification(e) == True:
        window.location.href = "team_checker.html"
    else:
        display(f'Please try again :)', target='output')
