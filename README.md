# Spy Game

## Description

Spy Game is a fast, browser-based version of the classic party game **Spyfall**—now with new features! Easily create your own set of locations and players, adjust the number of spies, and let each player reveal their role privately. Generate location lists using AI, and play with friends in person or online. Built with [PyScript](https://pyscript.net/) and hosted easily on GitHub Pages.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

**Open `index.html` in your browser.**
- Or [host on GitHub Pages](https://pages.github.com/) for easy sharing.

No additional setup is required!

## Usage

1. **Enter Locations:**  
   - Type each location on a new line.  
   - *Tip:* Use the AI generator by entering a keyword (e.g., "location", "marvel-characters") and clicking "Generate list by ai" for instant ideas.
2. **Enter Players:**  
   - Input player names separated by spaces or new lines.  
   - **Note:** Player names cannot contain spaces.
3. **Choose Number of Spies:**  
   - Set the number of spies for this round (minimum 1, up to the number of players).
4. **Start Game:**  
   - Click "Start Game." Pass the device to each player and let them reveal their secret role.
   - Spies will see their status (and, if more than one, their fellow spies). Others see the secret location.
5. **Play:**  
   - Ask questions, try to blend in or catch the spy!

### Game Rules

- One or more players are randomly assigned as spies; others know the same secret location.
- Players ask one another questions about the location. The spy tries to guess the location without being discovered.
- At any time, players may vote on who they think the spy is, or the spy may try to guess the location.
- **Locations:** Each location must be on a separate line.  
  *Need ideas?* Use the built-in AI generator!
- **Player Names:** No spaces allowed (use underscores or dashes if needed).

## Features

- 🎲 **Custom & AI-Generated Locations:** Enter your own or generate lists with built-in AI support.
- 🕵️ **Multiple Spies:** Set how many spies are in each game.
- 👥 **Flexible Player Input:** Add players easily, using spaces or new lines.
- 🔒 **Private Role Reveal:** Each player sees their role individually.
- ⚡ **Quick Start:** No registration, no downloads.
- 🐍 **PyScript Powered:** Runs entirely in your browser.
- ☁️ **Easy Hosting:** Works great on GitHub Pages.

## Contributing

Contributions are welcome!  
- Open issues for bugs or feature requests.
- Submit pull requests for improvements.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [PyScript](https://pyscript.net/) for enabling Python in the browser.
- [Nicholas Tollervey](https://github.com/ntoll) for the PyScript template inspiration. 
- Cloudflare for the AI-powered location generation backend.