# Challenge Project &ndash; Telco Customer Churn

<img src="https://compote.slate.com/images/6b1fe977-d4a8-4435-8d78-4988afa998c7.jpg" width="50%" />

## Due March 22

## Description

**Churn** is the term used in marketing and sales to describe a customer that ends a subscription and leaves for another provider. Minimizing churn is a major goal of any
business that operates on a subscription or recurring revenue model.

In this project, you'll work with a [data set from Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn) that includes customer churn information from a real 
telecom company. Your job is to load the data set into Pandas and perform an analysis, developing a model that can predict which customers are likely to churn. A company could use
an accurate churn-prediction model to identify customers that are at-risk of leaving and offer them special incentives or discounts in order to retain their business. 
Alternately, a model could be used to focus sales and marketing on customers that are likely to be long-term revenue generators.

You need to do the following:

- Start the project on repl.it, which includes the churn dataset

- Import the `.csv` file into a dataframe

- Perform a brief exploratory analysis: pick **two** features of the data that you suspect might be related to churn (for example, whether the customer is a senior citizen or not) 
and create plots showing the fraction of customers that churned vs. did not churn for each feature. For example, if you choose `SeniorCitizen` as a feature of interest, you would
want to show if there is any difference in the fraction of senior citizens that churned vs. non-senior citizens that churned.

- Hold out 20-30% of the data as a testing set, with the rest used as a training set. Look at the `train_test_split` function in the `Titanic` lab for an
example.

- Construct a predictive model for customer churn. You have the freedom to choose any technique that you think is appropriate (but you're probably going to make a decision tree).

- Create a **short** writeup summarizing the results of your exploratory analysis, your model, and a course of action that you would recommend taking based upon your analysis.

## Tips

- Note that there is a customer ID field in the data set. **Don't** include that in your model, or you'll be trying to classify customers based on their individual IDs.

- Do you need a training and test set? If you build a predictive model, it would make sense to hold out 20-30% of the data to show that your trained model can actually
make accurate predictions on data it hasn't seen before.
