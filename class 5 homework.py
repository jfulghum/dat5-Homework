# -*- coding: utf-8 -*-
"""
Created on Sat Apr 04 20:44:17 2015

@author: johanna
"""

Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
to complete the following parts.  Please turn in your code for each part.  
Before each code chunk, give a brief description (one line) of what the code is
doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
the code output produces a plot or answers a question, give a brief
interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
group A is higher than the mean for group B which means X,Y,Z").
'''

'''
Part 1
Produce a plot that compares the mean mpg for the different numbers of cylinders.
'''

'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
auto = pd.read_csv ("https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt", sep = '|')

auto.shape
auto.head
auto.columns

'''
Part 2
Use a scatter matrix to explore relationshipspspspspsps between different numeric variables.
'''# pd.scatter_matrix(iris, c=iris.species_num)
auto.plot(kind='scatter', x = 'mpg', y = 'weight', alpha = .07) 
plt.show()
pd.scatter_matrix(auto, c=auto.mpg)
plt.show()



'''
Part 3
Use a plot to answer the following questions:
-Do heavier or lighter cars get better mpg?
Lighter!
-How are horsepower and displacement related?
-What does the distribution of acceleration look like?
-How is mpg spread for cars with different numbers of cylinders?
-Do cars made before or after 1975 get better average mpg? (Hint: You need to 
create a new column that encodes whether a year is before or after 1975.)
'''
auto.plot(kind='scatter', x = 'horsepower', y = 'displacement', alpha = .07) 
plt.show()
auto.acceleration.hist(by=auto.car_name, sharex=True)


oldie = pd.DataFrame()
oldie['before_1975'] = auto[(auto.model_year <= 1975)].groupby('car_name').mpg.mean()
print oldie
# horsey['low_power'] = auto[(auto.horsepower < 100)].groupby('model_year').mpg.mean() 