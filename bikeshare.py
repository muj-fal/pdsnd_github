import time
import pandas as pd
import numpy as np

#22/5/2020 project 3 
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
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york city','washington']
    city = input("enter a city name:  \n").lower()
    while True :
        if city not in cities:
            print("wrong city")
            city = input("enter a city name: \n").lower()
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    Months = ['january','feburary','march','april','may' ,'june']
    month = input('enter the month \n').lower()
    while True:
       if month not in Months:
             print('wrong month ')
             month = input('enter the month \n').lower()
       else :
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    Days = ['monday','tuesday','wensday','thursday','friday','satarday','sunday']
    day = input('enter the day \n').lower()
    while True:
        if day not in Days:
                print('wrong day ')
                day = input('enter the day \n').lower()
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
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        Months = ['january','feburary','march','april','may' ,'june']
        month =  Months.index(month) + 1
        df = df[ df['month'] == month ]
        
    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('the most common month is ',common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print('the most common day of the week is ',common_day)

    # TO DO: display the most common start hour
    comm_hour =df['hour'].value_counts().idxmax()
    print('the most common start hour is ',comm_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].value_counts().idxmax()
    print('the most common start station is ',common_start,'/n')
    

    # TO DO: display most commonly used end station
    common_end = df['End Station'].value_counts().idxmax()
    print('the most common end station is ',common_end,'/n')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_end_station']=df['Start Station']+','+df['End Station']
    Start_end_station= df['Start_end_station'].mode()[0]
    print('the most common combanation is ',Start_end_station,'/n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
  
    print('Total travel time is ',total_time ,'\n') 
    

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('average travel time is ',mean_time,'\n')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Types=df['User Type'].value_counts()
    print('Type:\n',Types)

    # TO DO: Display counts of gender
    try:
        gender=df['Gender'].value_counts()
        print('Type:\n',gender )
    except KeyError:
        print('no data\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=df['Birth Year'].min()
        print('earliest year of birth : ',earliest,'\n')
    except KeyError:
        print('no data\n')
    try:
        most_recent = df['Birth Year'].max()
        print('most recent year of birth : ',most_recent,'\n')
    except KeyError:
        print('no data\n')
    try:
        most_common_year=df['Birth Year'].value_counts().idxmax()
        print('most common year of birth : ',most_common_year,'\n')
    except KeyError:
        print('no data\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def View_data(df):
    
    while True:
        i = 0
        choice=input('enter yes to show data or no to not show data \n')
        if choice =='yes':
                print(df.iloc[i:i+5])
                i +=5
                
        else:
                break

        return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        View_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	      main()