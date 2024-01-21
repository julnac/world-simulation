# World Simulation Game

The aim of the project is to implement a program in the form of an explorer's game, in the world of wild animals.

## Game goal
The goal of the game is for the traveler to capture all 3 totems without being eaten by other animals or killed by dangerous plants.

## Organisms
There are animals and plants in the game with different behavior. Some of them move (organisms
animals), some are immobile (plant organisms).  The order in which organisms move in a turn depends on their
initiatives. The animals with the highest initiative move first. In the case of animals
for the same initiative, the order is determined by the principle of seniority (the first one moves longer
living). 
### Animals
1. Wolf
2. Sheep
3. Fox - sharp sense of smell: the fox will never move
to the space occupied by
body stronger than him
4. Turtle - 75% of the time no
changes its position. Repels animal attacks
strength <5. The attacker must
get back on your own
previous field.
5. Antelope - moves two fields
6. CyberSheep - Its primary goal is
extermination of hogweed. Always in charge
towards the nearest one.
If there are none on the board
borscht pretends to be ordinary
sheep
### Plants
1. Grass
2. Milkweed
3. Guarana - animal that eats it, gains +3 force
4. WolfBerries - super deadly
5. Hogweed - only cyber sheep can eat this plant
## Collision
### Fight
Each organism occupies exactly one field in the table, each field can contain at most one organism (in the event of a collision, one of them dies due to the collapse or is moved).
In the event of a collision (one of
organisms are in the same space as another) one of the organisms wins by killing (e.g.
wolf) or by chasing away (e.g. a turtle) a competitor. Winning the match depends on the strength of the body. If the force is equal, the organism that attacked wins.
### Birght
If two organisms with the same species and age grater than 5 meet on the same field a new organism is born. Plants in every round have a 10% chance to grow. When plant grows,  a new plant appears next to it.

## Explorer
The explorer is presented by a red circle. The player can move the explorer by clicking up/down/right/left arrows. There is a special skill, Magic Elixir, which can be activated by pressing the "E" button. It adds +10 to the player's strength. With each subsequent turn, the strength decreases until it reaches its normal level. 

## Beginning
When you run the program on the board it should
there will be several pieces of all types of animals and plants. 

## Information
The console will display information about the results of battles, the consumption of plants and other events taking place in the world. On the right you will see actual turn and score counters. There will be also a animals ranking, showing their force, age and id. 
![image](https://github.com/julnac/world-simulation/assets/112817385/c3109789-1d9d-4a80-bf79-7dcf7d95bae5)

