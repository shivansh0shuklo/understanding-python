import random
greetings = ['hello','Hi','Hey','Hola']
colors = ['Red','black','green']
# value  = random.random()##between 0-1
# value  = random.uniform(1,10)## 1-10

#random integers
value = random.randint(1,6)


#random choices 
# value  = random.choice(greetings)


#random colors in list form
result = random.choices(colors,weights = [18,18,2],k=10)


#lsit random
deck = list(range(1,53))
random.shuffle(deck)##will shuffel the list atomatically
hand = random.sample(deck,k=5)##sample makes sure only uniqe values 


print(hand)