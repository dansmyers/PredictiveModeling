"""
Examples of plotting
"""

# Import pandas, etc.
import pandas as pd
import numpy as np

# Import the pyplot library
from matplotlib import pyplot as plt

# Create an example dataframe: units per month
#
# Structure the data as a list of lists
units_per_month = [['Jan', 285], 
                   ['Feb', 267],
                   ['Mar', 312],
                   ['Apr', 434],
                   ['May', 459],
                   ['Jun', 427]]

# Turn the data lists into a Pandas dataframe
#
# The columns entry assigns names to each data column
df = pd.DataFrame(units_per_month, columns=['Month', 'Units'])

print(df)

### Make a bar chart
# Basic example of plotting one column against another

# plt.figure() creates a new plot
plt.figure()

# Create the plot
plt.bar(df['Month'], df['Units'])

# Label the axes and make a title for the graph
plt.xlabel('Month')
plt.ylabel('Units (thousands)')
plt.title('Units per month')

# Save the figure as a png image
plt.savefig('bar.png', bbox_inches='tight')

### Line plot
#
# Similar approach: make a plot of two columns against each other

# Key question: how does this compare to the
# previous plot? Is it clear?

plt.figure()
plt.plot(df['Month'], df['Units'])
plt.xlabel('Month')
plt.ylabel('Units (thousands)')
plt.title('Units per month')

# Adjust the range of the axes using ylim
#
# Y axis should always start at 0 unless you have a compelling
# reason not to do so
plt.ylim(0, 500)

plt.savefig('line.png', bbox_inches='tight')


### Make a scatter plot
#
# Useful when you want to show relationships
# between two quantitative variables, but not
# necessarily illustrate a trend

# Here's another example of creating a dataframe
#
# np.arange creates a range of numbers
data = {'X': np.arange(1, 26), 'Y': np.random.randint(low=1, high=50, size=25)}
df = pd.DataFrame(data)

plt.figure()
plt.scatter(df['X'], df['Y'])
plt.xlabel('Trial number')
plt.ylabel('Length (m)')
plt.title('Scatter Plot Example')
plt.savefig('scatter.png', bbox_inches='tight')


### Pie chart for proportions

classes = ['First', 'Second', 'Third']
sizes = [200, 300, 500]

plt.figure()

# Make the chart
# autopct automatically calculates the percentage
# of entries in each wedge
plt.pie(sizes, labels=classes, autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('pie.png', bbox_inches='tight')
