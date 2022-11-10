import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

list_of_cities = ['chicago','new york city','washington']
list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December','All']
list_of_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Pick one of following cities: Washington, Chicago or New York City. \n')).lower()
        if city not in list_of_cities:
            print('That city does not exist, please choose one of: Washington, Chicago or New York City.')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Is there any month you want to filter by? If yes, then type out the selected month. If not, type in all\n')).title()
        if month not in list_of_months:
            print('That month does not exist, please choose a valid month!')
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Is there any day you want to filter by? If yes, then type out the selected day. If not, type in all\n')).title()
        if day not in list_of_days:
            print('That day does not exist, please choose a valid day!')
        else:
            break

    print('-'*40)
    return city, month, day


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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'All':
        month = list_of_months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('This is the most common month: {}'.format(list_of_months[common_month-1]))

    # TO DO: display the most common day of week
    print('This is the most common day: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_start = df['Start Station'].mode()[0]
    print('This is the most commonly used start station: ', most_commonly_start)

    # TO DO: display most commonly used end station
    most_commonly_end = df['End Station'].mode()[0]
    print('This is the most commonly used end station: ', most_commonly_end)

    # TO DO: display most frequent combination of start station and end station trip
    group_comb = df.groupby(['Start Station', 'End Station'])
    most_freq_comb_station = group_comb.size().sort_values(ascending=False).head(1)

    print('The trip which is the most frequent combination of start station & end stationn is: ', most_freq_comb_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_duration = df['Trip Duration'].sum()
    print('This is the total travel time: ', total_travel_duration)

    # TO DO: display mean travel time
    mean_travel_duration = df['Trip Duration'].mean()
    print('This is the mean travel time: ', mean_travel_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('This is the User Types in the dataset: ', counts_of_user_types)

    # TO DO: Display counts of gender
    if('Gender' in df):
        print('This are the genders for \n{}'.format(df['Gender'].value_counts()))
    else:
        print('There is no gender data for that city')

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]

        print('\nThis is the earliest year of birth: {}\n'.format(earliest_yob))
        print('\nThis is the most recent year of birth: {}\n'.format(most_recent_yob))
        print('\nThis is the most common year of birth: {}\n'.format(most_common_yob))

    else:
        print('There is no birth of year data for that city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_the_data(df):
    beginning = 0
    while True:
        choice_of_view = input("Are you intrested in see the raw data? Enter either Yes or No.\n").lower()
        if choice_of_view == "Yes":
            print(df.iloc[beginning : beginning + 6])
            beginning += 6
        elif choice_of_view =="No":
            break
        else:
            print("You need to enter either Yes or No")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_the_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
