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


next_button = document.querySelector("#next-button")
submit_button = document.querySelector("#submit")
locations_text = document.querySelector("#locations")
players_text = document.querySelector("#players")
game_text = document.querySelector("#game-text")

def game():
    global spy, actual, here
    game_text.style.display = "block"
    next_button.innerText = "Next"

    spy = random.choice(players)
    actual = 0
    while here == None or here == "":
        here = random.choice(locations)

    game_text.innerText = "Game is starting! Click next to continue"

    next_button.style.display = "block"

def next_step(event):
    global actual, showing, reseting,game_text,next_button
    
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
    game_text.style.display = "none"
    next_button.style.display = "none"
    locations = None
    players = None
    spy = None
    actual = None
    here = None
    showing = False
    reseting = False

def submit_event(event):
    global locations, players, submit_button,players_text,locations_text
    
    locations = locations_text.value.strip().splitlines()
    players = players_text.value.split()

    submit_button.style.display = "none"
    locations_text.style.display = "none"
    players_text.style.display = "none"

    game()
