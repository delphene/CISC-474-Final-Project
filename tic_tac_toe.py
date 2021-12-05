import random
import time

class Board:
    def __init__(self, state="000000000"):
        self.winner     = None
        self.state      = state
        self.reward     = 0
        self.open       = []
        for i in range(len(state)):
            if state[i] == "0":
                self.open.append(i)

    def check_end(self, player, action):
        # set self.winner to player who has won
        if action == 0:
            if (self.state[0] == self.state[1] and self.state[1] == self.state[2]) or (self.state[0] == self.state[3] and self.state[3] == self.state[6]) or (self.state[0] == self.state[4] and self.state[4] == self.state[8]):
                self.winner = player
        elif action == 1:
            if (self.state[0] == self.state[1] and self.state[1] == self.state[2]) or (self.state[1] == self.state[4] and self.state[4] == self.state[7]):
                self.winner = player
        elif action == 2:
            if (self.state[0] == self.state[1] and self.state[1] == self.state[2]) or (self.state[2] == self.state[5] and self.state[5] == self.state[8]) or (self.state[2] == self.state[4] and self.state[4] == self.state[6]):
                self.winner = player
        elif action == 3:
            if (self.state[0] == self.state[3] and self.state[3] == self.state[6]) or (self.state[3] == self.state[4] and self.state[4] == self.state[5]):
                self.winner = player
        elif action == 4:
            if (self.state[3] == self.state[4] and self.state[4] == self.state[5]) or (self.state[1] == self.state[4] and self.state[4] == self.state[7]) or (self.state[0] == self.state[4] and self.state[4] == self.state[8]) or (self.state[2] == self.state[4] and self.state[4] == self.state[6]):
                self.winner = player
        elif action == 5:
            if (self.state[2] == self.state[5] and self.state[5] == self.state[8]) or (self.state[3] == self.state[4] and self.state[4] == self.state[5]):
                self.winner = player
        elif action == 6:
            if (self.state[6] == self.state[7] and self.state[7] == self.state[8]) or (self.state[0] == self.state[3] and self.state[3] == self.state[6]) or (self.state[2] == self.state[4] and self.state[4] == self.state[6]):
                self.winner = player
        elif action == 7:
            if (self.state[1] == self.state[4] and self.state[4] == self.state[7]) or (self.state[6] == self.state[7] and self.state[7] == self.state[8]):
                self.winner = player
        elif action == 8:
            if (self.state[2] == self.state[5] and self.state[5] == self.state[8]) or (self.state[6] == self.state[7] and self.state[7] == self.state[8]) or (self.state[0] == self.state[4] and self.state[4] == self.state[8]):
                self.winner = player
        # if no player has won and there are no more moves, reward is 0 and winner is "0"
        if self.winner == None and self.open == []:
            self.winner = "0"
            self.reward = 0
        # if x wins reward is 1
        if self.winner == "1":
            self.reward = 1
        # if y wins reward is -1
        elif self.winner == "2":
            self.reward = -1  

    def play(self, action, player):
        self.state = self.state[:action] + player + self.state[(action+1):] # update state
        self.open.remove(action)        # remove action from open places
        self.check_end(player, action)  # check if move is winning move

    def display(self):
        p_board = []
        for i in self.state:
            if i == "0":
                p_board.append("_")
            elif i == "1":
                p_board.append("X")
            elif i == "2":
                p_board.append("O")
        
        print("\nboard:\n\t0:",p_board[0],"\t1:",p_board[1],"\t2:",p_board[2])
        print(          "\t3:",p_board[3],"\t4:",p_board[4],"\t5:",p_board[5])
        print(          "\t6:",p_board[6],"\t7:",p_board[7],"\t8:",p_board[8],"\n")

class Agent:
    def __init__(self, epsilon, discount, alpha, algorithm="qlearning"):
        self.epsilon    = epsilon
        self.discount   = discount
        self.alpha      = alpha
        self.algorithm  = algorithm
        self.State      = Board()
        self.q          = {}
        self.states     = set()
        self.add_state(self.State.state, self.State.open)
        self.players    = {True:"1", False:"2"}

    def train(self, num_episodes):
        if self.algorithm == "qlearning":
            self.qlearning(num_episodes)
        else:
            self.sarsa(num_episodes)

    def best_action(self, player):
        if player: # if x playing
            best    = max(self.q[self.State.state].values())
            actions = [a for a, v in self.q[self.State.state].items() if v == best]
        else:       # if o playing
            best    = min(self.q[self.State.state].values())
            actions = [a for a, v in self.q[self.State.state].items() if v == best]
        return random.choice(actions)

    def choose_action(self, player):
        if random.random() > self.epsilon:
            return self.best_action(player)
        else:
            return random.choice(self.State.open)

    def add_state(self, state, open):
        # add new state to set of states
        self.states.add(state)
        # add each possible state-action pair to q with initial value 0.0 
        self.q[state] = {}
        for action in open:
            self.q[state][action] = 0.0

    def qlearning(self, num_episodes):
        episode = 0
        while episode < num_episodes:
            self.State = Board()
            player = True
            while self.State.winner == None:
                state = self.State.state                        # save initial state for update
                action = self.choose_action(player)             # player chooses action
                self.State.play(action, self.players[player])   # player takes action
                player = not player                             # current player has played, swap to other player for next move
                if self.State.state not in self.states:         # if new state add to set of states and q table
                    self.add_state(self.State.state, self.State.open)
                if self.State.winner == None:                   # if no winner then get Q(S',argmax/argmin(a)) value
                    expected = self.State.reward + (self.discount * self.q[self.State.state][self.best_action(player)])
                else:
                    expected = self.State.reward
                self.q[state][action] += self.alpha * (expected - self.q[state][action])
            episode += 1

    def sarsa(self, num_episodes):
        episode = 0
        while episode < num_episodes:
            self.State = Board()
            player = True
            action = self.choose_action(player)
            while self.State.winner == None:
                state = self.State.state
                self.State.play(action, self.players[player])
                player = not player
                if self.State.state not in self.states:         # if new state add to set of states and q table
                    self.add_state(self.State.state, self.State.open)
                if self.State.winner == None:                   # if no winner then get Q(S',A') value
                    next_action = self.choose_action(player)
                    expected = self.State.reward + (self.discount * self.q[self.State.state][next_action])
                else:
                    expected = self.State.reward
                # update state action value
                self.q[state][action] += self.alpha * (expected - self.q[state][action])
                # update action
                action = next_action
            episode += 1

    def play_o(self, num_games):
        game = 0
        while game < num_games:
            self.State = Board()
            x = True
            print()
            while True:
                if len(self.State.open) < 1:
                    print("TIE GAME\n")
                    break
                if x:
                    move = int(self.best_action(x))
                    print("Computer X plays:", move)
                    self.State.play(move, "1")
                    if self.State.winner == "1":
                        self.State.display()
                        print("X WINS!\n")
                        break
                else:
                    while True:
                        print("Your move:",end=' ')
                        move = int(input())
                        if move in self.State.open:
                            break
                    self.State.play(move, "2")
                    if self.State.winner == "2":
                        self.State.display()
                        print("O WINS!\n")
                        break
                x = not x
                self.State.display()
            game += 1

    def play_x(self, num_games):
        game = 0
        while game < num_games:
            self.State = Board()
            x = True
            print()
            while True:
                if x:
                    while True:
                        print("Your move:",end=' ')
                        move = int(input())
                        if move in self.State.open:
                            break
                    self.State.play(move, "1")
                    if self.State.winner == "1":
                        self.State.display()
                        print("X WINS!\n")
                        break
                else:
                    move = int(self.best_action(x))
                    print("Computer X plays:", move)
                    self.State.play(move, "2")
                    if self.State.winner == "2":
                        self.State.display()
                        print("O WINS!\n")
                        break
                if len(self.State.open) < 1:
                    self.State.display()
                    print("TIE GAME\n")
                    break
                x = not x
                self.State.display()
            game += 1

def main():
    discount = 1.0
    epsilon = 0.3
    alpha = 0.5
    algorithm = "qlearning"
    num_episodes = 10000000

    s = time.time()
    ai = Agent(epsilon, discount, alpha, algorithm)
    ai.train(num_episodes)
    print('training took', round(time.time()-s,2), 'seconds')

    while True:
        print("your letter:",end='')
        player = input()
        if player == "o":
            ai.play_o(1)
        elif player == "x":
            ai.play_x(1)
        else:
            print('please enter x or o')

main()