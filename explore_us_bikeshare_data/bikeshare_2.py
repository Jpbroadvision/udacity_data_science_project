import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'explore_us_bikeshare_data/chicago.csv',
             'new york city': 'explore_us_bikeshare_data/new_york_city.csv',
             'washington': 'explore_us_bikeshare_data/washington.csv'}

# All available city names
CITIES_ONLY = ['chicago', 'new york city', 'washington']
# All available months 
MONTHS_ONLY = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
# all available days
WEEK_DAYS_ONLY = ['all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']

def switch_to_number(provided_int, marker):
    """Uses this method when the user decides to provide an integer or a number instead of a string

    Args:
        provided_int (int): The number the user enters
        marker (str): The marker that represents (city, month, day). This is used to switch between selections

    Returns:
       selected_value (str): The corresponding name of the city according to the order the cities are presented to the user
    """
    # Switches to this condition if the user is providing a number for city
    if marker == "city":
        SELECTED_NAME = {
            1: 'chicago',
            2: 'new york city',
            3: 'washington'
        }

    # Switches to this condition if the user is providing a number for month
    elif marker == "month":
        SELECTED_NAME = {
            0: 'all',
            1: 'january',
            2: 'february',
            3: 'march',
            4: 'april',
            5: 'may',
            6: 'june'
        }
    # Switches to this condition if the user is providing a number for day
    elif marker == "day":
        SELECTED_NAME = {
            0: 'all',
            1: 'monday',
            2: 'tuesday',
            3: 'wednesday',
            4: 'thursday',
            5: 'friday',
            6: 'saturday',
            7: 'sunday'
        }

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
    while True:
        try:
            print()
            city = (input('Enter name of city (chicago, new york city, washington):>> ').strip()).lower()
            # Get the name of the city the user entered and check whether it exist
            response = city in CITIES_ONLY
            # If the responses exist, then pass
            if response == True:
                break
            # If not...
            elif response == False:
                try:
                    # We alert the user to enter a number or an integer between 1, 2 or 3 respectively
                    print()
                    int_city = int(input(
                    'Oops!!. There may be a typo in there. You can also enter numbers such as 1 for chicago, 2 for new york city, 3 for washington:>> '))
                    # Check whether what the user entered is a number, may raise KeyError 
                    city = switch_to_number(int_city, 'city')
                    break
                except KeyError:
                    print()
                    print("The input provided is not available. If it is a number you provided, select between 1, 2 or 3")
                    print()
            
        except ValueError:
            print()
            print(":) NOOOOOOOOO!!!. Try again.  Enter a valid city name or number to continue...")
        except KeyboardInterrupt:
            return
    print()
    print(f"GREAT, YOU SELECTED {city}")
        # get user input for month (all, january, february, ... , june)
    while True:
        try:
            print()
            month = (
                input('Enter a month (all, january, february, ... , june):>> ').strip()).lower()
            # Get the name of the month the user entered and check whether it exist
            response = month in MONTHS_ONLY
            # If the responses exist, then pass
            if response == True:
                break
            # If not...
            elif response == False:
                try:
                    # We alert the user to enter a number or an integer between 0, 1, 2, 3, 4, 5 or 6 respectively
                    print()
                    int_month = int(input(
                        'Oops!!. There may be a typo in there. You use can enter 0, 1, 2, 3, 4, 5 or 6 for (all, january, february, ... , june) respectively:>> '))
                    # Check whether what the user entered is a number, may raise KeyError 
                    month = switch_to_number(int_month, 'month')
                    break
                except KeyError:
                    print()
                    print("The input provided is not available. If it is a number you provided, select between 0, 1, 2, 3, 4, 5 or 6 for (all, january, february, ... , june)")
                    print()
        except ValueError:
            print()
            print(":) NOOOOOOOOO!!!  Try again. Enter a valid month name or number to continue...")
        except KeyboardInterrupt:
            return
    print()  
    print(f"YOU ARE ALMOST THERE. YOU SELECTED {month}")
        

    while True:
        # get user input for day of week (all, monday, tuesday, ... sunday)
        try:
            day = (input('Enter a day in a week (all, monday, tuesday, ... sunday):>> ').strip()).lower()
            response = day in WEEK_DAYS_ONLY
            # If the responses exist, then pass
            if response == True:
                break
            # If not...
            elif response == False:
                try:
                    # We alert the user to enter a number or an integer between 0, 1, 2, 3, 4, 5, 6 or 7 for (all, monday, tuesday, ... sunday) respectively
                    print()
                    int_day = int(input('Oops!!. There may be a typo in there. \
                        You use can enter 0, 1, 2, 3, 4, 5, 6 or 7 for (all, monday, tuesday, ... sunday) respectively:>> '))
                    # Check whether what the user entered is a number, may raise KeyError 
                    day = switch_to_number(int_day, 'day')
                    break
                except KeyError:
                    print()
                    print("The input provided is not available. If it is a number you provided, select between 0, 1, 2, 3, 4, 5, 6 or 7 for (all, monday, tuesday, ... sunday)")
                    print()
        except ValueError:
            print()
            print(":) NOOOOOOOOO!!!  Try again. Enter a valid day name or number to continue...")
        except KeyboardInterrupt:
            return
    print()
    print(f"EXECELLENT!. YOU ARE ON TRACK. YOU SELECTED {day}")
    
    print('-'*40)
    print(f"YOUR SEARCH QUERIES ARE CITY: {city}, MONTH: {month} and DAY: {day} ")
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
    read_city['day_of_week'] = read_city['Start Time'].dt.day_name()
    # Create hour column
    read_city['hour'] = read_city['Start Time'].dt.hour
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


def time_stats(read_city):
    """Displays statistics on the most frequent times of travel.
    
    Args:
        (DataFrame) read_city - Pandas DataFrame containing city data with filters.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = read_city['month'].mode()[0]
    print()
    print(f'\nBase on your Selections. The most common month of travel is: {MONTHS_ONLY[common_month].title()}')

    # display the most common day of week
    common_day = read_city['day_of_week'].mode()[0]
    print()
    print(f'\nBase on your Selections. The most common day of the week used of travel is: {common_day}')
    # display the most common start hour
    common_hour = read_city['hour'].mode()[0]
    print()
    print(f'\nBase on your Selections. The most common hour is: {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(read_city):
    """ Displays statistics on the most popular stations and trip.

    Args:
        (DataFrame) read_city - Pandas DataFrame containing city data with filters.

    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_use_start_station = read_city['Start Station'].mode()[0]
    print()
    print(f"The most commonly used start station from the given selections is:  {common_use_start_station}")
    # display most commonly used end station
    common_use_end_station = read_city['End Station'].mode()[0]
    print()
    print(f"The most commonly used end station from the given fitered data is: {common_use_end_station}")
    # display most frequent combination of start station and end station trip
    start_end_station = (read_city['Start Station'] + '||' + read_city['End Station']).mode()[0]
    print()
    print(f"The most frequent combination of start station and end station trip is :  {start_end_station.split('||')}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(read_city):
    """Displays statistics on the total and average trip duration.
    
    Args:
        (DataFrame) read_city - Pandas DataFrame containing city data with filters.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = read_city['Trip Duration'].sum()
    print()
    print(f"The total travel time selections is: {total_travel_time}")

    # display mean travel time
    mean_travel_time = read_city['Trip Duration'].mean()
    print()
    print(f"The mean travel time selections is: {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(read_city, city):
    """Displays statistics on bikeshare users.
    
    Args:
        (DataFrame) read_city - Pandas DataFrame containing city data with filters.

    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = read_city['User Type'].value_counts()
    print()
    print(f"The total counts of user types from selections is:\n{count_user_types}")
    # Display counts of gender
    if 'Gender' in read_city.columns:
        count_gender = read_city['Gender'].value_counts()
        print()
        print(f"The count of user gender from Selection is:\n{count_gender}")
    else:
        print()
        print(f"The count of user gender from {city} city is not possible because it has no such column as 'Gender'. Skipping now...")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in read_city.columns:
        # Earliest year of birth
        earliest_birth = read_city['Birth Year'].min()
        print()
        print(f"Earliest birth from Selection is: {earliest_birth}")
        # Most recent year of birth
        most_recent_birth = read_city['Birth Year'].max()
        print()
        print(f"Most recent birth from Selection is: {most_recent_birth}")
        # Most common year of birth
        most_common_birth = read_city['Birth Year'].mode()[0]
        print()
        print(f"Most common birth from Selection is: {most_common_birth}")
    else:
        print()
        print(f"The count stats for Birth Year from {city} city is not possible because it has no such column as 'Birth Year'. Skipping now...")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("D O N E")

def user_view_raw_data(read_city):
    """Allow users to view the raw data from the city file

    Args:
        (DataFrame) read_city - Pandas DataFrame containing city data with filters.
    """
    while True:
        print()
        view_raw_data = input('Would you like to view first five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() == 'yes':
            print(read_city.head())
            initial_view = 0
            while True:
                print()
                view_raw_data = input('Would you like to view the next five raw data set from this city? Enter yes or no. >>')
                if view_raw_data.lower() == 'yes' or view_raw_data.lower() == 'y':
                    initial_view += 5
                    print(read_city.iloc[initial_view : initial_view + 5])
                else:
                    return
        else: 
            break
        

def main():
    while True:
        city, month, day = get_filters()
        read_city = load_data(city, month, day)

        time_stats(read_city)
        station_stats(read_city)
        trip_duration_stats(read_city)
        user_stats(read_city, city)
        user_view_raw_data(read_city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("THANK YOU. Quiting Now...")
            break


if __name__ == "__main__":
    main()
