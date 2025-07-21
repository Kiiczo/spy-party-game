from js import document, fetch
import random
import asyncio

setup = document.getElementById("setup")
game = document.getElementById("game")
locations_text = document.getElementById("locations")
players_text = document.getElementById("players")
spy_count_input = document.getElementById("spy-count")
start_btn = document.getElementById("start-btn")
player_progress = document.getElementById("player-progress")
player_name = document.getElementById("player-name")
role_box = document.getElementById("role-box")
reveal_btn = document.getElementById("reveal-btn")
next_btn = document.getElementById("next-btn")
reset_btn = document.getElementById("reset-btn")
generate_btn = document.getElementById("generate-btn")
prompt_text = document.getElementById("prompt")

locations = []
players = []
spies = []
location = ""
current_player = 0
revealed = False
spies_list = ""

async def fetch_locations(addition):
    generate_btn.style.backgroundColor = "grey"  
    url = "https://spygame-ai.witold-zzak.workers.dev" + addition
    response = await fetch(url)
    text = await response.text()
    generated = [line.strip() for line in text.splitlines() if line.strip()]
    generate_btn.style.backgroundColor = "#1d4ed8" 
    return generated

def submit_event(event=None):
    global locations, players, spies, location, current_player, revealed, spies_list

    locations = [l.strip() for l in locations_text.value.strip().splitlines() if l.strip()]
    players = [p.strip() for p in players_text.value.replace('\n', ' ').split() if p.strip()]

    spy_count = int(spy_count_input.value)
    if spy_count < 1: spy_count = 1
    if spy_count > len(players): spy_count = len(players)

    spies = random.sample(players, spy_count)
    spies_list = ""
    for i in spies:
        spies_list = spies_list + " " + i
    location = random.choice(locations)
    current_player = 0
    revealed = False

    setup.classList.add("hidden")
    game.classList.remove("hidden")
    next_btn.style.display = "none"
    reset_btn.style.display = "none"
    reveal_btn.style.display = "block"
    show_player()

def show_player():
    global revealed
    revealed = False
    player_progress.innerText = f"Player {current_player+1} of {len(players)}"
    player_name.innerText = players[current_player]
    role_box.innerHTML = f"Pass the device to <b>{players[current_player]}</b> and click Next to reveal their role."
    reveal_btn.innerText = "Reveal Role"
    reveal_btn.style.display = "block"
    next_btn.style.display = "none"
    reset_btn.style.display = "none"

def reveal_role(event=None):
    global revealed
    if revealed:
        return
    revealed = True
    if players[current_player] in spies:
        if len(spies) == 1:
            role_box.innerHTML = "<b>You are a SPY!</b><br>Try to guess the location."
        else:
            role_box.innerHTML = f"<b>You are a SPY!</b><br>Try to guess the location with:</b><br>{spies_list.replace(players[current_player], '')}"
    else:
        role_box.innerHTML = f"<b>The location is:</b><br>{location}"
    reveal_btn.style.display = "none"
    next_btn.style.display = "block"
    if current_player == len(players) - 1:
        next_btn.innerText = "Finish"
    else:
        next_btn.innerText = "Next"

def next_player(event=None):
    global current_player
    if current_player < len(players) - 1:
        current_player += 1
        show_player()
    else:
        player_progress.innerText = "All roles revealed!"
        player_name.innerText = ""
        role_box.innerHTML = "Game finished. Start a new game?"
        reveal_btn.style.display = "none"
        next_btn.style.display = "none"
        reset_btn.style.display = "block"

def reset_game(event=None):
    setup.classList.remove("hidden")
    game.classList.add("hidden")
    role_box.innerText = ""
    player_name.innerText = ""
    player_progress.innerText = ""

async def generate_list(event=None):

    prompt = prompt_text.value
    if prompt == None:
        prompt = ""
    else:
        prompt = "/?query=" + prompt

    generated = await fetch_locations(prompt)
    generated_text = ""
    for i in generated:
        generated_text+= i + "\n"
    locations_text.value = generated_text

game.classList.add("hidden")
reset_btn.style.display = "none"
next_btn.style.display = "none"