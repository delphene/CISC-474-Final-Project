import time
import agent

def main():
    discount = 1.0
    epsilon = 0.3
    alpha = 0.5
    algorithm = "qlearning"
    num_episodes = 1000000

    s = time.time()
    ai = agent.Agent(epsilon, discount, alpha, algorithm)
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