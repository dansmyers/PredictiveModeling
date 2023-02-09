
# Sprint 2 &ndash; Regression

<img src="https://imgs.xkcd.com/comics/fuck_grapefruit.png" width="50%" />

*Pineapples the clear outlier.*

## Starts Thursday, 2/9
## Deliverables and quiz are due on Wednesday, 2/22

## Overview and Goals

The first sprint was a warm-up and review of some familiar statistical concepts. We're now ready to go deeper and talk about two important, related modeling techniques.

This unit will cover:

- Revisiting the important concept of **regression**, with an emphasis on understanding the derivation of simple linear regression and the least squares approach.

- The concept of **classification** (also called "supervised learning") and examples of useful classification models.

- Our first two predictive modeling techniques, **K-Nearest Neighbors** and **logistic regression**, and concepts related to implementing a supervised learning model.

By the end of this unit, you will have a good command of the core concepts of supervised machine learning. We'll continue to introduce more techniques in the next two units.

## Reading

Complete the **participation questions** for chapters 6 (on regression) and 10 (supervised learning) in the ZyBook.

## Deliverables

In addition to the reading, complete the following:

- The Longbones lab in the `Examples` directory. Put all of your work in a file called `longbones.py` in the `Sprint 2` workspace.

- The logistic regression lab, also in `Examples`. We'll work through most of this one in class so I can explain some of the important concepts.

- The four miniprojects described in the `Deliverables` directory. Each one asks you to build a model that analyzes a dataset and draws some conclusions. For each model, put all your work in a single Python file in the sprint workspace. Your interpretations and conclusions can be given as comments in the Python scripts; you don't need to upload separate written documents.

## What You Need to Learn

The basics of linear regression, including:

- When linear regression is appropriate.

- The concept of deriving the line of best fit by minimizing the residual error. You don't need to memorize the derivation.

- Implementing linear regression and interpreting the output of the model.

- The r and R<sup>2</sup> measures.

For classification,

- The definition of supervised and unsupervised learning.

- The concept of K-nearest neighbors. We'll look at some examples in class, but you don't need to code this technique for the assignments.

- Creating and viewing a correlation matrix between variables in a dataset.

- The basic concept of logistic regression: how the model maps an input number into the range (0, 1), which can then be interpreted as a classification probability. We'll talk about this in class.

- Building and interpreting a logistic regression model.

- Evaluating the confusion matrix. In particular, identifying **false positives** and **false negatives** and the related concepts of specificity and sensitivity. Be able to calculate the overall accuracy of a model given a confusion matrix.

## Resources

The example labs are your main resource for the programming techniques that you need for the assginment.

[This article](https://towardsdatascience.com/linear-regression-derivation-d362ea3884c2) works through the math of deriving simple linear regression. [This video](https://www.youtube.com/watch?v=ewnc1cXJmGA) covers similar territory.

[This video](https://www.youtube.com/watch?v=VwVg9jCtqaU) from Google gives a high-level overview of machine learning and supervised learning. It's good background before you dig into the logistic regression lab.

The ZyBook reading does a good job of covering confusion matrix interpretation.

For background information on data mining, beyond the ZyBook, I recommend [these notes and slides](https://www-users.cs.umn.edu/~kumar001/dmbook/index.php) for the book
*Introduction to Data Mining* by Tan et al.

- Start with the slides for Chapter 3, although they quickly get into decision trees (we'll talk about those in the next unit).

- You can then look at the slides for KNN (Chapter 4) and basic clustering (Chapter 7).
