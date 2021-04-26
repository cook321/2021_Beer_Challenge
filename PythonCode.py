import pandas as pd
import random
#Run this code in any python environment
#When reading in the csv make sure to to have the correct file path to the data

myDF = pd.read_csv(r"C:\Users\adam1\Downloads\BeerDataScienceProject\BeerDataScienceProject.csv", encoding='latin1')

#1
brewer_grouping = myDF.groupby('beer_brewerId')['beer_ABV'].mean()
myDF1 = pd.DataFrame(brewer_grouping)
myDF1.sort_values(by=['beer_ABV'], ascending = False)
#The three strongest breweries were ids 6513, 736, and 24215

#2
myDF['year'] = pd.DatetimeIndex(pd.to_datetime(myDF['review_time'], unit = 's')).year
year_grouping = myDF.groupby('year')['review_overall'].mean()
myDF2 = pd.DataFrame(year_grouping)
myDF2.sort_values(by=['review_overall'], ascending = False)
#The highest overall rating for a particular was 4.18 out of 5 stars across the total categories.

#3
list_names = ['taste', 'aroma', 'appearance', 'palette']
list_avg = [myDF['review_taste'].mean(), myDF['review_aroma'].mean(), myDF['review_appearance'].mean(), myDF['review_palette'].mean()]

averages = pd.DataFrame()
averages['names'] = list_names
averages['categories'] = list_avg
averages['difference from review_total'] = averages['categories'] - myDF['review_overall'].mean()
averages
#after looking at the difference between the overall reviews and the aroma review, they actually are surpisingly similar.
#aroma appears to be the most important factor.

#4
individual_beers = myDF.groupby('beer_beerId')['review_overall'].mean()
myDF4 = pd.DataFrame(individual_beers)
myDF4 = myDF4[myDF4['review_overall'] == 5]

list_5s = []
for beer in myDF4.index:
    list_5s.append(beer)

individual_beers = myDF.groupby('beer_beerId')['review_taste'].mean()
myDF4 = pd.DataFrame(individual_beers)
myDF4 = myDF4[myDF4['review_taste'] == 5]

list_5staste = []
for beer in myDF4.index:
    list_5staste.append(beer)

overlap = []
for beer in list_5s:
    if beer in list_5staste:
        overlap.append(beer)


beers = random.choices(overlap, k=3)

for b in beers:
    inter = myDF[myDF['beer_beerId'] == b]
    print(inter['beer_name'])
    
#The 3 names of the randomly selected 5 star overall and 5 star taste beers are printed here
