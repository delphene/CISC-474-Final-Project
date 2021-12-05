## IMPLEMENTATION

### OVERVIEW
#### Implementation of environment Board class
##### Attributes
---
```
state
winner
open
reward
```
##### Methods
---
    check_end
    play
    display
#### Implementation of agent class Agent, train Q-Learning or Sarsa algorithm
##### Attributes
---
```
epsilon
discount
alpha
algorithm
State 
q 
states 
players
```
##### Methods 
---
```
train
best_action
choose_action
add_state
qlearning
sarsa
play_o
play_x
```
##### Functions
---
```
main
```
### Board 
| Attribute | Description | Representation |
|---|---|---|
| state | current state of a game | 9 char string where "1"=x "2"=o "0"=empty<br />eg. board "120021102" represents board:<br /><pre>         x \| o \|<br />        -----------<br />           \| o \| x<br />        -----------<br />         x \|   \| o</pre>
| winner | winner at current game state | char representing winning player<br />x has won = "1"<br />o has won = "2"<br />tie game/no winner = "0" |
| open | all currently open positions on the board | list of ints representing indecies of state string<br />eg. [0,1,2] says only the top row is open|
| reward | reward for current board | int<br />no winner or tie = 0<br />x has won = 1<br />o has won = -1 |

| Method     | Description | Parameters | Function |
|---         |---          |---         |---       |
| \_\_init__ | initialization | self, state="000000000" | state is defaulted to the open board<br />set winner to None<br />set state to parameter<br />set reward to 0<br />check each index in the state and append each open position to open |
| check_end  | checks after each action to see if the winner has changed | self, player, action | checks all winning combinations for action (eg. if action is 0 check top row, left column, -1 diagonal)<br />if there is no winner and there are no more open spaces then game is tie <br />if x or o has won set reward |
| play       | takes action on board | self, action, player | insert player char at action index of state<br />remove the action index from open<br />call check_end for action and player |
| display    | print board to console | self | for each index is state, convert "0" to "_", "1" to "X", "2" to "O"<br />print board in 3x3 grid with corresponding index to the left as "{index}:" |













