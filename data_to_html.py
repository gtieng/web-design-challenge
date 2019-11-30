#import library
import pandas as pd
import numpy as py

#read CSV
data = pd.read_csv('Resources/cities.csv')

#convert to html
data.to_html('data.html')