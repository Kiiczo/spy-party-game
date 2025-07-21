# Spy Game Web

## Description

A simple browser-based version of the classic party game **Spyfall**. Easily create a set of locations and players, then play with friends—no accounts or downloads required. Built with [PyScript](https://pyscript.net/) and hosted on GitHub Pages using a template from [Nicholas Tollervey](https://github.com/ntoll).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

   - You can open the index.html directly in your browser
   - https://kiiczo.github.io/spy-party-game

## Usage

1. **Enter Locations and Players**  
   - Input each location on a new line in the **Locations** box. Tip: For inspiration, I recommend asking ChatGPT for a set of Spyfall locations!
   - Input each player name on a new line in the **Players** box (avoid spaces).

2. **Start the Game**  
   - Click **Submit** to begin. The input fields will hide, and the game will randomly assign one player as the spy and select a location.

3. **Playing the Game**  
   - Click **Next** to cycle through players.  
   - Each player confirms they have the device by clicking **Yes**.  
   - Non-spies see the secret location; the spy sees a message identifying them as the spy.

4. **Resetting**  
   - After all players have viewed their info, the **Next** button changes to **Reset**, which resets the game and shows the input fields again.

### Game Rules

- The spy does not know the location.
- Non-spies try to identify the spy without revealing the location.
- The spy wins by guessing the location or evading detection.
- Players after some time vote to reveal the spy.

## Features

- 🎲 **Custom Locations:** Enter any set of locations you like.
- 👥 **Flexible Player Setup:** Add/remove players easily.
- ⚡ **Quick Start:** No registration, no downloads.
- 🐍 **PyScript Powered:** Game logic runs in the browser using Python.
- ☁️ **GitHub Pages Hosting:** Share and play instantly.

## Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests for improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [PyScript](https://pyscript.net/) for enabling Python in the browser.
- [Nicholas Tollervey](https://github.com/ntoll) for the PyScript template.