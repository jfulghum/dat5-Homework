# -*- coding: utf-8 -*-
"""
Created on Sat Apr 04 22:49:41 2015

@author: johanna
"""

##########################################
#############    Homework    #############
##########################################
'''
Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.csv) 
to complete the following parts.  Please turn in your code for each part.  
Before each code chunk, give a brief description (one line) of what the code is
doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
the code output produces a plot or answers a question, give a brief
interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
group A is higher than the mean for group B which means X,Y,Z").
'''

'''
Part 1
Load the data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
into a DataFrame.  Try looking at the "head" of the file in the command line
to see how the file is delimited and how to load it.
Note:  You do not need to turn in any command line code you may use.
'''

import pandas as pd # pandas is a library that makes all the data handling easier 
import matplotlib.pyplot as plt
import numpy as np

# if they aren't already in there do this: columns = ["mpg","cylinders","displacement","horsepower","weight", "acceleration", "model year", "origin", "car name"]
auto = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep = '|')
# you do have to put sep = '|' b/c its not a csv file

'''
Part 2
Get familiar with the data.  Answer the following questions:
- What is the shape of the data?  How many rows and columns are there?
- What variables are available?
- What are the ranges for the values in each numeric column?
- What is the average value for each column?  Does that differ significantly
  from the median? (median is the 50%)
'''
auto.shape # there are (392 rows , 5 columns)
auto.values # um by that do you mean column? 'weight', 'acceleration', 'model_year', 'origin', 'car_name'
auto.columns
auto.head()
auto.max()

auto.weight.max()
auto.describe()
auto.head()

#Part 3
#Use the data to answer the following questions:
# Which 5 cars get the best gas mileage?  
auto.groupby('mpg').car_name.max().tail()
auto.sort_index(by='mpg')(0:5)

# Which 5 cars with more than 4 cylinders get the best gas mileage?
auto[auto.cylinders > 4].sort_index(by='mpg')[['mpg','car_name']].tail()

# Which 5 cars get the worst gas mileage? 
auto.groupby('mpg').car_name.max().head()

# Which 5 cars with 4 or fewer cylinders get the worst gas mileage?
auto[auto.cylinders > 4].sort_index(by='mpg')[['mpg','car_name']].head()


auto.columns
auto.groupby('mpg').car_name.min()  #hi 1200d, chevy c20,  chevrolet impala,  buick electra 225 custom, amc ambassador brougham

'''
Part 4
Use groupby and aggregations to explore the relationships 
between mpg and the other variables.  Which variables seem to have the greatest
effect on mpg?
Some examples of things you might want to look at are:
- What is the mean mpg for cars for each number of cylindres (i.e. 3 cylinders,
  4 cylinders, 5 cylinders, etc)?
- Did mpg rise or fall over the years contained in this dataset? 
- What is the mpg for the group of lighter cars vs the group of heaver cars?
Note: Be creative in the ways in which you divide up the data.  You are trying
to create segments of the data using logical filters and comparing the mpg
for each segment of the data.
'''
auto.groupby('cylinders').mpg.max()
auto.groupby('model_year').mpg.mean() 
auto.groupby('weight').mpg.mean()
