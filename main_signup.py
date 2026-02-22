from pyscript import display, document


def create_account(e):
    document.getElementById("output").innerHTML = ""

    username = document.getElementById("username").value
    password = document.getElementById("password").value

    if len(username) < 7:
        display("Username too short", target="output")

    elif len(password) < 10:
        display("Password too short", target="output")

    elif password.isalpha():
        display("Password must contain at least one number", target="output")

    elif password.isdigit():
        display("Password must contain at least one letter", target="output")

    else:
        display("Account created successfully", target="output")

