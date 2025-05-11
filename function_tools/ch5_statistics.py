# Facts are stubborn, but statistics are more pliable.
# Mark Twain
# Statistics refers to the mathematics and techniques with which we understand data.

# But now you are faced with the problem of how to describe it.
# One obvious description of any data set is simply the data itself:
num_friends = [100, 49, 41, 40, 25,
                # ... and lots more
                ]

# For a small enough data set this might even be the best description. But for a larger data
# set, this is unwieldy and probably opaque. (Imagine staring at a list of 1 million numbers.)
# For that reason we use statistics to distill and communicate relevant features of our data.
# As a first approach you put the friend counts into a histogram using Counter and 
# plt.bar() (Figure 5-1):

from matplotlib import pyplot as plt
from collections import Counter

friend_counts = Counter(num_friends)
xs = range(101) # largest value is 100
ys = [friend_counts[x] for x in xs] # height is just # of friends
# plt.bar(xs, ys)
# plt.axis([0, 101, 0, 25])
# plt.title("Histogram of Friend Counts")
# plt.xlabel("# of friends")
# plt.ylabel("# of people")
# plt.show()


# Unfortunately, this chart is still too difficult to slip into conversations. So you start
# generating some statistics. Probably the simplest statistic is simply the number of data points:
num_points = len(num_friends) # 204

# You’re probably also interested in the largest and smallest values:
largest_value = max(num_friends) # 100
smallest_value = min(num_friends) # 1

# which are just special cases of wanting to know the values in specific positions:
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]                   # 1
second_smallest_value = sorted_values[1]            # 1
second_largest_value = sorted_values[-2]            # 49

# Central Tendencies
# Usually, we’ll want some notion of where our data is centered. Most commonly we’ll use
# the mean (or average), which is just the sum of the data divided by its count:
# this isn't right if you don't from __future__ import division
def mean(x):
    return sum(x) / len(x)
mean(num_friends)                                   # 7.333333



# Median
# which is the middle-most value (if the number of data points is odd) 
# or the average of the two middle-most values (if the number of data points is even).
# Notice that — unlike the mean — the median doesn’t depend on every value in your data.
# For example, if you make the largest point larger (or the smallest point smaller), the
# middle points remain unchanged, which means so does the median.

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
    # if odd, return the middle value
        return sorted_v[midpoint]
    else:
    # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

median(num_friends)                                     # 6.0


# A generalization of the median is the quantile, which represents the value less than which
# a certain percentile of the data lies. (The median represents the value less than which 50%
# of the data lies.)

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]
quantile(num_friends, 0.10) # 1
quantile(num_friends, 0.25) # 3
quantile(num_friends, 0.75) # 9
quantile(num_friends, 0.90) # 13


# Less commonly you might want to look at the mode, or most-common value[s]:
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

mode(num_friends) # 1 and 6


'''
Dispersion
Dispersion refers to measures of how spread out our data is. Typically they’re statistics for
which values near zero signify not spread out at all and for which large values (whatever
that means) signify very spread out. For instance, a very simple measure is the range,
which is just the difference between the largest and smallest elements:
'''
# "range" already means something in Python, so we'll use a different name
def data_range(x):
    return max(x) - min(x)

print(data_range(num_friends)) # 99


'''
Like the median, the range doesn’t really depend on the whole data set. A data set whose
points are all either 0 or 100 has the same range as a data set whose values are 0, 100, and
lots of 50s. But it seems like the first data set “should” be more spread out.
A more complex measure of dispersion is the variance, which is computed as:
'''

