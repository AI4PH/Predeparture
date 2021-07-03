import numpy as np
import time
#Activity generator
#Enter an activity
#Outputs a random answer from a list

def randomActivity(a):
    np.random.seed(int(time.time()))
    num = np.random.randint(0, 6)
    alist = options[a]
    return alist[num]


options={'food':['sushi', 'pizza', 'tacos', 'dim sum', 'burgers', 'pasta'],
    'places':['Singapore', 'Las Vegas', 'Mexico City', 'Beijing', 'Amsterdam', 'Italy'],
    'sports':['basketball', 'baseball', 'hockey', 'lacrosse', 'soccer', 'tennis']
}

print("Welcome to the activity generator! What would you like to do today?")
activity = ""
while activity not in ('eat', 'travel', 'play a sport'):
    activity = input("Please input either 'Eat', 'Travel', or 'Play a sport'\n").lower()
    if activity == "eat" :
        print("You should eat " + randomActivity("food") + "!")
    elif activity == "travel" :
         print("You should go to " + randomActivity("places") + "!")
    elif activity == "play a sport" :
         print("You should play " + randomActivity("sports") + "!")
    else :
        print("Invalid input!")