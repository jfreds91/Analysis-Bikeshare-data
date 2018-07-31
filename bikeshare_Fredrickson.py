import time
import pandas as pd
import os
import string as str
import numpy as np
import sys

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def getRuntime(someFunction):

    def timer(*args, **kwargs):

        t1 = time.time()
        out = someFunction(*args, **kwargs)
        t2 = time.time()
        hours, rem = divmod(t2-t1, 3600)
        minutes, seconds = divmod(rem, 60)
        print('This took {:02.0f}:{:02.0f}:{:05.2f}'.format(hours, minutes, seconds))
        print('-' * 40)

        return out

    return timer


def filter_df(df, month, day):
    """
    Filters the dataframe based on previous user input
    """

    #filter by month
    df = df.loc[df['month'] == month]

    #filter by day
    df = df.loc[df['day_of_week'] == day]

    return df


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter desired city (new york city, chicago, washington): ').lower()

        if city in CITY_DATA:
            break

        print('invalid input, try again.')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter desired month (january : june): ').lower()

        if month in months:
            month = months.index(month) + 1
            break

        print('invalid input, try again.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter desired day of the week: ').lower()

        if day in days:
            day = days.index(day)
            break

        print('invalid input, try again.')

    print('-' * 40)
    return city, month, day


@getRuntime
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    path = os.getcwd().replace('\\', '/') + '/'
    try:
        df = pd.read_csv(path + CITY_DATA.get(city))
    except FileNotFoundError as e:
        sys.exit('Error loading file. Make sure that the datafiles are in the working directory.')

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    if df is None:
        sys.exit('Error initializing dataframe. File was loaded successfully but load_data() failed.')

    return df


@getRuntime
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating Time Stats...\n')

    # display the most common month
    mode_month = df['month'].mode()[0]
    print('(Pre-filter) the most common month is {}'.format(mode_month))

    # apply filter
    df = filter_df(df, month, day)

    # display the most common day of week
    mode_day = df['day_of_week'].mode()[0]
    print('the most common day is {}'.format(mode_day))

    # display the most common start hour
    mode_hour = df['day_of_week'].mode()[0]
    print('the most common hour is {}'.format(mode_hour))

    return


@getRuntime
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating Station Stats...\n')

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    return


@getRuntime
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Duration Stats...\n')

    # display total travel time

    # display mean travel time

    return


@getRuntime
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
