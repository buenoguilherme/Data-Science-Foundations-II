from pandas import DataFrame, Series
import numpy

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_medal_counts = {'country_name':Series(countries),
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}

df = DataFrame(olympic_medal_counts) 

def avg_bronze_medal_count(df):
    countries_gold_medals_df = df['bronze'][df.gold >= 1]
    avg_bronze_at_least_one_gold = numpy.mean(countries_gold_medals_df)

    return avg_bronze_at_least_one_gold

def avg_medal_count(df):
    # avg_medal_count = df.mean(0)
    avg_medal_count = df[['gold', 'silver', 'bronze']].apply(numpy.mean)
    return avg_medal_count

def points_per_medal(df):
    # avg_medal_count = df.mean(0)
    points_table = [4, 2, 1] # this goals from gold to bronze 

    medals = df[['gold', 'silver', 'bronze']]
    points = medals.dot(points_table)
    points_df = DataFrame({
        'country_name': df['country_name'],
        'points': points
        })
    return points_df

print(points_per_medal(df))
