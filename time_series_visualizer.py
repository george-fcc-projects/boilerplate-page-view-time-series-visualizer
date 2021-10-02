import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(filepath_or_buffer='fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # print(df)
    # Draw line plot
    fig, ax = plt.subplots(figsize=[15, 5])
    ax.xaxis_date()
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    locator = mdates.AutoDateLocator(minticks=8, maxticks=9, interval_multiples=False)
    locator.intervald[1] = [6]
    ax.xaxis.set_major_locator(locator)

    fig = sns.lineplot(data=df, x='date', y='value').set_title(
        'Daily freeCodeCamp Forum Page Views 5/2016-12/2019').figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    monthDict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

    df_bar = df.copy()
    df_bar = df_bar.groupby(by=[df_bar.index.year, df_bar.index.month])
    # print(df_bar.groups)
    df_bar = df_bar.mean()
    # print(df_bar.index)
    df_bar.reset_index(level=1, inplace=True)
    # print(df_bar)
    # Draw bar plot
    fig, ax = plt.subplots(figsize=[10, 10])

    barplot = sns.barplot(data=df_bar, y='value', hue='date', x=df_bar.index, ax=ax)

    barplot.set_xlabel('Years')
    barplot.set_ylabel('Average Page Views')
    barplot.legend(labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December'])
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # print(df_box)

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize=[28.8, 10.8])

    plot1 = sns.boxplot(data=df_box, y='value', x='year', ax=ax[0])
    plot2 = sns.boxplot(data=df_box, y='value', x='month', ax=ax[1], order=month_order)

    plot1.set_xlabel('Year')
    plot2.set_xlabel('Month')
    plot1.set_ylabel('Page Views')
    plot2.set_ylabel('Page Views')
    plot1.set_title('Year-wise Box Plot (Trend)')
    plot2.set_title('Month-wise Box Plot (Seasonality)')





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
