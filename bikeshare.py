import time
import pandas as pd
import numpy as np

"""
i couldn't write in README.txt for some reason so i will document everything in this docstring:
most of the way i wrote this code is from the lessons of pandas and scripting and the practice problems before the project
another part of the code which has to with city_selection is mainly taken from the webinar 
other than that i have taken a look at these websites but i didn't gain much or heavily used :
https://nfpdiscussions.udacity.com/t/project1-how-to-test-my-statistic-results/45405/2
https://nfpdiscussions.udacity.com/t/the-most-common-start-and-end-station/45702
https://medium.com/@rtjeannier/pandas-101-cont-9d061cb73bfc
https://shichaoji.com/2016/10/11/python-iterators-loading-data-in-chunks/
"""



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#city=input('which city you\'d like to choose?\n')

def filter_city():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_selection=input('Select Only from the following:\n 1 for chicago\n 2 for New York City\n 3 for Washington\n')
            if city_selection in ['1','2','3']:
                                 break
        
            
        except KeyboardInterrupt: 
                                 print("no input is taken")
        else:
                                 print('invalid input!!\n Try again')
        
                                 
    city_selections={'1':'chicago','2': 'new york city','3':'washington'} 
    if city_selection in city_selections.keys():
                city=city_selections[city_selection]
    return city          
def load_data_none(city):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.dropna(axis=0, inplace=True)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
  
    return df
def load_data_month(city,month):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        
        (str) month - name of the month to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.dropna(axis=0, inplace=True)
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
    return df
def load_data_day(city,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.dropna(axis=0, inplace=True)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df
def load_data_both(city,month,day):
    df = pd.read_csv(CITY_DATA[city])
    df.dropna(axis=0, inplace=True)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if (month =='all') and (day != 'all'):
        df = df[df['day_of_week'] == day.title()]
        
    elif (day =='all') and (month !='all'):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by month if applicable
    elif (month != 'all') and (day !='all'):
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] 
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    return df
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time////
    print("Total Travel time: ",df['Trip Duration'].sum())


    # TO DO: display mean travel time////
    print("Average Travel time: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts(0)) 

    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        print(df['Gender'].value_counts(0)) 

    # TO DO: Display earliest, most recent, and most common year of birth/////
    if 'Birth Year' in (df.columns):
        print("most common year: ",df['Birth Year'].mode()[0]) 
        print("most recent year: ",df['Birth Year'].max()) 
        print("earliest year: ",df['Birth Year'].min()) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station//////
    common_start_station = df['Start Station'].mode()[0]
    print("most common start station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]                             
    print("most common start station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["rout"] = df["Start Station"] + "-" + df["End Station"] 
    print (df['rout'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def most_common_strt_hr(city):
    #filename = '{}.csv'.format(city)

# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.dropna(axis=1, inplace=True)

# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

# find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)
def most_common_month(city):
    #filename = '{}.csv'.format(city)

# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.dropna(axis=1, inplace=True)
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
    df['month'] = df['Start Time'].dt.month

# find the most popular hour
    common_month = df['month'].mode()[0]

    print('Most common month', common_month)
def most_common_day(city):
    #filename = '{}.csv'.format(city)

# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.dropna(axis=1, inplace=True)
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.day_name()

# find the most popular hour
    common_day = df['day'].mode()[0]
    
    print('Most common day\n', common_day)
def display_raw_input(city):
    while display_raw == 'yes':
       try:
            #looping over the chunks in the pd.read_csv() function with a for loop (chunksize=5):
            for chunk in pd.read_csv(file name, chunksize=5)
            print(chunk)
            # repeating the question
            display_raw = "do you wish to display another 5 rows?").lower()
            if display_raw != 'yes':
                print('Thank You')
                break
            break
        except KeyboardInterrupt:
                print('Thank you.')




def main():
  
  while True:
    while True:
        city=filter_city()
      
      #filename = '{}.csv'.format(city
        x=input('would you like to filter by :\n (1) month\n (2) day \n (3) both\n (4) none\n ')
            
            

        if x=='1':
            try:
                month=input('which month you\'d like to filter by.. write the name of any month starting from january till june \n').lower()
                print(load_data_month(city,month))
                print(most_common_month(city))
                df=load_data_month(city,month)
                df.dropna(axis=0, inplace=True)
                break
            except (KeyboardInterrupt, ValueError, NameError):
                print("oops.. try again")
                continue
                
        
        elif x=='2':
              try:
                  day=input("which weekday would you like filter by?.. write the fullname of the desired weekday\n").lower()
                  print(load_data_day(city,day))
                  print(most_common_day(city))
                  df=load_data_day(city,day)
                  df.dropna(axis=0, inplace=True)
                  break
              except (KeyboardInterrupt, ValueError, NameError):
                     print("oops.. try again")
                     continue
                    
    
        elif x=='3':
             try:
                  month=input('which month you\'d like to filter by.. write the name of any month starting from january till june or type all  \n').lower()
                  day=input("which weekday would you like filter by?.. write the fullname of the desired weekday\n").lower()
                  print(load_data_both(city,month,day))
                  print(most_common_month(city))
                  print(most_common_day(city))                
                  df=load_data_both(city,month,day)
                  df.dropna(axis=0, inplace=True)
                  break
             except (KeyboardInterrupt, ValueError, NameError):
                  print("oops.. try again")  
                
         
        elif x=='4':
            try:
                  df=load_data_none(city)
                  df.dropna(axis=0, inplace=True)
                  print(most_common_month(city))
                  print(most_common_day(city))
                  break
                #print("please try again and type correctly")
            except (KeyboardInterrupt, ValueError, NameError):
                print("oops.. try again")
            
        else:
           print("try typing correctly")
           continue
            

    most_common_strt_hr(city)
    trip_duration_stats(df)  
    user_stats(df)
    station_stats(df)
    display_raw_input(city)
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
                  break


if __name__ == "__main__":
	main()
