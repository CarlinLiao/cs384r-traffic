from dta.dta_env import dta_env

ni = 60//5
env = dta_env(interval=60*5,numIntervals = ni)
for i in range(30):
    # env = dta_env(interval=60*5, numIntervals=ni)
    with open(""+str(i)+".txt",'w') as outfile:
        
        state = env.reset()
        for _ in range(ni):
            _, rew, _ = env.step()
            outfile.write(str(rew)+"\n")
            outfile.flush()