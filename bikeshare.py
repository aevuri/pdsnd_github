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
    c=['chicago','new york city','washington']
    city = input("Which city would you like to choose data for chicago,new york city, washington: ")
    while city not in c:
        print("Incorrect city value. Please select from 3 cities - chicago, washington and new york city!")
        city = input("Which city would you like to choose data for chicago,new york city, washington: ")
        c=['chicago','new york city','washington']
        if city in c:
            print("This is a valid city!")        
            break        
    greeting = 'Thanks for Selecting the city {}!'.format(city)
    print(greeting)
        
    # get user input for month (all, january, february, ... , june)
    mth = ['all','january','february','march','april','may','june','july','august','september','october','november','december']
    month = input("Would you like to filter data by month, all, january, february, march, april, may, june:")
    #handle invalid inputs
    while month not in mth:
        print("Incorrect month value. Please select individual month name in lower case (or) all!")
        month = input("Would you like to filter data by month, all, january, february, march, april, may, june:")
        mth = ['all','january','february','march','april','may','june','july','august','september','october','november','december']
        if month in mth:
            print("This is a valid month!")        
            break
    greeting = 'Thanks for Selecting the month {}!'.format(month)
    print(greeting)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    d=['all','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = input("Would you like to filter data by days all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday:")
    #handle invalid inputs
    while day not in d:
        print("Incorrect day value. Please select individual day name with first letter capital value (or) all!")
        day = input("Would you like to filter data by days all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday:")
        d=['all','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        if day in d:
            print("This is a valid day!")        
            break
    greeting = 'Thanks for Selecting the day {}!'.format(day)
    print(greeting)
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
# load data file into a dataframe
    #Add Gender and Birth Year column with Null values in Washington csv to align with chicago and New york
    if city == 'washington' :
        df = pd.read_csv(CITY_DATA[city])
        df['Gender']=np.nan
        df['Birth Year']=np.nan
    else:
        df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]           
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    popular_month = df['month'].mode()
    print('Most common month:',popular_month)
    
    # display the most common day of week
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()
    print('Most common week:',popular_day)
        
    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # find the most commonly used start station
    start_station = df['Start Station'].mode()
    print('Most Commonly Used Start Station:', start_station)

    # display most commonly used end station
    # find the most commonly used start station
    end_station = df['End Station'].mode()
    print('Most Commonly Used End Station:', end_station)

    # display most frequent combination of start station and end station trip
    Common_Station = (df['Start Station']+df['End Station']).mode()
    print('Most frequent combination of start station and end station trip:',Common_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:',tot_travel_time)
    
    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time per Trip:',avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:',user_types)
     # Display gender counts
    gender_cnt = df['Gender'].value_counts()
    print('No.of Males and Females:',gender_cnt)    
    # Display earliest, most recent, and most common year of birth
    earliest_dob = df['Birth Year'].min()
    print('Earliest Year of Birth:',earliest_dob)
    recent_dob = df['Birth Year'].max()
    print('Recent Year of Birth:',recent_dob)
    mean_dob = df['Birth Year'].mean()
    print('Recent Year of Birth:',mean_dob)
    common_dob = df['Birth Year'].mode()
    print('Common Year of Birth:',common_dob)    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rawdata(df):
    """Displays first 5 rows in the dataframe based on the user input yes/no"""
    print('\nDisplay first 5 rows\n')
    start_time = time.time()
    
    #rawdata = input("Would you like to view the raw data (yes/no)?: ")
    for i in range(len(df)):
        rawdata = input("Would you like to view the raw data (yes/no)?: ")
        if rawdata == 'yes':
            print(df.iloc[i:i+5])
            continue
        elif rawdata == 'no':
            break
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
        display_rawdata(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
