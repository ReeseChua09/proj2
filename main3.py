from js import document

blue_bears = [
    "Alotaya, M.",
    "Alwit, D.",
    "Aquino, S.",
    "Brar, O.",
    "Chavez, C.",
    "Chua, R.",
    "De Los Santos, S.",
    "Estabillo, C."
]

red_bulldogs = [
    "Faner, J.",
    "Fernandez, L.",
    "Gale, B.",
    "Garcia, J.",
    "Gill, E.",
    "Kaur, S.",
    "Laeda, L.",
    "Lusica, A."
]

green_hornets = [
    "Macala, S.",
    "Macas, Z.",
    "Maranan, K.",
    "Montemayor, P.",
    "Musor, H.",
    "Omnes, W.",
    "Oreiro, R.",
    "Platon, T."
]

yellow_tigers = [
    "Ramirez, A.",
    "Razonable, M.",
    "Salvador, E.",
    "Salvador, T.",
    "Silleza, L.",
    "Tiwari, K.",
    "Villanueva, L.",
    "NEED 1 MORE FOR EQUALITY"
]

def show_blue(e=None):
    output = document.getElementById("output")
    output.innerHTML = ""
    for player in blue_bears:
        output.innerHTML += player + "<br>"

def show_red(e=None):
    output = document.getElementById("output")
    output.innerHTML = ""
    for player in red_bulldogs:
        output.innerHTML += player + "<br>"

def show_green(e=None):
    output = document.getElementById("output")
    output.innerHTML = ""
    for player in green_hornets:
        output.innerHTML += player + "<br>"

def show_yellow(e=None):
    output = document.getElementById("output")
    output.innerHTML = ""
    for player in yellow_tigers:
        output.innerHTML += player + "<br>"
