John Conway's Game of Life 

Introduction 

John Conway's Game of Life is a game which is based on simple mathethematical rules, but can often produce complex and interesting patterns. In the game, there is a board composed of cells. Given a starting configuration input by the users, the cells either "die" or become "alive" if the following conditions are met: 

- if a cell is alive, it stays alive if it has two or three neighbors which are alive
- if a cell is alive, it dies if it has more than three neighbors (overpopulation) 
- if a cell is alive, it dies if it has less than two neighbors (starvation) 
- if a cell is dead, it becomes alive if it has three neighbors (reproduction) 

Implementation 

This implemenation was created uisng PyGame, a useful Python gaming library. A grid is represented by a pygame.Rect, and each cell of the grid inherits from pygame.Rect and is stored in a two-dimensional array. If the user clicks on a specific cell before starting the simulation, it becomes "alive" using the pygame.Rect.colliderect method. Once the simulation has started, the cells are constantly iterated over and the state of the cell for the next iteration is recorded. The GUI is then updated once the logic has updated the internal state of each of the cells. This continues until the user presses the stop button. 

Installation 

To run this game, clone the repo and install the required dependencies (listed in requirements.txt) using: 
``` bash 

pip -r freeze requirements.txt 

```

To run, simply call your Python3 exectuable using (on my Windows computer using Git Bash, for instance): 

``` bash 

./python.exe gol.py

```

A screen should open up, as shown below. 

If you have another version of PyGame installed on your machine, it will likely be necessary to create a virtual environment first to ensure your other programs don't break. 

Further Reading: 

http://web.mit.edu/sp.268/www/2010/lifeSlides.pdf

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

![](gol.gif)
