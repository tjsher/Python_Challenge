import matplotlib.pyplot as plt

def avg (array):
    sum = 0
    for i in array:
        sum += i
    return int(sum/len(array))

file = open("log.txt","r")
physics = []
free = []
active = []
while True:
    line = file.readline()
    if(not line):
        break
    physics.append(line[:-1])
    line = file.readline()
    free.append(line[:-1])
    line = file.readline()
    active.append(line[:-1])
x = [i for i in range(len(physics))]#time
free = [int(f) for f in free]#convert
active = [int(a) for a in active]#convert

free = [f/avg(free) for f in free]
active = [a/avg(active) for a in active]
physics = [1 for i in range(len(free))]
plt.figure()
p1, = plt.plot(x,active,color = 'green',label = 'active')
p2, = plt.plot(x,free,color = 'blue',label = 'free')
p3, = plt.plot(x,physics,color = 'red',label = 'physics')

plt.xlabel(u'time',fontsize=14)
plt.ylabel(u'size',fontsize=14)
plt.legend([p3,p2,p1],['physics','free','active'])
plt.show()
