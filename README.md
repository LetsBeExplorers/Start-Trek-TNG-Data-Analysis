# Start Trek TNG: Data Analysis

Data is an android from Star Trek: The Next Generation (TNG). This project aimed to determine whether Data's speech patterns actually become more human throughout the show by analyzing how many different words Data used per episode. I hypothesized that if Data's speech patterns do indeed become more human, than his word variability should increase over time.

Word Variability was tested by how many different words Data uses per episode, and how often he uses the same words (i.e. the distribution). Linear regression was performed on the distributions to determine if the overall trend was increasing, decreasing, or neither.

## Project Files

#### DataAnalysis.py
This is the main file that performs the analysis. Run this file to get output and see results.

#### cleandataframe.py
This file takes in a dataframe and drops the columns/rows that are uneeded for this project. It also fixes the missing data and casts a couple columns to integers before processing. It is not a general cleaning function, it is specific to this project and removes exactly what is needed to process the data for purposes stated above. 

#### TNG.csv
The csv file that is being processed and turned into a dataframe for analysis. 

#### bagofwords.py
This file contains a function which takes all the speech lines, creates text blocks for each episode, counts how many times each words was used in the text block, and then saves those counts to a dictionary. It returns an array of dictonaries that contain the word counts for each episode.

#### linearRegressionSKL.py
The function in this file performs Linear Regression Analysis on the bag of words data; implemented using the SciKit-Learn library. It returns an array of predicted values based on the regression analysis.

#### linearRegressionRK.py
The function in this file performs Linear Regression Analysis on the bag of words data; implemented manually by me. It also returns an array of predicted values based on the regression analysis.

#### FinalProject_WriteUp.pdf
A write-up of the conclusion and results of this analysis. 

### Generated Files
#### output.txt
This file contains all the dictionaries of word counts for each episode. This is used for troubleshooting and verification. 

#### DataAnalysisPlots.jpg
This file contains all the plots for this project.

## Project Libraries
nltk \
matplotlib \
sklearn \
numpy \
string \
os \
pandas

## Sources
https://spotintelligence.com/2022/12/20/bag-of-words-python/ (bag of words) \
https://www.geeksforgeeks.org/python-linear-regression-using-sklearn/ (Linear Regression SKL) \
https://github.com/RMHogervorst/TNG (dataset) \
Lots of Stack Overflow (everything)

