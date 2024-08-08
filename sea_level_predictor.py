import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    lr_1880_2012 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051, 1), lr_1880_2012.slope * range(1880, 2051, 1) + lr_1880_2012.intercept)

    lr_2000_2012 = linregress(df.query('Year >= 2000')['Year'], 
                              df.query('Year >= 2000')['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051, 1), lr_2000_2012.slope * range(2000, 2051, 1) + lr_2000_2012.intercept)

    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot();
