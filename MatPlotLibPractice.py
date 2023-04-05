import matplotlib.pyplot as plt

t1=[1,2,3,4,5]
t2=[1,2,3,4,10]
t3=[2,3,4,5,11]

plt.figure()
plt.subplot(121)
plt.title('Scatterplot Greendots')
plt.plot(t1, t2, 'go')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,6)
plt.ylim(0,12)

plt.subplot(122)
plt.title('Scatterplot Bluestars')
plt.plot(t1, t3, 'b*')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,6)
plt.ylim(0,12)
plt.show()
