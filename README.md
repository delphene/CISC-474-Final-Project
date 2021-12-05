## IMPLEMENTATION

### OVERVIEW
#### Implementation of environment class [Board](#board_h)
##### Attributes
---
[state](#state_p)<br>
[winner](#winner_p)<br>
[open](#open_p)<br>
[reward](#reward_p)<br>
##### Methods
---
[check_end](#check_end_m)<br>
[play](#play_m)<br>
[display](#display_m)<br>
#### Implementation of agent class [Agent](#agent_h)
##### Attributes
---
[epsilon](#epsilon_p)<br>
[discount](#discount_p)<br>
[alpha](#alpha_p)<br>
[algorithm](#algorithm_p)<br>
[State](#State_p)<br>
[q](#q_p)<br>
[states](#states_p)<br>
[players](#players_p)<br>
##### Methods 
---
[train](#board_h)<br>
[best_action](#board_h)<br>
[choose_action](#board_h)<br>
[add_state](#board_h)<br>
[qlearning](#board_h)<br>
[sarsa](#board_h)<br>
[play_o](#board_h)<br>
[play_x](#board_h)<br>
### Variables
---
| Variable | Description | Representation |
|---       |---          |---             |
| <a name="player_v">player<a> | represents X or O in code | char "1" for X and "2" for O |
| <a name="action_v">action<a> | represents a position on the board | integer refering to the index in the board state<br>eg. |
| <a name="state_v">state<a> | represents a board in any state | 9 char string where "1"=x "2"=o "0"=empty<br>eg. board "120021102" represents board:<br><pre>         x \| o \|<br>        -----------<br>           \| o \| x<br>        -----------<br>         x \|   \| o</pre>
### <a name="board_h">Board<a>
| Attribute | Description | Representation |
|---        |---          |---             |
| <a name="state_p">state<a> | current state of a game | represented as [state](#state_v) |
| <a name="winner_p">winner<a> | winner at current game state | char representing winning player<br>x has won = "1"<br>o has won = "2"<br>tie game/no winner = "0" |
| <a name="open_p">open<a> | all currently open positions on the board | list of ints representing indecies of state string<br>eg. [0,1,2] says only the top row is open|
| <a name="reward_p">reward<a> | reward for current board | int<br>no winner or tie = 0<br>x has won = 1<br>o has won = -1 |

| Method     | Description | Parameters | Function |
|---         |---          |---         |---       |
| \_\_init__ | initialization | self, state="000000000" | set [winner](#winner_p) to None<br>set [state](#state_v) to parameter<br>set [reward](#reward_p) to 0<br>check each index in the [state](#state_v) and append each open position to [open](#open) |
| <a name="check_end_m">check_end<a>  | checks after each action to see if the [winner](#winner_p) has changed | self, player, action | checks all winning combinations for [action](#action_v) (eg. if [action](#action_v) is 0 check top row, left column, -1 diagonal)<br>if [winner](#winner_p) is still None and there are no more [open](#open) spaces then game is tie <br>if x or o has won set reward |
| <a name="play_m">play<a>       | takes action on board | self, action, player | insert player char at [action](#action_v) index of state<br>remove the action index from open<br>call check_end for [action](#action_v) and player |
| <a name="display_m">display<a>    | print board to console | self | for each index in [state](#state_v), convert "0" to "_", "1" to "X", "2" to "O"<br>print board in 3x3 grid with corresponding index to the left as "{index}:" |
### <a name="agent_h">Agent<a>
| Attribute | Description | Representation |
|---        |---          |---             |
| <a name="epsilon_p">epsilon<a> | epsilon-greedy value<br>% of the time to choose non-greedy action | float |
| <a name="discount_p">discount<a> | forgetting rate for bellmen equation | float |
| <a name="alpha_p">alpha<a> | learning rate for bellmen equation | float |
| <a name="algorithm_p">algorithm<a> | which algorithm the agent will use | string of "qlearning" or "sarsa" |
| <a name="State_p">State<a> | holds the current [state/board][#board_h] | instance of class Board |
| <a name="q_p">q<a> | Q table values | dictionary of {state: {[action](#action_v): value}, ...}<br>accessed as q\[state][action] |
| <a name="states_p">states<a> | all visited states | set of [states](#state_v) |
| <a name="players_p">players<a> | used to determine which player is choosing actions and get their corresponding char ("1" or "2") | dictionary of {True:"1",False:"2"}<br>such that turns can be alternated by flipping a [boolean](#player_l) |

| Method     | Description | Parameters | Function |
|---         |---          |---         |---       |
| \_\_init\_\_    | initialization | self, epsilon, discount, alpha, algorithm="qlearning" | set attributes to parameters<br>initialize:<br>State = Board()<br>q = empty dictionary<br>states = empty set<br>add initial state from State using add\_state |
| <a name="train_m">train<a>         | call training function based on algorithm (attribute) | self, num_episodes | check algorithm (attribute)<br>if algorithm is "qlearning" call function qlearning<br>if not, call function sarsa |
| <a name="best_action_m">best_action<a>   | return a choice of best [action](#action_v) for current state | self, player | check [player](#player_l) boolean, if true [player](#player_v) is x<br>find max value for all actions at current state, append each [action](#action_v) that is equal to that value and return a choice from those actions<br>if false [player](#player_v) is o<br>find min value for all actions at current state, append each [action](#action_v) that is equal to that value and return a choice from those actions |
| <a name="choose_action_m">choose\_action<a> | choose [action](#action_v) based on [epsilon](#epsilon_p)-greedy | self, player | generate random float between 0 and 1<br>if the value is greater than [epsilon](#epsilon_p) return [best\_action](#best_action_m)<br>if the value is less than epsilon return random choice from [open](#open_p) positions on grid |
| <a name="add_state_m">add_state<a>     | add new state to states and q-table | self, state, open | add state to set [states](#states_p)<br>create new dictionary for [q](#q_p) with key=state<br>for each position in [open](#open_p) add dictionary at key=state with key=open ([action](#action_v)) and value 0.0 |
| <a name="qlearning_m">qlearning<a>     | call qlearning algorithm | self, num_episodes | local variable <a name="player_l">player<a> (boolean)<br>for each episode initialize [State](#States_p) to default Board value and set player to True (X)<br>while the [State](#States_p) has no [winner](#winner_p)<br>save a copy of the current state<br>choose an [action](#action_v) for the current player, take that [action](#action_v) on the board and negate [player](#player_l) boolean to continue with the next player<br>if the new state after the [action](#action_v) has not been seen, add it to [states](#states_p)<br> if there is no winner yet (includes no tie):<br>set expected value as [reward](#reward_p) + [discount](#discount_p) * [q](#q_p)\[value at new state\]\[action returned from [best action](#best_action_m) at new state\]<br>if there is a [winner](#winner_p) set expected to [reward](#reward_p)<br>update [q](#q_p)\[saved [state](#state_v) (previous state)\]\[[action](#action_v) taken\] += [alpha](#alpha_p) * \(expected value - [q](#q_p)\[saved [state](#state_v) (previous state)\]\[[action](#action_v) taken\]\)<br> |
| <a name="sarsa_m">sarsa<a>         | call sarsa algorithm | self, num_episodes |  |
| <a name="play_o_m">play\_o<a>       | play a game as o against the agent | self, num\_games |  |
| <a name="play_x_m">play\_x<a>        | play a game as x against the agent | self, num\_games |  |













