from pyscript import display, document


def update_sections(e):
    grade = document.getElementById("grade").value
    section = document.getElementById("section")

    if grade == "gr10":
        section.innerHTML = """
        <option>Ruby</option>
        <option>Sapphire</option>
        <option>Topaz</option>
        <option>Emerald</option>
        """

    elif grade == "gr11":
        section.innerHTML = """
        <option>Luna</option>
        <option>Hidalgo</option>
        <option>Amorsolo</option>
        """


def account_authenticator(e):
    document.getElementById("output").innerHTML = ""

    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    if grade == "gr10":
        if section == "Ruby":
            display("You are part of the Blue Bears", target="output")
        elif section == "Sapphire":
            display("You are part of the Green Hornets", target="output")
        elif section == "Topaz":
            display("You are part of the Yellow Tigers", target="output")
        elif section == "Emerald":
            display("You are part of the Red Bulldogs", target="output")

    elif grade == "gr11":
        if section == "Luna":
            display("You are part of the Blue Bears", target="output")
        elif section == "Hidalgo":
            display("You are part of the Green Hornets", target="output")
        elif section == "Amorsolo":
            display("You are part of the Yellow Tigers", target="output")