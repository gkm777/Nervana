import numpy
import statsmodels
import matplotlib.pyplot as plt
import ecdf
import sys

(school_name, scores) = ecdf.parseArguments()
e = statsmodels.distributions.empirical_distribution.ECDF(scores)
# X = numpy.linspace(min(scores), max(scores))
# print X
# y = ecdf(x)
# plt.step(x, y)
X = numpy.arange(0, 100, 0.1)
Y = e(X)

fig = plt.figure()
plt.step(X, Y)
fig.suptitle(school_name, fontsize=14, fontweight='bold')
plt.xlabel('mean test score')
plt.ylabel('ECDF')
plt.show()
