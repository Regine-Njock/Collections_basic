colors = ['cyan', 'magenta', 'green', 'yellow', 'black ', 'white']
colors = [i for i in colors if i not in ('green', 'white')] #using list comprehension

print(*colors, sep='\n')