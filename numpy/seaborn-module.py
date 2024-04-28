import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns

# sns.displot([0, 1, 2, 3, 4, 5])
# sns.kdeplot([0, 1, 2, 3, 4, 5])
# plt.show()

# **Normal Distribution (Gaussian): It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.**
#loc - (Mean) where the peak of the bell exists.
#scale - (Standard Deviation) how flat the graph distribution should be.
#size - The shape of the returned array.

x = random.normal(size=(2, 3))
# sns.kdeplot(random.normal(size=1000))
# plt.show()

# **Binomial Distribution: It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.**
# n - number of trials.
#p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
#size - The shape of the returned array.

y = random.binomial(n=10, p=0.5, size=10)
print(y)
# sns.histplot(random.binomial(n=10, p=0.5, size=1000), kde=False)
# plt.show()

# **Poisson Distribution: It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?**
#lam - rate or known number of occurrences e.g. 2 for above problem.
#size - The shape of the returned array.

z = random.poisson(lam=2, size=10)
print(z)
# Visualization
# sns.histplot(random.poisson(lam=2, size=1000), kde=False)
# plt.show()

#**Uniform Distribution: Used to describe probability where every event has equal chances of occuring.**
#a - lower bound - default 0 .0.
#b - upper bound - default 1.0.
#size - The shape of the returned array.

p = random.uniform(size=(2,3))
print(p)
# sns.kdeplot(random.uniform(size=1000))
# plt.show()

#**Logistic Distribution: used to describe growth.**
#loc - mean, where the peak is. Default 0.
#scale - standard deviation, the flatness of distribution. Default 1.
#size - The shape of the returned array.

l = random.logistic(loc=1, scale=2, size=(2, 3))
print(l)
# sns.kdeplot(random.logistic(size=1000))
# plt.show()

#**Multinomial Distribution: It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.**
#n - number of possible outcomes (e.g. 6 for dice roll).
#pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
#size - The shape of the returned array.

m = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(m)

#**Exponential Distribution: used for describing time till next event e.g. failure/success etc**
#scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
#size - The shape of the returned array.

# sns.kdeplot(random.exponential(size=1000))
# plt.show()

#**Chisquare: used as a basis to verify the hypothesis.**
#df - (degree of freedom).
#size - The shape of the returned array.

# sns.kdeplot(random.chisquare(df=1, size=1000))
# plt.show()

#**Rayleigh Distribution :  used in signal processing**
# scale - (standard deviation) decides how flat the distribution will be default 1.0).
# size - The shape of the returned array.

# sns.kdeplot(random.rayleigh(scale=2, size=1000))
# plt.show()

#**Pareto Distribution: A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).**
# a - shape parameter
# size - The shape of the returned array.
# sns.histplot(random.pareto(a=2, size=1000))
# plt.show()

#**Zipf Distribution: used to sample data based on zipf's law.**
#a - distribution parameter.
#size - The shape of the returned array.
u = random.zipf(a=2, size=1000)
sns.histplot(u[u<10], kde=False)
plt.show()