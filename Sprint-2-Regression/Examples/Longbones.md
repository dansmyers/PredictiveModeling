# The Infamous Longbones Project (The Weirdest Example of All Time)


Scatterplots, linear correlation and regression allow us to determine the straight-line relationship between two quantitative variables. Scatterplots visualize the relationship between the two variables and give us a general sense of how they vary in relation to one another. A regression line is a mathematical model that uses the value of one variable (called the independent or explanatory variable, interchangeably) to predict the value of the other variable (called the dependent or response variable, interchangeably). Correlation and R<sup>2</sup> measure the strength of the linear relationship modeled by the regression line. They allow us to determine if there is a strong, weak or no association between the independent and dependent variables.

In this lab, you'll create a scatterplot to display the relationship between two quantitative variables and calculate their correlation. You will determine the regression equation that relates two quantitative variables and use it to predict the value of the response variable for a particular value of the explanatory variable. Finally, you'll calculate R<sup>2</sup> and draw conclusions about the ability of one variable to predict the other.  

## Introduction

Scatterplots, linear correlation and regression allow us to determine the straight-line relationship between two quantitative variables. Scatterplots visualize the relationship between the two variables and give us a general sense of how they vary in relation to one another. A regression line is a mathematical model that uses the value of one variable (called the independent or explanatory variable, interchangeably) to predict the value of the other variable (called the dependent or response variable, interchangeably). Correlation and R<sup>2</sup> measure the strength of the linear relationship modeled by the regression line. They allow us to determine if there is a strong, weak or no association between the independent and dependent variables.

## Scatterplots and Linear Regression

The first step in linear regression is to determine which variable in the dataset is the explanatory variable and which is the response variable. Usually this is done through careful reading of background information or as you develop your research question. In general terms, the explanatory or independent variable is the one you wish to use to predict the response or dependent variable. It is important to be clear on which variable is which because switching them in the regression model will produce totally different (and incorrect!) results. 

Once you have identified the explanatory and response variables, you must check the conditions for modeling the data using linear regression.

- First, the two variables must be quantitative. Linear regression is not the model to use if you want to examine the relationship between one or more categorical variables.
- Second, the relationship between the two variables should be linear.
- Third, there should be no outliers in the data. 

The most direct way to test the conditions for linear regression is by creating a scatterplot. A scatterplot graphs each ordered pair (independent variable, dependent variable), allowing you to see if the data points fall more or less in a straight line (with either a positive or negative trend), have a curved (nonlinear) relationship, or have no relationship and look like a cloud of points. Violations of the conditions for linear regression are typically obvious from a scatterplot (and a residual plot), and later we’ll discuss what to do if this happens.

Once you’ve determined that it is appropriate to model your data using linear regression, R makes it very easy to calculate the slope and intercept terms and predict the mean response for a particular value of the independent variable. 

## The Correlation Coefficient (r) and the Coefficient of Determination (R<sup>2</sup>)

The correlation coefficient (also called the correlation or r, interchangeably) and the coefficient of determination (also called R<sup>2</sup>) are related mathematically (R<sup>2</sup> is the square of the correlation) and they measure the strength of the linear relationship between two quantitative variables in slightly different ways. Correlation measures the relationship between the two variables on a scale of -1 to 1 with -1 and 1 being the strongest relationships (negative and positive, respectively) and 0 being no relationship. A correlation of exactly -1 or exactly 1 would mean that all the data points fell in a straight line. 

R<sup>2</sup> is measured on a scale of 0 to 1 (recall that the square of a negative number is positive) and is usually expressed as a percent from 0% to 100%. R<sup>2</sup> tells us the percent of variation in the response variable that is explained by differences in the explanatory variable. If R<sup>2</sup> is close to 100%, then knowing what the independent variable is tells us almost everything we need to know to estimate the value of the dependent variable. In contrast, if R<sup>2</sup> is small, then there is missing information in our model that would, if present, allow us to do a better job predicting the dependent variable. 

## Can forensic scientists determine how long a body has been buried by how much nitrogen remains in the long bones of the skeleton?

Anyone who is a fan of detective TV shows has watched a scene where human remains are discovered and some sort of expert is called in to determine when the person died. But is this science fiction or science fact? Is it possible to use evidence from skeletal remains to determine how long a body has been buried (a decent approximation of how long the person has been dead)? 

Researchers sampled long bone material from bodies exhumed from coffin burials in two cemeteries in England. In each case, date of death and burial (and therefore interment time) was known. This data is given in the `Longbones.csv` dataset. We wish to determine if there is a relationship between the nitrogen composition of the long bones of the skeleton and the length of time the body was interred.
   
### Steps
1. Import the `Longbones.csv` dataset into a dataframe. List the variables it contains and identify each variable in the dataset as categorical or quantitative. If the variable is categorical, further identify it as ordinal, nominal or an identifier variable. If the variable is quantitative, identify it as discrete or continuous.

2. Create a scatterplot to display the relationship between long bone nitrogen composition and length of interment. Describe any patterns apparent from the scatterplot.

3. Study authors were concerned that contamination with fuel oil might change the relationship between long bone nitrogen composition and length of interment. On the scatterplot, identify the three skeletons that were contaminated with fuel oil using a different color dot. The study authors decided to remove these observations from analysis. Do you agree?

4. Create a new dataset using only records of remains that were not contaminated by fuel oil. Use this dataset to complete steps 5 – 10. Are the conditions met to model the relationship using correlation and linear regression?

5. Calculate the correlation between long bone nitrogen composition and length of interment.

6. Determine the regression equation that relates long bone nitrogen composition and length of interment. Interpret the slope and intercept of the line.

7. Create a scatterplot to show the relationship between long bone nitrogen composition and interment length, and annotate it with the regression line and correlation.

8. Create a residual plot and look for potential violations of the conditions for linear regression.

9. Use the regression line to determine the expected mean interment time for a body discovered with a long bone nitrogen composition of 3.71g/100g of bone.  

10. Calculate R<sup>2</sup> for this relationship. Does long bone nitrogen composition seem to be a good predictor of length of interment?  

### Import the Longbones.csv dataset into R-Studio. List the variables it contains and identify each variable in the dataset as categorical or quantitative. If the variable is categorical, further identify it as ordinal, nominal or an identifier variable. If the variable is quantitative, identify it as discrete or continuous.

Put the following code in a file named `longbones.py`.

```
"""
Analyze the longbones dataset
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Open and view the dataset
#
# The files are in the Data subdirectory
df = pd.read_csv('Data/Longbones.csv')
print(df)
```

The first variable is `Site`, which is a nominal categorical variable identifying from which of two sites the remains were exhumed. The second variable is `Time`, which is a quantitative, continuous variable measuring the time the body was interred in years. The third variable is `Depth`, which is a quantitative, continuous variable measuring the depth at which the body was buried. The fourth variable is `Lime`, which is a nominal, categorical variable indicating if the body was buried with Quicklime. The fifth variable is `Age`, which is a quantitative, continuous variable recording the age at the time of death (though this was unknown in some cases). The sixth variable is `Nitro`, which is a quantitative, continuous variable measuring the nitrogen composition in the femur of the skeleton in g/100g of bone. The seventh variable is `Oil`, which is a nominal, categorical variable that indicates if the burial site was contaminated with fuel oil. 
 
### Create a scatterplot to display the relationship between long bone nitrogen composition and length of interment. Describe any patterns apparent from the scatterplot.

Let's use the `seaborn` package to create the scatterplot.

```
sns.scatterplot(df, x='Nitro', y='Time')
plt.xlabel('Nitrogen content (g per 100g of bone)')
plt.ylabel('Length of interment (years)')
plt.xlim(3, 4.5)
plt.ylim(0, 100)
plt.savefig('time_vs_nitro.png', bbox_inches='tight')
```

Most of the seaborn plotting functions have a similar format: specify the dataframe (`df` in this example), then give the columns to use for the x and y axes of the plot. Because we are trying to predict length of interment from long bone nitrogen composition, nitrogen composition is treated as the independent variable (on the x-axis) and length of interment as the dependent variable (on the y-axis). The other statements assign labels (with relevant units) to the axes and set the scale.

The plotted points exhibit a linear trend suggesting a negative linear relationship between long bone nitrogen composition and length of interment. In bodies with longer interment time, there is either greater variability in the nitrogen composition of the long bones or possibly a few outliers.
 
### Study authors were concerned that contamination with fuel oil might change the relationship between long bone nitrogen composition and length of interment. On the scatterplot, identify the three skeletons that were contaminated with fuel oil using a different color dot. The study authors decided to remove these observations from analysis. Do you agree?

Seaborn plots can take a `hue` parameter that controls the color of each point. The code below uses the `Oil` field of the dataframe (which is a 0-1 value) to mark the points that have been contaminated with oil. The `legend` command adds a legend to the plot showing what each color represents.

```
plt.figure()
sns.scatterplot(df, x='Nitro', y='Time', hue='Oil')
plt.xlabel('Nitrogen content (g per 100g of bone)')
plt.ylabel('Length of interment (years)')
plt.xlim(3, 4.5)
plt.ylim(0, 100)
plt.legend(['Contaminated with oil', 'No contamination'], loc='lower left')
plt.savefig('time_vs_nitro_with_oil.png', bbox_inches='tight')
```

All three oil-contaminated skeletons were interred for about 80 years and had between 3.75 to 4.0 g of nitrogen per 100g of bone remaining in their long bones. Because there are chemical and biological reasons that the oil contamination could alter the natural relationship between long bone nitrogen concentration and length of interment, it makes sense to remove those points from the analysis.  

### Create a new dataset using only records of remains that were not contaminated by fuel oil. Use this dataset to complete steps 5 – 10. Are the conditions met to model the relationship using correlation and linear regression?

Use the standard technique of selecting rows based on a column value:

```
# Remove the three contaminated data points
# by selecting only the points that have Oil == 0
#
# Here, Oil != 1 means "Oil not equal to 1"
df = df[df['Oil'] != 1]
print(df)
```

The inner statement, `df['Oil'] != 1`, identifies all rows in the dataset where the `Oil` value is not 1; those are the values we want to keep. The outer statement then selects only those rows and makes them the active dataframe.

Both variables are quantitative, the scatterplot doesn’t show any strong non-linear shape and we have removed three outliers from the data. All of the conditions for modeling the relationship between long bone nitrogen composition and interment time using linear regression are met.

### Deliverable 5: Calculate the correlation between long bone nitrogen composition and length of interment.

The `cor` function is used to calculate the correlation between two variables. It doesn’t matter what order they are entered in the function. 

```
> cor(Longbones.subset$Nitro,Longbones.subset$Time)
[1] -0.6961346
```

The correlation between long bone nitrogen composition and length of interment is about -0.70, which indicates a moderately strong negative linear relationship.

### Determine the regression equation that relates long bone nitrogen composition and length of interment. Interpret the slope and intercept of the line.

The `statsmodels` library can create a regression line. The relevant function is `sm.OLS`, which performs ordinary least squares regression on the variables its given. In this case, we're going to select the y and x values to be `Time` and `Nitro` respectively.

```
Y = df['Time']
X = df['Nitro']
X = sm.add_constant(X)  # <-- sm requires calling add_constant to add an intercept
mod = sm.OLS(Y,X)
res = mod.fit()
print(res.params)
```

There are a few subtleties:

- The `statsmodels` library requires calling the `add_constant` function to add an intercept term to the linear model. If you accidentally omit this call, you'll get a model with no y-intercept, which probably won't be what you want.

- The fitting procedure has two steps. First, create the OLS model (called `mod` in the code above), then call `fit()` to actually calculate the regression parameters.

The parameters of the model should be:

```
const    335.474532
Nitro    -74.255062
```

The results return the coefficient of the intercept and the slope. Rewriting them as a model, we have 

```
y = 335.47 - 74.26 x
```

The slope term tells us that, for every additional gram of nitrogen per 100g of bone found in the long bones of a skeleton, we would expect the body to have been interred for about 74.26 fewer years. The intercept tells us what the interment time would be for a skeleton with a long bone nitrogen composition of 0 grams per 100g of bone. Because a nitrogen composition of 0 g per 100g of bone is outside the range of the data collected, it doesn’t make sense to interpret the y-intercept. 


More detailed information is available by calling `summary`.

```
print(res.summary())
```

The summary output shows the values of the parameters and the statistical tests and confidence intervals that can be used to evaluate their significance.

```
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        335.4745     47.673      7.037      0.000     238.879     432.070
Nitro        -74.2551     12.589     -5.898      0.000     -99.763     -48.747
==============================================================================
```

The rightmost two columns define a 95% confidence interval for the parameters. For the `Nitro` parameter, the model indicates the confidence interval is (-99.763, -48.747). The confidence interval is a measure of the uncertainty in the parameter estimation. In particular, we need to check if the interval contains zero:

- If the interval **does** contain zero, then there is a possibility that the x-variable has no significant impact on the y-variable. That is, if the slope might be zero, we can't conclude that changing the x-variable has a meaningful impact on the y-variable. Any apparent linear relationship in the scatterplot might be due to chance.

- If the interval **does not** contain zero, then we can conclude that the x-variable does have a statistically significant impact on the y-variable. That is, the slope is meaningfully different from zero, so changing the x-variable should lead to a meaningful change in the y-variable.

Here, the range doesn't include zero, so we can reasonably conclude that nitrogen is a statistically significant predictor of interment time.



### Create a scatterplot to show the relationship between long bone nitrogen composition and interment length, and annotate it with the regression line.

The built-in `regplot` function creates a regression plot that combines the scatterplot with the linear model. The `ci` parameter controls whether the plot includes a confidence interval around the line. Experiment with setting it to `True` and observe the difference.

```
plt.figure()
sns.regplot(df, x='Nitro', y='Time', ci=None)
plt.savefig('regplot.png', bbox_inches='tight')
```

### Create a residual plot and look for potential violations of the conditions for linear regression.

The residual plot shows the difference from the regression line. If the fit is good, the residuals should be roughly equally balanced around the regression line with no obvious shape.

```
plt.figure()
sns.residplot(df, x='Nitro', y='Time')
plt.savefig('residuals.png', bbox_inches='tight')
```

There do not appear to be any outliers in the data or any curved pattern that would indicate a nonlinear relationship between long bone nitrogen composition and interment time.

###  Use the regression line to determine the expected mean interment time for body discovered with a long bone nitrogen composition of 3.71g/100g of bone.  

Use the parameters of the model to make the prediction with an input of 3.71.

```
y = 335.47 - 74.26 * 3.71
```

Based on our regression model, the average interment time for a body discovered with a long bone nitrogen composition of 3.71g/100g of bone is about 60 years.

### Deliverable 10: Calculate R<sup>2</sup> for this relationship. Does long bone nitrogen composition seem to be a good predictor of length of interment?  

The `summary` function provides a lot of information about a regression model and can be used to determine the value of R<sup>2</sup>, the Coefficient of Determination. 

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   Time   R-squared:                       0.485
Model:                            OLS   Adj. R-squared:                  0.471
```

R<sup>2</sup> tells us that about 48.5% of the variability in length of interment can be explained by differences in the nitrogen composition in the long bones. This makes biological sense because the more nitrogen that has decomposed in the bones, the longer the person has been dead and buried.

The output also includes an "adjusted R-squared" value. Adjusted R-squared is an alternate calculation that takes into account the number of variables in the model. The adjusted calculation penalizes models that have many variables with low predictive power. Adjusted R-squared will always be lower than the basic R-squared value, but if the gap is large it can indicate that the model is overfitting the data and that the low-quality variables should be removed.

After examining the scatterplot and residual plot and removing outliers, it makes sense to model the relationship between long bone nitrogen composition and interment length with a linear regression model. However, because more than 50% of the variability in interment length is still unexplained by the model, we should think about expanding our model to include other potential predictors such as age at the time of death.
