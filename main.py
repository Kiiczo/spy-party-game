from js import document
from pyodide.ffi import create_proxy
import random

locations = None
players = None
spy = None
actual = None
here = None
showing = False
reseting = False


def game():
    global spy, actual, here
    output_div = document.querySelector("#output")
    output_div.innerHTML = ""

    spy = random.choice(players)
    actual = 0
    while here == None or here == "":
        here = random.choice(locations)

    game_text = document.createElement("div")
    game_text.id = "game-text"
    game_text.innerText = "Game is starting! Click next to continue"
    output_div.appendChild(game_text)

    next_button = document.createElement("button")
    next_button.innerText = "Next"
    next_button.id = "next-button"
    next_button.addEventListener("click", create_proxy(next_step))

    output_div.appendChild(document.createElement("br"))
    output_div.appendChild(next_button)

def next_step(event):
    global actual, showing, reseting,game_text,next_button
    game_text = document.querySelector("#game-text")
    next_button = document.querySelector("#next-button")
    
    if not showing and not reseting:
        game_text.innerText = players[actual] + " are you holding the phone?"
        next_button.innerText = "Yes"
        showing = True
    elif not reseting:
        if players[actual] != spy:
            game_text.innerText = "The location is: " + here
        else:
            game_text.innerText = "You are a spy!"
        next_button.innerText = "Next"
        
        if actual == len(players) - 1:
            next_button.innerText = "Reset"
            reseting = True
        showing = False
        actual+=1
    else:
        reset()

def reset():
    global locations,players,spy,actual,here,showing,reseting
    submit_button.style.display = "block"
    locations_text.style.display = "block"
    players_text.style.display = "block"
    game_text.remove()
    next_button.remove()
    locations = None
    players = None
    spy = None
    actual = None
    here = None
    showing = False
    reseting = False

def submit_event(event):
    global locations, players, submit_button,players_text,locations_text
    
    locations_text = document.querySelector("#locations")
    locations = locations_text.value.strip().splitlines()

    
    players_text = document.querySelector("#players")
    players = players_text.value.split()

    submit_button = document.querySelector("#submit")
    submit_button.style.display = "none"
    locations_text.style.display = "none"
    players_text.style.display = "none"

    game()
