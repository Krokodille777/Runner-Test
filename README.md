# Runner-Test

===
Runner-test is a simple endless runner game built with Pygame-ce module. Gameplay is very similar to the Google Dino game:

- Run and jump over obstacles which really don't like your presence.
- The game speeds up, yet the acceleration is quite gentle to keep the game playable.
- Score increases passively as you survive longer.
- If one of these pesky obstacles touches you, it's game over!

===

## How to run it?

Follow these steps to run the game:

1. Before installed, make sure you have installed Python 3.10 or higher on your system.
2. Clone the repository to your IDE or local machine.
3. This game requires the "pygame-ce" module. You can install it using pip, when the repo has been closed:

   ```
   pip install pygame-ce
   ```
   *Just don't confuse it with the regular pygame module!* ~~(Though it might work too)~~

4. Navigate to the project directory in your terminal or command prompt.
5. Run the game using the following command:

   ```
   python game.py
   ```
6. Enjoy the game! ~~If you can~~

===

## Controls

- Press the **SPACEBAR** to make the player jump.

===

## Game Mechanics

- The game world starts at a speed of 200 pixels per second and accelerates over time.
- Obstacles spawn randomly with a bias towards spikes over pterodactyls ~~(rhombus)~~. Spawning also speeds up as the game progresses.
- The player can jump to avoid obstacles. The jump height is fixed.
- The game ends when the player collides with an obstacle.

===

## Fun Facts

- Before runner, I planned to turn this into a platformer with levels and all, but I scrapped the idea to focus on making a simple endless runner.

===

## Contributing

Contributions are **always** welcome! If you have any ideas for improvements or new features, feel free to fork the repository and submit a pull request. 

===

## Gratitude 

Special thanks to the Pygame-ce community for their support and resources that made this project possible!

> *Enjoy running and jumping!* 