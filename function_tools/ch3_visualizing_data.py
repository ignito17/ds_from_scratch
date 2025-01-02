# A fundamental part of the data scientist’s toolkit is data visualization. 
# Although it is very easy to create visualizations, it’s much harder to produce good ones.

# There are two primary uses for data visualization:
# To explore data
# To communicate data

# In this chapter, 
# we will concentrate on building the skills that you’ll need to start exploring
# your own data and to produce the visualizations we’ll be using throughout the rest of the book

# In particular, we will be using the matplotlib.pyplot module. In its simplest use, pyplot
# maintains an internal state in which you build up a visualization step by step. Once you’re
# done, you can save it (with savefig()) or display it (with show()).

from matplotlib import pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# add a title
plt.title("Nominal GDP")
# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()