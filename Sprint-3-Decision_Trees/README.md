# Sprint 5 &ndash; Decision Trees
<img src="https://imgs.xkcd.com/comics/trained_a_neural_net_2x.png" width="30%" />

## Starts Thursday, 2/23
## Deliverables and quiz are due on Wednesday, 3/8

## Overview and Goals

Our main goal for this unit is to study two more important classification techniques: **decision trees** and **neural networks**.

A decision tree is a hierarchical flowchart where the leaves at the bottom of the tree represent classification decisions. Using a decision tree to classify an item is
straightforward: start at the top of the tree and work your way down, following the appropriate branch at each level based upon the features of the item under consideration.

<img src="https://upload.wikimedia.org/wikipedia/commons/e/eb/Decision_Tree.jpg" width="50%" />

>*Example decision tree for the Titanic data set. The numbers in each leaf node are the probability of survival and the total fraction of the data set associated with that outcome. 73% of women survived accounting for 36% of passengers. Men over the age of 9.5 were 61% of all passengers but had only a 17% survival rate.*

We're going to be interested in **building** decision trees from data. This is a supervised learning problem: given a set of labeled training examples, we'd like to 
construct the best possible decision tree for classifying them. This turns out to be an interesting problem, and along the way we'll get to learn a little bit of
information theory to explain why some trees are better than others.

Once we know how to build individual decision trees, we can use the powered-up version of decision tree learning: **random forests**, which creates a set of multiple
decision trees and combines their outputs to produce more robust classiication decisions.

## A Note on the Deliverables for this Unit

You have only one main project to solve for this unit and a few short questions that allow you to practice constructing decision trees. 
The main project is intentionally more open than some of our previous projects, but not that difficult.

I'm also assigning Challenge Project #1, which will have the same due date as the main project.


## Reading

Complete the **participation questions** for Chapter 12 of the Zybook on Decision Trees.

## Deliverables and Quiz

Complete the problems in `Deliverables`. Remember that you may work freely with the members of your team and you may use any resources that you find helpful to
complete the project.

**Remember that you have only two weeks to complete this sprint, so don't procrastinate!**

## Submission Instructions

Put your code and any other documents you create in the `Sprint 3` workspace on Repl.it.


## Resources

We'll mostly be working through material in class. In addition to the ZyBook, the main resource you'll want to look at are the notes from *Introduction to Data Mining* [link](https://www-users.cs.umn.edu/~kumar001/dmbook/index.php). Take a look at the text and slides for Chapter 3 on Decision Trees and the slides for Chapter 4 on neural networks.
These chapters contain a lot of material, so don't get bogged down in trying to understand every detail the first time you read them. In particular, you can lightly glide over
the derivations that require Calculus; we'll talk about the important concepts in class.

I recommend [this article](https://towardsdatascience.com/entropy-how-decision-trees-make-decisions-2946b9c18c8) for more details on the entropy measurement for determining decision splits.
