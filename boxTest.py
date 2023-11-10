import matplotlib.pyplot as plt

# Create a circle without fill
circle = plt.Circle((0, 0), 0.5, color='r', fill=False)

# Set up the plot
fig, ax = plt.subplots()
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('AU')
plt.ylabel('AU')
plt.grid(linestyle='-')
ax.set_aspect(1)
ax.add_artist(circle)
plt.title('Habitable Zone Around the Sun', fontsize=8)

# Display the plot
plt.show()
