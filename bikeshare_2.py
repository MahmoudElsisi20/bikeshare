import pandas as pd
import numpy as np
import time


#datasets
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# months,days and filter names
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days=['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday','all']
filters_data=['month','day','both']



def get_filters():
    """
    Asks user to specify a city,filter,month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) filter - name of filter 
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city=input("Would you like to see data for [Chicago, New York, or Washington]:").lower() 
    if city not in CITY_DATA:
          print("############Enter correct input###############")
          exit()
          
    # get user input for filter (month,day, both). HINT: Use a while loop to handle invalid inputs
    filters=input("Would you like to filter data [month,day or both]:").lower()
    if filters not in filters_data:
                    print("############Enter correct input###############")
                    exit()

    if filters=="month":
        # get user input for month (all, january, february, ... , june)
            month=input("Which month - [January, February, March, April, May, or June]:").lower()
            if month not in months:
                        print("############Enter correct input###############")
                        exit()

            day=None
            print('-'*40)
          
            return city,filters,month,day
        # get user input for day of week (all, monday, tuesday, ... sunday)
    elif filters=="day":
            day=input("Which day -[Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday]:").lower()
            if day not in days:
                        print("############Enter correct input###############")
                        exit()

            month=None
            print('-'*40)
            return city,filters,month,day
    else:
            month=input("Which [month - January, February, March, April, May, or June]:").lower()
            if month not in months:
                        print("############Enter correct input###############")
                        exit()

            day=input("Which day - [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday]:").lower()
            if day not in days:
                        print("############Enter correct input###############")
                        exit()

            print('-'*40)
            return city,filters, month, day
    

def load_data(city):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day
    df['hour']=df['Start Time'].dt.hour
    df["start_end_station"] = "Start_Station:"+df["Start Station"]+" "+"End_Station:"+df["End Station"]


    



    return df

def time_stats(df,filters,month,day):
    """
    Displays statistics on the most frequent times of travel.
    like:[Most popular month,Most popular day,Most popular hour]
    
    inputs: df-> DataFrame of datasset that we worked with
            (str)filters->name of filter
            (str)month ->name of month
            (str)day ->name of day
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if filters=="month":
    # display the most common month
        if month !="all":
            month = months.index(month) + 1
            df = df[df['month'] == month]
            print("Most popular month {0}".format(month))
            common_hour=df["hour"].mode()
            count_hour=df["hour"].value_counts()[common_hour]
            print("Most popular hour: {0} count= {1}".format(common_hour[0],int(count_hour)))

        else:
            print("Most popular month {0}".format(df["month"].mode()[0]))
            common_hour=df["hour"].mode()
            count_hour=df["hour"].value_counts()[common_hour]

            print("Most popular hour: {0} count= {1}".format(common_hour[0],int(count_hour)))


    elif filters=="day":
    # display the most common day of week
        if day !="all":
            day=days.index(day) + 1
            df = df[df['day'] == day]
            print("Most popular day {0}".format(day))
            common_hour=df["hour"].mode()
            count_hour=df["hour"].value_counts()[common_hour]
            print("Most popular hour: {0} count= {1}".format(common_hour[0],int(count_hour)))

        else:
            print("Most popular day {0}".format(df["day"].mode()[0]))
            common_hour=df["hour"].mode()
            count_hour=df["hour"].value_counts()[common_hour]

            print("Most popular hour: {0} count= {1}".format(common_hour[0],int(count_hour)))

    else:
        if month !="all":
            month = months.index(month) + 1
            df = df[df['month'] == month]
            print("Most popular month {0}".format(month))
        else:
            print("Most popular month {0}".format(df["month"].mode()[0]))
        
        if day !="all":
            day=days.index(day) + 1
            df = df[df['day'] == day]
            print("Most popular day {0}".format(day))
        else:
            print("Most popular day {0}".format(df["day"].mode()[0]))
        
        common_hour=df["hour"].mode()
        count_hour=df["hour"].value_counts()[common_hour]

        print("Most popular hour: {0} count= {1}".format(common_hour[0],int(count_hour)))  
    print("Filter: {0}".format(filters))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df,filters):
    """
    Displays statistics on the most popular stations and trip.
    inputs:
           df: dataframe which used to extract information that needed
           filter: name of filter
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_station=df["Start Station"].value_counts().index[0]
    count_station=df["Start Station"].value_counts()[common_station]
    print("Most popular Start Station: {0}  count: {1}".format(common_station,int(count_station)))   


    # display most commonly used end station
    common_end_station=df["End Station"].value_counts().index[0]
    count_end_station=df["End Station"].value_counts()[common_station]
    print("Most popular End Station: {0}  count: {1}".format(common_end_station,int(count_end_station)))   


    # display most frequent combination of start station and end station trip
    common_start_end_station=df["start_end_station"].value_counts().index[0]
    count_start_end_station=df["start_end_station"].value_counts()[common_start_end_station]
    print("Most popular frequent combination of start station and end station trip: {0}  count: {1}".format(common_start_end_station,int(count_start_end_station)))      

    print("Filter: {0}".format(filters))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df,filters):
    """
    Displays statistics on the total and average trip duration.
    inputs:
           df: dataframe which used to extract information that needed
           filter: name of filter 
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration=df["Trip Duration"].sum()
    print("Totla Duration : {0}".format(total_duration))   



    # display mean travel time
    mean_duration=df["Trip Duration"].mean()
    print("mean of Trip Duration: {0}".format(mean_duration))   


    print("Filter: {0}".format(filters))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df,city,filters):
    """
    Displays statistics on bikeshare users.
    inputs:
           df: dataframe which used to extract information that needed
           city: name of city
           filter: name of filter
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()
        
        # Display counts of user types
    count_of_userTypes=df["User Type"].value_counts()
    print("count of user types: ")
    print(count_of_userTypes)  
 
    if city !='washington':
        # Display counts of gender
        count_of_gender=df["Gender"].value_counts()
        print("count of gander: ")
        print(count_of_gender)
        # Display earliest, most recent, and most common year of birth
        earliest_year=df["Birth Year"].min()
        print("earliest year: {0}".format(int(earliest_year))) 

        recent_year=df["Birth Year"].max()
        print("recent year: {0}".format(int(recent_year)))
        common_year=df["Birth Year"].mode()
        print("Most popular year: {0}".format(int(common_year))) 


    print("Filter: {0}".format(filters))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def main():
    while True:
        city,filters, month, day = get_filters()
        df = load_data(city)

        time_stats(df,filters,month,day)
        station_stats(df,filters)
        trip_duration_stats(df,filters)
        user_stats(df,city,filters)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            get_filters()


if __name__ == "__main__":
	main()
