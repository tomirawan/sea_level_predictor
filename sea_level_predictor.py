import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df1 = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df1['Year'], df1['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lin1 = linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])
    x = np.arange(df1['Year'].min(), 2050, 1)
    y = lin1.intercept + lin1.slope*x
  
    fig, ax = plt.subplots(1,2, figsize=(15,6))
  
    ax[0].scatter(df1['Year'], df1['CSIRO Adjusted Sea Level'], label='original data')
    ax[0].plot(x,y, 'r', label='fitted line')
    ax[0].set_ylabel('Sea Level (inches)')
    ax[0].set_xlabel('Year')
    ax[0].legend()
  
    # Create second line of best fit
    df2 = df1.loc[df1['Year'] >= 2000]
    
    lin2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])

    x2 = np.arange(df2['Year'].min(), 2050, 1)
    y2 = lin2.intercept + lin2.slope*x2 
  
    # Add labels and title
    ax[1].plot(x2,y2, 'r', label='fitted line')
    ax[1].set_title('Rise in Sea Level')
    ax[1].set_xlabel('Year')
    ax[1].set_ylabel('Sea Level (inches)')
    ax[1].legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()