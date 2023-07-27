from P3AT4A16O import *

env = Pioneer()
q_table = np.loadtxt('q_table.txt')
print(q_table)
for i in range(1):
    state = env.reset()
    done = False
    
    while not done:
        action = np.argmax(q_table[state])
        #print(f'{state} {action} {q_table[state]}')
        next_state, reward, done, info = env.step(action) 
        state = next_state