import datetime
import pandas as pd
 
def automated_strategy(data, window1, window2):
    # Calculating SMA
    short_rolling = data.rolling(window=window1).mean()
    long_rolling = data.rolling(window=window2).mean()
 
    # Creating signals
    data['short_mavg'] = short_rolling
    data['long_mavg'] = long_rolling
    data['signal'] = 0.0
    data['signal'][window1:] = np.where(data['short_mavg'][window1:] 
                        > data['long_mavg'][window1:], 1.0, 0.0)   
 
    # Generating trading orders
    data['positions'] = data['signal'].diff()
 
    # Initializing the plot figure
    fig = plt.figure()
 
     # Plotting SMA
    ax1 = fig.add_subplot(111, ylabel='Price in $')
    data[['Close', 'short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
 
    # Plotting the trading orders
    ax2 = fig.add_subplot(111, ylabel='Order', yticklabels=[])
    data['positions'].plot(ax=ax2, lw=2., color='r')
 
    # Plotting the trading orders
    ax3 = fig.add_subplot(111, ylabel='P&L', yticklabels=[])
    data['p&l'].plot(ax=ax3, lw=2., color='g')
 
    # Show the plot
    plt.show()