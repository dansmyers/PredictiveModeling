# Weather in Australia

*Note: insert humorous meme about how everything in Australia is deadly*

## Description

This lab will allow you to practice the mechanics of implementing and interpreting an logistic regression model in Python. We'll use Pandas and the `statsmodels` library.

The data comes from Kaggle, and is a collection of weather measurements taken at stations at different locations in Australia. The goal is to predict whether it will rain on the next day given observations of the temperature, humidity, pressure, and other factors on the current day.

We're going to do the following:

1. Open the `weatherAUS.csv` dataset and list its features.

2. Construct and examine the correlation matrix, showing the strength of the relationship between pairs of variables.

3. Construct a logistic regression model that predicts whether it will rain tomorrow based on rain today.

4. Evaluate the performance of the model.

5. Experiment with adding more variables to the model and seeing how those changes affect its performance.

After completing this lab, you'll be prepared to complete the logistic regression questions on the deliverable assignment

## Completion

Create a file called `weather.py` in your Sprint 2 workspace. Put all of your code in there. Any interpretation questions or notes can be added as comments.


## Open the dataset

The file is saved in the `Data` subdirectory. Put the following code in your `weather.py` script:

```
"""
Analyze the Australian weather data set
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('Data/weatherAUS.csv')
print(df.head())
```

You can print a list of the columns using

```
print(df.columns)
```

Each entry in the dataframe is one set of measurements taken at a weather station in Australia. The variable of interest is called `RainTomorrow` and records whether there was rain on the next day. We'd like to build a model that can use each day's measurements to predict `RainTomorrow`.

## Convert `Yes`/`No` features to binary

The `RainToday` and `RainTomorrow` features record string values, but the logistic regression method only works on numbers. Use the following statements to construct two new 0/1 columns:

```
df['RainToday_Num'] = np.where(df['RainToday'] == 'No', 0, 1)
df['RainTomorrow_Num'] = np.where(df['RainTomorrow'] == 'No', 0, 1)
```

The first argument to `np.where` is a test applied to a column. If the test is `True`, then output is assigned the first option; in this case, if `RainToday` is `'No'`, then `RainToday_Num` becomes 0. If the test is `False`, then the second value is assigned. Here, if `RainToday` is `'Yes'`, then `RainToday_Num` is assigned 1.

## Examine the correlation matrix

The **correlation matrix** shows the strength of the relationship between all pairs of variables in the dataset. Correlation is a continuous value from -1 to 1:

- Positive values indicate positive correlation. When one variable goes up, the other one also goes up. Correlations closer to 1.0 indicate a stronger relationship.

- Negative correlation is the opposite: when one variable goes up, the other goes **down**.

- A correlation close to zero implies minimal relationship. Changes in one variable are not associated with an particular change in the other.

Now, you've probably heard the famous phrase, ***Correlation does not equal causation***. Just because two variables are **correlated** does not mean that one is **causing** changes in the other. There may be some other variable (or set of variables) that's the true underlying driver of the observed changes.

That said, examining variable correlations is often a good exploratory analysis step, since it can point to variables that are *possibly* related.


The following lines calculate the correlation matrix and then print the correlations associated with the `RainTomorrow_Num` feature.
```
corr = df.corr()
print(corr['RainTomorrow_Num'])
```

The output will look like this:

```
MinTemp             0.083107
MaxTemp            -0.155053
Rainfall            0.235811
Evaporation        -0.115656
Sunshine           -0.440916
WindGustSpeed       0.231923
WindSpeed9am        0.095216
WindSpeed3pm        0.089099
Humidity9am         0.251682
Humidity3pm         0.434908
Pressure9am        -0.238326
Pressure3pm        -0.218350
Cloud9am            0.315981
Cloud3pm            0.377142
Temp9am            -0.023916
Temp3pm            -0.186477
RainToday_Num       0.340036
RainTomorrow_Num    1.000000
```

Which variables have the most positive, most negative, and closest to zero correlations with `RainTomorrow_Num`?

Print the correlations for `Humidity3pm`. What variables are correlated with that field? Do those relationships make sense?

## Fit the logistic regression model

Let's start by fitting a simple model: can we predict rain tomorrow based on whether it rained today?

We'll use a subset of the `statsmodels` library called `smf` that can build models from a formula string. Here is the relevant code:

```
log_reg = smf.logit('RainTomorrow_Num ~ RainToday_Num', data=df).fit()
print(log_reg.summary())
```

The `smf.logit` function takes a string describing the model that we want to build. In this case,

```
RainTomorrow_Num ~ RainToday_Num
```

tells the function to build a model that predicts `RainTomorrow_Num` using `RainToday_Num` as the only dependent variable.

Fitting a logistic regression model is more complicated than fitting a simple least squares linear regression and requires using a numerical math technique called **maximum likelihood estimation** to find the best values for the parameters.

The `summary` method prints details on the fitted model, including confidence intervals for the parameters. A standard technique in social science and biostatistics is to build a logit model, then use its output to identify statistically significant variables.

## Calculate the confusion matrix

How good is this model? Consider this:

- A perfect mode would be one that classifies every test point correctly. That is, if the test point is really a 1, the model would always predict 1 and likewise if the test point is 0.

- But a real model probably isn't perfect and will **misclassify** some points. Misclassified points can be **false positives** (the model predicted a 1 but the real value is 0) or **false negatives** (the model predicted 0 when it should have predicted 1).

The **confusion matrix** compares the predicted and correct classifications for a set of testing data. To generate one for the logit model, use the following statement:

```
print(log_reg.pred_table(.5))
```

Recall that the logistic model always produces an output value between 0.0 and 1.0. The input to `pred_table` is a threshold used as a cutoff between the classes. In this case, anything with a logistic output less than .5 is assigned to class 0 and anything greater than .5 is assigned class 1. This is the most natural cutoff, but it's possible to use something other than .5 if necessary.

The output will look like the following:

```
[[110316.      0.]
 [ 35144.      0.]]
```

Interpreting this requires some work. The rows represent the **true classifications** for the points in the dataset. That is, the real, known value of the `RainTomorrow_Num` field. The columns represent the **predicted classification** determined by the model. Rewritte as a table,

```
                    Predicted
               0             1
           -------------------------
       0 |   110316          0
True     |
       1 |    35144          0

```

The output shows there were 110316 entries that had a true value of 0 where the model correctly predicted 0. These are the **true negatives**. There are another 35144 entries with a true value of 1 where the model incorrectly predicted 0. There are the **false negatives**.

The right column shows that there are no data points where the model predicted 1. That is, using only the single input `RainToday_Num`, it turns out that your best option is to simply predict that it will never rain in Australia. The fraction of correct predictions is

```
110316 / (110316 + 35144) = .7583
```

So simply predicting "No rain tomorrow" turns out to be correct around 75% of the time.

## Can we do better?

Experiment with adding more variables to the model and examining the results. For example, to add `Humidity3pm` to the model, use

```
log_reg = smf.logit('RainTomorrow_Num ~ RainToday_Num + Humidity3pm', data=df).fit()
print(log_reg.summary())
```

Examine the confusion matrix for that model and identify the numbers of true negatives, true positives, false negatives and false positives. What is the overall accuracy?
