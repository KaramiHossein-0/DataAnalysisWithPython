import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count =  df['race'].value_counts()
    # What is the average age of men?
    average_age_men =  round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors  = (bachelors_count / total_people) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    advanced_edu_df = df[df['education'].isin(advanced_education)]
    total_advanced_edu = len(advanced_edu_df)
    advanced_edu_over_50K = advanced_edu_df[advanced_edu_df['salary'] == '>50K'].shape[0]
    percentage_over_50K = (advanced_edu_over_50K / total_advanced_edu) * 100 if total_advanced_edu > 0 else 0



    # What percentage of people without advanced education make more than 50K?
    non_advanced_education = ['HS-grad', '11th', '9th', 'Some-college','Assoc-acdm', 'Assoc-voc', '7th-8th', 'Prof-school', '5th-6th', '10th', '1st-4th', 'Preschool', '12th']
    non_advanced_edu_df = df[df['education'].isin(non_advanced_education)]
    total_non_advanced_edu = len(non_advanced_edu_df)
    non_advanced_edu_over_50K = non_advanced_edu_df[non_advanced_edu_df['salary'] == '>50K'].shape[0]
    percentage_over_50K_non_advanced = (non_advanced_edu_over_50K / total_non_advanced_edu) * 100 if total_non_advanced_edu > 0 else 0




    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = advanced_education
    lower_education = non_advanced_education



    # percentage with salary >50K
    higher_education_rich = percentage_over_50K
    lower_education_rich = percentage_over_50K_non_advanced

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_hours = df['hours-per-week'].min()
    min_work_hours = min_hours

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours = df['hours-per-week'].min()
    min_hours_people = df[df['hours-per-week'] == min_hours]

    if len(min_hours_people) > 0:  
        count_above_50K = (min_hours_people['salary'] == '>50K').sum()
        total_people = len(min_hours_people)
        percentage_above_50K = (count_above_50K / total_people) * 100
    else:
        percentage_above_50K = 0



    num_min_workers = None

    rich_percentage = percentage_above_50K

    # What country has the highest percentage of people that earn >50K?



    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack(fill_value=0)

    country_salary['percentage_above_50K'] = country_salary['>50K'] * 100

    highest_percentage_country = country_salary['percentage_above_50K'].idxmax()
    highest_percentage_value = country_salary['percentage_above_50K'].max()

    highest_earning_country = highest_percentage_country
    highest_earning_country_percentage = highest_percentage_value

    # Identify the most popular occupation for those who earn >50K in India.


    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    most_popular_occupation = india_high_earners['occupation'].value_counts().idxmax()
    top_IN_occupation = most_popular_occupation

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men,1),
        'percentage_bachelors': round(percentage_bachelors,1),
        'higher_education_rich': round(higher_education_rich,1),
        'lower_education_rich': round(lower_education_rich,1),
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': (highest_earning_country),
        'highest_earning_country_percentage':
        round(highest_earning_country_percentage,1),
        'top_IN_occupation': top_IN_occupation
    }
