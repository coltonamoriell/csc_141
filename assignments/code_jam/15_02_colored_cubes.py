import matplotlib.pyplot as plt

# Define x-values and calculate cubes
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# Apply a built-in style
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Create a scatter plot with a colormap (using Purples for cubes)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=10)

# Set chart title and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set the size of tick labels and plain notation
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')

# Display the plot
plt.show()