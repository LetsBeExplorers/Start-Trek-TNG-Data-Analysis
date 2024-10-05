import pandas as pd
from cleandataframe import cleanDataframe
from bagofwords import bagOfWords
import matplotlib.pyplot as plt
from linearRegressionSKL import linearRegressionSKL
from linearRegressionRK import linearRegressionRK


# pull in csv file and put it into a dataframe
csv_file_path="/home/raytracer/projects/CS3080/Final_Project/TNG.csv"
tngData=pd.read_csv(csv_file_path, encoding='latin-1')

# returns a cleaned dataframe that can be used for data collection
tngData = cleanDataframe(tngData)

# putting all unique pairs of season/episode into a list for indexing
pairs = tngData.groupby(['Season', 'Episode'])
indexPairs = []
for pair in pairs.groups.keys():
    indexPairs.append(pair)

# counts how many times each word is used in data's speech
# creates an array of dictionaries containing word counts
bow_model = bagOfWords(tngData, indexPairs)

# create an array with the number of unique words per episode
episodeWT = []
for total in bow_model:
    episodeWT.append(len(total))

# create a series that holds the number of episodes in each season
episodesPerSeason = tngData.groupby('Season')['Episode'].nunique()

# number of season and number of episodes
numSeasons = tngData['Season'].nunique()
numEpisodes = sum(episodesPerSeason)

# creates an array containing average of unique words per season
seasonWT = []
start = 0
for x in episodesPerSeason:
    end = start+x
    seasonWT.append(int(sum(episodeWT[start:end])/x))
    start += x

# total of 6 plots in this project
fig, axs = plt.subplots(6, figsize=(15, 30))

# creates a simple line graph from the given data
def plotData(y, x, plot, title):
    # set title and plot
    plot.set_title(title)
    plot.plot(x, y)

    # start both axes at 0 and add some to the top of the y axis
    plot.set_xlim(xmin=1)

    upperLimit = 50+plot.get_ybound()[1]
    plot.set_ylim(bottom=0, top=upperLimit)  

# creating the unique words per episode plot
print("Plotting number of unique words per episode...")
plotTitle = "Number of Unique Words used by Data per TNG Episode"
plotData(list(episodeWT), range(1, numEpisodes+1), axs[0], plotTitle)

print("Plotting the average of unique words per season...")
plotTitle = "Average of Unique Words used by Data per TNG Season"
plotData(list(seasonWT), range(1, numSeasons+1), axs[1], plotTitle)

# SKL header
print()
print("Linear Regression implemented using the SKL library")
print("---------------------------------------------------")

# send episode and season word totals through SKL linear regression
print()
print("Number of Words per Episode")
predictWTE = linearRegressionSKL(episodeWT)

print()
print("Average Number of Words per Season")
predictWTS = linearRegressionSKL(seasonWT)

# plot linear regression lines, as done by SKL, on top of data
print()
print("Plotting SKL linear regression line for number of words per episode...")
plotTitle = "Linear Regression Line for Words per Episode - SKL"
plotData(list(episodeWT), range(1, numEpisodes+1), axs[2], plotTitle) # data plot
plotData(list(predictWTE), range(1, numEpisodes+1), axs[2], plotTitle) # linear regression line

print("Plotting SKL linear regression line for average words per episode...")
plotTitle = "Linear Regression Line for Average Words per Season - SKL"
plotData(list(seasonWT), range(1, numSeasons+1), axs[3], plotTitle) # data plot
plotData(list(predictWTS), range(1, numSeasons+1), axs[3], plotTitle) # linear regression line

#header
print()
print("Linear Regression implemented by Rachel Koch (me)")
print("---------------------------------------------------")

# send episode and season word totals through my linear regression
print()
print("Number of Words per Episode")
predictWTE = linearRegressionRK(episodeWT)

print()
print("Average Number of Words per Season")
predictWTS = linearRegressionRK(seasonWT)

# plot linear regression lines, as done by myself, on top of data
print()
print("Plotting RK linear regression line for number of words per episode...")
plotTitle = "Linear Regression Line for Words per Episode - RK"
plotData(list(episodeWT), range(1, numEpisodes+1), axs[4], plotTitle) # data plot
plotData(list(predictWTE), range(1, numEpisodes+1), axs[4], plotTitle) # linear regression line

print("Plotting RK linear regression line for average words per episode...")
plotTitle = "Linear Regression Line for Average Words per Season - RK"
plotData(list(seasonWT), range(1, numSeasons+1), axs[5], plotTitle) # data plot
plotData(list(predictWTS), range(1, numSeasons+1), axs[5], plotTitle) # linear regression line

# save all graphs to an image
plt.subplots_adjust(hspace=0.3)
plt.savefig('DataAnalysisPlots.jpg', bbox_inches='tight', pad_inches=1)