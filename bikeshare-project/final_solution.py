import pandas as pd
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city_list = CITY_DATA.keys()
    
    city = input('\nWould you like to see data for Chicago, New York City or Washington?\n')
    while city.lower() not in city_list:
        print("Please enter from the three cities mentioned")
        city = input('Would you like to see data for Chicago, New York City or Washington?\n')
        
    # get user input for month (all, january, february, ... , june)
    month_list = ["all","january","february","march","april","may","june"]
    month = input('\nWhich month would you like to filter for (all, january, february, ... ,june)?\n')
    while month.lower() not in month_list:
        print("Please enter month as mentioned above")
        month = input("Which month would you like to filter for?\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    day = input('\nWhich day would you like to see data for(all, Monday, Tuesday...)?\n')
    while day.lower() not in day_list:
        print("Please enter day as mentioned above.")
        day = input("Which day would you like to see data for(all, Monday, Tuesday...)?\n")

    print('-'*40)
    return city.lower(), month.lower(), day.lower()

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
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':    
        df = df[df['day_of_week'] == day.title()]
    return df


def raw_data(df):
    """
    Prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.
    """
    index=0
    i=0
    while i>=0:
        raw = input("Would you like to see individual trip data (yes or no):")
        if raw.lower() == "no":
            break    

        if raw.lower() == "yes":
            index = i
            for index, row in df.iterrows():
                if index<=(i+4):    
                    print(row)
                    index += 1
                
        i+=5

    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    pop = df['month'].mode()[0]
    print('\nMost common month is : ' + str(df['month'].mode()[0]))

    # display the most common day of week
    print('\nMost common day of week is : ' + str(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print('\nMost common start hour is : ' + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station is : ' + str(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most commonly used end station is : ' + str(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['se'] = df['Start Station'] + " and " + df['End Station']
    print('Most commonly used combination of start station and end station trip is : ' + df['se'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time (hours) is : ' + str(round(df["Trip Duration"].sum()/3600, 2)))

    # display mean travel time
    print('Mean travel time (minutes) is : ' + str(round(df["Trip Duration"].mean()/60, 2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if "User Type" in df.columns:
        print("Counts of user types are : \n" + str(df["User Type"].value_counts()))

    # Display counts of gender
    if "Gender" in df.columns:
        print("\nCounts of gender are : \n" + str(df["Gender"].value_counts()))

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("\nEarliest year of birth is : " + str(df["Birth Year"].min()))
        print("Most recent year of birth is : " + str(df["Birth Year"].max()))
        print("Most common year of birth is : " + str(df["Birth Year"].mode()[0]))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
