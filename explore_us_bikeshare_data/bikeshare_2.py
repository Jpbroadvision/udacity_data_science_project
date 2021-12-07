import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def switch_to_number(provided_int, marker):
    """Uses this method when the user decides to provide an integer or a number instead of a string

    Args:
        provided_int (int): The number the user enters
        marker (str): The marker that represents (city, month, day) numbers. This is used to switch between selections

    Returns:
       selected_value (str): The corresponding name of the city according to the order the cities are presented to the user
    """
    # Switches to this condition if the user is providing a number for city
    if marker == "city":
        SELECTED_NAME = {1: 'chicago',
                2: 'new york city',
                3:'washington' }
    
    # Switches to this condition if the user is providing a number for month
    elif marker == "month":
        SELECTED_NAME = {0: 'all',
             1: 'january',
              2:'february',
              3: 'march',
             4: 'april',
              5:'may', 
              6: 'june'
              }
    # Switches to this condition if the user is providing a number for day
    elif marker == "day":
        SELECTED_NAME = {0: 'all',
             1: 'monday',
              2:'tuesday',
              3: 'wednesday',
             4: 'thursday',
              5:'friday',
              6: 'saturday',
             7: 'sunday'}
        
    selected_value = SELECTED_NAME[provided_int]
    return selected_value

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
    try: 
        city = (input('Enter name of city (chicago, new york city, washington): ').strip()).lower()
    except:
        int_city = int(input('Oops!!. There may be a typo in there. You can also enter numbers to 1 for chicago, 2 for new york city, 3 for washington: '))
        city = switch_to_number(int_city, 'city')
    finally:
        print("Sorry. You must enter valid charaters. Exiting now...")
        # return
    print(f"Great, You selected {city}")
    # get user input for month (all, january, february, ... , june)
    try: 
        month = (input('Enter a month. (all, january, february, ... , june): ').strip()).lower()
    except:
        int_month = int(input('Oops!!. There may be a typo in there. You use can enter 0, 1, 2, 3, 4, 5 or 6 for (all, january, february, ... , june) respectively: '))
        month = switch_to_number(int_month, 'month')
    finally:
        print("Sorry. You must enter valid charaters. Exiting now...")
    
    print(f"You are almost there. You selected {month}")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    try: 
        day = (input('Enter a day in a week (all, monday, tuesday, ... sunday): ').strip()).lower()
    except:
        int_day = int(input('Oops!!. There may be a typo in there. You use can enter 0, 1, 2, 3, 4, 5, 6 or 7 for (all, monday, tuesday, ... sunday) respectively: '))
        day = switch_to_number(int_day, 'day')
    finally:
        print("Sorry. You must enter valid charaters. Exiting now...")
    

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
    city_file = CITY_DATA[city]
    read_city = pd.read_csv(city_file)
    read_city['Start Time'] = pd.to_datetime(read_city['Start Time'])

    # create a month column
    read_city['month'] = read_city['Start Time'].dt.month
    # create day of week coulmn
    read_city['day_of_week'] = read_city['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_2Num = months.index(month) + 1
    
        # filter by month to create the new dataframe
        read_city = read_city[read_city['month'] == month_2Num]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        read_city = read_city[read_city['day_of_week'] == day.title()]

    return read_city


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    

    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    # while True:
    city, month, day = get_filters()
    df = load_data(city, month, day)

        # time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        # restart = input('\nWould you like to restart? Enter yes or no.\n')
        # if restart.lower() != 'yes':
        #     break


if __name__ == "__main__":
	main()
