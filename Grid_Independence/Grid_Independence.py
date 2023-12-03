import matplotlib.pyplot as plt

elements = [6397,8711,14708,25879,28942,33313,40874]
avg_U = [0.950563,0.950541,0.95232,0.950374,0.950348,0.950333,0.950323]

plt.plot(elements,avg_U)
plt.title('Grid Independance Analysis')
plt.xlabel('Number of Grid Elements')
plt.ylabel('Average Velocity')
plt.grid()
plt.show()
