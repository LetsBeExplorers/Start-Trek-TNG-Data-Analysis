# cleans the provided dataframe by dropping unnecessary columns and rows, 
# replacing missing data, and correcting column types
def cleanDataframe(data):
    
    # pulling out unnecessary rows and columns and isolating Data's speech
    cleanedDF = data.drop(columns=["productionnumber", "speechdescription", "partnumber", "setnames","characters", "Released", "act","scenenumber","scenedetails", "imdbRating","imdbID"])
    cleanedDF = cleanedDF.drop(cleanedDF.columns[0], axis=1)
    cleanedDF = cleanedDF[cleanedDF['type'].str.contains("description") == False]
    cleanedDF = cleanedDF[cleanedDF['who'].str.contains("DATA") == True]
    cleanedDF = cleanedDF.drop(columns=["type", "who"])

    # fix a couple of episodes with missing data
    cleanedDF.loc[cleanedDF.episode == 'time\'s arrow', 'Episode'] = 26
    cleanedDF.loc[cleanedDF.episode == 'time\'s arrow', 'Season'] = 5
    cleanedDF.loc[cleanedDF.episode == 'rascals', 'Episode'] = 7
    cleanedDF.loc[cleanedDF.episode == 'rascals', 'Season'] = 6

    # make all speech lowercase
    cleanedDF['text'] = cleanedDF['text'].str.lower() 

    # convert season and Episode columns to ints
    cleanedDF['Episode'] = cleanedDF['Episode'].astype(int)
    cleanedDF['Season'] = cleanedDF['Season'].astype(int)

    return cleanedDF
