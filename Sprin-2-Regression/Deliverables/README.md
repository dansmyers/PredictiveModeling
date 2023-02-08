# Sprint 2 Deliverables

## Instructions

Complete the following four analyses. For each question,

- Make a `.py` file in your Repl.it workspace. Put all of your code for the question in the file.
- You can put answers to any interpretation questions right into the Python file using comments. You don't need to upload any Word, PDF, or text files.

## Tips

- Start early! Don't wait until the last minute!

- Complete the Longbones and Weather labs first. They contain the relevant examples that you'll need for the assignment.

- If you need to install `seaborn` or `statsmodels`, use `pip`. For example,

```
pip install seaborn
```

## Animal Sleep

**What factors influence mammal sleep patterns?**

All mammals sleep. As any college student who has pulled an all-nighter knows, going without sleep or trying to function on too little sleep has a host of deleterious effects. But for something that is so clearly physiologically important, there is a great variety in sleep needs throughout the animal kingdom from animals that seem never to sleep to those who that seem never to wake (ahem, cats). Researchers recorded data on sleep duration as well as a set of ecological and constitutional variables for a selection of mammal species1. This data appears in the `Sleep.xlsx` dataset. We wish to examine the relationship between dreaming and non-dreaming sleep time in this set of mammal species. 

1.	Open `Sleep.csv` and read it into a dataframe. List the variables and identify each variable in the dataset as categorical or quantitative.

2.	Display and describe the distribution of total sleep for the mammal species in the dataset.

3.	Plot the relationship between non-dreaming and dreaming sleep. Do animals who spend more time in dreaming sleep also spend more time in non-dreaming sleep or does dreaming sleep decrease as non-dreaming sleep increases?

4.	What is the appropriate method to model the relationship between time spent in non-dreaming sleep and time spent in dreaming sleep? Verify that the assumptions for using this method are met.

5.	Create a model to predict time spent in dreaming sleep from time spent in non-dreaming sleep.

6.	Calculate and interpret the correlation and R<sup>2</sup> describing the relationship between dreaming and non-dreaming sleep time.

7.	If a mammal species experiences 5 hours of non-dreaming sleep a day, how many hours of dreaming sleep would we expect that animal to get on average?

8.	Calculate the difference in the number of hours spent in non-dreaming and dreaming sleep for each mammal in the dataset.

## Plants

**The goal of this problem is to present an example where linear regression is *not* the appropriate model**.

How do environmental factors contribute to the diversity of plant life on an island? The `Plants.xlsx` dataset provides information on a number of characteristics of the British Isles (not including Ireland or Britain itself) including latitude, area, and distance from Britain. We wish to use linear regression to determine if islands with a larger area are home to a greater number of species of plant life.

1.	Import the `Plants.csv` dataset. List the variables and identify each variable in the dataset as categorical or quantitative.

2.	Create a scatterplot to display the relationship between island area and number of plant species living in the British Isles.

3.	Determine the regression equation that relates island area to number of plant species. 

4.	Modify the scatterplot from #2 to include the regression line.

5.	Create a residual plot and look for potential violations of the assumptions for linear regression.

6.	Does island area seem to be related to the of number of plant species living on each of the British Isles? Is linear regression the correct method for modeling this relationship?  


## The Dream of Wearing Shorts Forever

<img src="https://upload.wikimedia.org/wikipedia/commons/3/30/City_Centre_viewed_from_Mount_Ainslie_lookout.jpg" width="75%" />

*View of Canberra*

Let's return to the `weatherAUS` data set, which recorded meteorological observations from weather stations in Australia.

Suppose we're interested in whether it will rain today using the features corresponding to the weather measurements at 9 AM. Write an R script that builds a logistic
regression model for carrying out this task. Your model should do the following:

1. Load the `weatherAUS` data set.

2. Create a `RainToday_Num` column by converting `RainToday` into a 0-1 value.

3. Use the `logit` function to predict `RainToday_Num` based on the features that have `9am` in their names.

4. Use `summary` to examine the output of the model and identify which features, if any, are significant.

5. Predict the probability of rain today associated with each point in the data set, then create a table showing the numbers of correct and incorrect classifications.

6. Compare your results to the naïve classification approach of just predicting "No" for every instance. Does your classifier perform better?

7. Create two subsets, one for the observations from the city of Darwin (on the northern coast) and the other for Uluru (in the middle of the Outback). Do a little exploratory analysis and then construct a model for each location. Can you generate more accurate predictions for one location than for the other? If so, which features are most important for each location? FYI: I don't have a sure answer in mind for this question; it's just an interesting analysis. Try it out and see what you can discover!

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/ULURU.jpg/1920px-ULURU.jpg" width="50%" />

*Uluru or Ayers Rock. Picture from Wikimedia.*.

## High vs. Low Mileage

<img src="https://hatchheaven.com/wp-content/uploads/2013/07/subary_gl_84_1-880x660.jpg" width="50%" />

*The 1984 Subaru hatchback. I learned to drive a stick shift on one of these. Ah, nostalgia.*

This problem uses the `Auto` dataset to predict whether cars have high or low gas mileage.

1. Load the `Auto` data set into a Pandas dataframe.

2. Create a new variable called `high_mpg` that will have value 0 if a vehicle has below-median gas mileage and 1 if the vehicle has above-median gas mileage. Tip: do a little research to find out how to calculate the median of a column in a Pandas dataframe.

3. Spend some time looking at the data and conducting some exploratory analysis. Which variables do you think are likely predictors of high vs. low gas
mileage? **Note that you can't use `mpg` as a predictor because we used it to define the class**.

4. Construct a logistic regression model to predict the probability that a vehicle is high or low mileage.

5. Use `summary` to investigate which predictors appear to be significant.

6. Calculate the confusion matrix and the overall fraction of correct classifications for your test set. How does your model perform?
