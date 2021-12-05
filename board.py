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