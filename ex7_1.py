import random

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
#results = [(ali, homa), (shahin, neda) , …]

results = []
length = len(boys)
x=0

while x < length:
    i = random.randint(0 , len(boys)-1)
    j = random.randint(0 , len(girls)-1)
    choice_boy = boys[i]
    choice_girl = girls[j]

    results.append(choice_boy + ' & ' + choice_girl)
    boys.remove(choice_boy)
    girls.remove(choice_girl)
    x += 1

for r in results:
    print(r)