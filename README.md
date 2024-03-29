# Miner Dance

---
In Miner Dance, the player starts out as a small miner trapped on top of a volcano. The goal is to survive as long as possible and rack up as many points as you grow bigger by consuming food for points. 

## About

---
Miner Dance is a game involving a Miner stuck on top of a Volcano, that is tasked with dodging debris that is being shot out of the volcano, collecting coins to try and rack up as many points as possible, using mushrooms to decrease in size to make the game easier, and collecting med kits to increase size and speed, so you can dodge more effectively. 
### [Game Preview](https://youtu.be/4Ko2sXoe97A)


## Instructions

---
Using W to move left and D to move right respectively dodge the rocks falling down on the screen and collect items using the movement.

| Sprite                                      | Representation                                             |
|---------------------------------------------|------------------------------------------------------------|
| <img src="Photos/miner.png" height="60">    | The Player model to be controlled                          |
| <img src="Photos/coins.png" height="60">    | Coins to be collected that <br/>Increase the players score |
| <img src="Photos/rock.png" height="40">     | Rocks falling from the sky that<br/>need to be dodged      |
| <img src="Photos/kit.png" height="60">      | Makes the miner bigger and<br/> also makes them faster     |
| <img src="Photos/mushroom.png" height="60"> | Makes the miner smaller so it<br/>is easier to dodge       |

## Authors

---
| Name          | Email             |
|---------------|-------------------|
| James Gatonye | jamegato@udel.edu |


## Acknowledgements

---
| Website Link                                                                                                                                                             | Reasoning                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [Designer Guide List](https://designer-edu.github.io/designer/contents.html#)                                                                                            | Help with screens, collisions, falling objects and destroying things                             |
| [Github Formatting ](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)    | Helping me set up the README.md file                                                             |
| [Stack Overflow Data Class Help](https://stackoverflow.com/questions/53632152/why-cant-dataclasses-have-mutable-defaults-in-their-class-attributes-declaratio)           | Needed help with getting lives and scores to translate across screens and outside of dataclasses |
| [Stack Overflow Adding Images  ](https://stackoverflow.com/questions/59738918/how-do-i-add-image-to-readme-file-on-gitlab)                                               | Needed help on adding images to my README.md file for this project                               |
 -------------------------------------------

## [Phase 1](https://youtu.be/gazHs2fcIjA): 
- [X] Miner Exists: There is a miner on the screen
- [X] Miner Moves: The miner moves left or right whenever the arrow keys are pressed 
- [X] Spawning Food: Food will randomly spawn inside the boundaries
- [X] Screen Limits: The miner cannot be moved offscreen, I want him to stop when he hits the end of the screen like a collision zone

## [Phase 2](https://youtu.be/z4aX2MOs_PU):
- [X] Rocks Spawning: Rocks will spawn in the sky and on top of the miner inside the boundaries
- [X] Rocks Despawning: Rocks will despawn when they hit the ground and or the miner
- [X] Growth: When the miner consumes food he will grow in size
- [X] Miner Hurt: When the miner gets hit by a rock they should get hurt and lose a heart
- [X] Timer: The timer should be displayed on the screen on startup
- [X] Show Stats: The current score and number of lives are shown in the game in the top right corner of the screen.

## [Phase 3](https://youtu.be/jtC6lTPlDrA):
- [X] Play Button: A play button and home screen should be displayed that takes you into the game 
- [X] Power Ups: Power Ups should spawn around that increase player speed and also give them more health 
- [X] Game Win: A message is displayed when the player runs out of time , or some other visual indicator that the player has Won.
- [X] Game Over: A message is displayed when the player runs out of lives, or some other visual indicator that the player has lost.
- [X] Game UI: Making the Game Look Pretty!
- [X] Mini Mushroom: Add a power up that makes the miner become smaller after consuming it
- [X] Difficulty Ramp Up: The game becomes harder as time progresses

