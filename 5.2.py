import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [5, 3, 4, 6, 2]

# Create subplots (1 row, 3 columns)
plt.figure(figsize=(10, 4))

# Line plot
plt.subplot(1, 3, 1)
plt.plot(x, y1, color='blue')
plt.title('Line Plot')

# Scatter plot
plt.subplot(1, 3, 2)
plt.scatter(x, y2, color='red')
plt.title('Scatter Plot')

# Bar plot
plt.subplot(1, 3, 3)
plt.bar(x, y3, color='green')
plt.title('Bar Plot')

# Show all plots together
plt.show()
