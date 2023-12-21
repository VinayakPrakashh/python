import random

def rolldice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1,dice2
def diceprob(num_trials):
    same_value=0
    for i in range(num_trials):
        dice1,dice2 = rolldice()
        if dice1 ==dice2:
            same_value+=1
    probability = same_value/num_trials
    return probability
prob = diceprob(100)
print(prob)