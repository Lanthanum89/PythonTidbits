# Temporal Explorer - Time Travel Adventure Game

An interactive text-based adventure game where players travel through different time periods to solve a temporal mystery.

## Description

Temporal Explorer is a console-based adventure game that puts you in the role of a time traveler tasked with preventing temporal anomalies. Travel between different time periods, collect items, and uncover the mystery behind timeline disruptions.

## How to Run

```bash
python3 timeTravelGame.py
```

## Features

- **Multiple Time Periods**: Travel between Present, Ancient Egypt, Renaissance Italy, and Neo Tokyo 2250
- **Interactive Storytelling**: Make choices that affect your journey
- **Inventory System**: Collect and use items across different time periods
- **Typewriter Effect**: Immersive text display with realistic typing animation
- **Mystery Solving**: Discover the secret of the golden scarab to save the timeline
- **Error Handling**: Robust input validation and graceful error recovery
- **Multiple Endings**: Different outcomes based on your actions

## Requirements

- Python 3.x

## Time Periods & Locations

1. **Present (2025)** - Research Lab: Your starting point and base of operations
2. **Ancient Egypt (2500 BCE)** - Discover mysterious hieroglyphs and ancient artifacts
3. **Renaissance Italy (1500)** - Explore an artist's workshop with mechanical inventions
4. **Neo Tokyo (2250)** - Navigate a futuristic city with holographic displays

## Example Gameplay

```
Welcome to Temporal Explorer!
You are a time traveler tasked with preventing temporal anomalies.
Explore different time periods and solve the mystery!

You're in your research lab. The time machine is ready.
Where would you like to travel?

Options: ancient, renaissance, future, inventory, quit
ancient

You materialize in Ancient Egypt.
You see a mysterious hieroglyph and a golden scarab.

Options: take scarab, examine hieroglyph, return, inventory, quit
take scarab
You picked up the golden scarab.
```

## Game Objective

Discover the secret of the golden scarab by exploring different time periods. The scarab appears in various forms throughout history and holds the key to preventing a temporal disaster. Collect clues from each era to understand its significance and save the timeline.

## Controls

- Type your choices from the available options
- Use 'inventory' to check collected items
- Use 'return' to go back to the present
- Use 'quit' to exit the game
- Press Ctrl+C to pause the game

## How It Works

The game uses a class-based structure with methods for each time period. Player choices determine the story flow, and the inventory system allows items to be carried between time periods, creating connections across different eras.

Perfect for fans of interactive fiction, time travel stories, and puzzle-solving adventures!