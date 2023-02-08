# Sprint 2 Deliverables

## Instructions

Complete the following four analyses. For each question,

- Make a `.py` file in your Repl.it workspace. Put all of your code for the question in the file.

- You can put answers to any interpretation questions right into the Python file using comments.


## The Dream of Wearing Shorts Forever

<img src="https://upload.wikimedia.org/wikipedia/commons/3/30/City_Centre_viewed_from_Mount_Ainslie_lookout.jpg" width="75%" />

*View of Canberra*


Let's return to the `weather` data set, which recorded meteorological observations from a weather station in Canberra.

Suppose we're interested in whether it will rain today using the features corresponding to the weather measurements at 9 AM. Write an R script that builds a logistic
regression model for carrying out this task. Your model should do the following:

- Load the `weatherAUS` data set.

- Create a `RainToday_Num` column by converting `RainToday` into a 0-1 value.

- Use the `logit` function to predict `RainToday_Num` based on the features that have `9am` in their names.

- Use `summary` to examine the output of the model and identify which features, if any, are significant.

- Predict the probability of rain today associated with each point in the data set, then create a table showing the numbers of correct and incorrect classifications.

- Compare your results to the naïve classification approach of just predicting "No" for every instance. Does your classifier perform better?


## High vs. Low Mileage

<img src="https://hatchheaven.com/wp-content/uploads/2013/07/subary_gl_84_1-880x660.jpg" width="50%" />

*The 1984 Subaru hatchback. I learned to drive a stick shift on one of these. Ah, nostalgia.*

This problem uses the `Auto` dataset to predict whether cars have high or low gas mileage.

- Load the `Auto` data set into a Pandas dataframe.

- Create a new variable called `high_mpg` that will have value 0 if a vehicle has below-median gas mileage and 1 if the vehicle has above-median gas mileage. Tip: do a little research to find out how to calculate the median of a column in a Pandas dataframe.

- Spend some time looking at the data and conducting some exploratory analysis. Which variables do you think are likely predictors of high vs. low gas
mileage? **Note that you can't use `mpg` as a predictor because we used it to define the class**.

- Construct a logistic regression model to predict the probability that a vehicle is high or low mileage.

- Use `summary` to investigate which predictors appear to be significant.

- Calculate the confusion matrix and the overall fraction of correct classifications for your test set. How does your model perform?