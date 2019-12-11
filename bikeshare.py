
import pandas as pd
import time
#import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    #df = pd.read_csv(CITY_DATA[month])
    
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    cities = ["chicago", "new york city", "washington"]
    
    city = input("Enter the city: ").lower()
    
    while city not in cities:
            print("The city you entered:" + city + "is not available, please enter {}, or {}, or {}".format(cities[0], cities[1], cities[2]))
            city = input("Enter the city: ").lower()

    #get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    month = input("Enter the month or all for all months: ").lower()
    
    while month not in months:
            print("The month you entered:" + month + " is not available, please enter {}, or {}, or {}, {}, or {}, or {}, or {}".format(months[0], months[1], months[2], months[3], months[4], months[5], months[6]))
            month = input("Enter the month or all: ").lower()

    #get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    day = input("Enter the day of week or all for all days of the week: ").lower()
    
    while day not in days:
            print("The day you entered: " + day + " is not valid. the correct input must be sunday to saturday, or all for all days of the week")
            day = input("Enter the day of week or all for all days of the week: ").lower()
                                    
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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #combine Start Station and End station to create a new column
    df['Start and End Stations'] = df['Start Station'] + " TO " + df["End Station"]
        
    
    #filter by month if applicable
    if month != 'all':
        
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create to create new datafarme
        df = df[df['month'] == month]
        
        #filter by day of week if applicable
        
    if day != 'all':
        
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]        

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    common_month = df['month'].mode()[0]
    print("The most common month is:", common_month )

    #display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is:", common_day_of_week)

    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #calculate Station stats
    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    frequent_start_end_station = df['Start and End Stations'].mode()[0]
    
    #display station stats 
    print("The most common start station is:", common_start_station, "\nThe most commonly used End Station is:", common_end_station, "\nThe most frequent combination of start and end stations is:", frequent_start_end_station )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is:", total_travel_time)

    #display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_travel_time)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_types = df['User Type'].value_counts()

    print("The count of user type is: " ,user_types)

    #Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("The gender count is: " ,gender_count)
<<<<<<< HEAD
        
    # Handle Gender column exception for the for washington   
||||||| 91d3ec5
        
=======

    # Handle Gender column exception for the for washington city   
>>>>>>> refactoring
    except KeyError:        
        print("No Gender data is available for washington city")        
                
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_YOB = df['Birth Year'].min()
        most_recet_YOB = df['Birth Year'].max()
        most_common_YOB = df['Birth Year'].mode()[0]
    
        # Refactor the print statement to execute from one line of code
        print("The earliest year of birth is: " ,earliest_YOB, "\nThe most recent year of birth is: " ,most_recet_YOB, "\nThe most common year of birth is: " ,most_common_YOB)

        
    except KeyError:
        print("No Birth Year data is available for washington city")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Asks the user if they want to print raw data
    
    Args:
        raw_data - the acceptable values are yes or no, to confirm if the user wants to print raw data
        num_rows - number of rows of raw data that the user wants print
    
    Output:
        prints the list raw data records as specified by the user
    """
    # display the complte list of columns in a datafarme
    pd.set_option('display.max_columns', None)
    
    #display raw data, allow the user to specify how many rows they want to display
    choice = ["yes", "no"]
    while True:
        raw_data = input('\nWould you like to diplay raw data? Enter yes or no.\n').lower()
        
        while raw_data not in choice:
            print("Your input is not valid, please enter 'yes' or 'no' ")
            raw_data = input('\nWould you like to diplay raw data? Enter yes or no.\n').lower()
            
        if raw_data == "yes":
            num_rows = int(input('How many rows would you like to display?: only integers are accepted:'))
                        
            print(num_rows, 'lines of raw data \n', df.head(num_rows))
            
            #print raw data to csv file: raw_data.csv
            print("The raw data has also been saved to the csv file named: 'raw_data_file.csv' ")
            df.head(num_rows).to_csv('raw_data_file.csv')
            break
                    
        elif raw_data == 'no':
            break
        
        else:
            True 
    
def main():
    while True:
        city, month, day = get_filters() 
        df = load_data(city, month, day)
        df.to_csv('file1_bikeshare.csv')
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
                  
        #allow the user to restart, or to terminate
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()