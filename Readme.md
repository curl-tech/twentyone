# TwentyOne - 21



<img src="https://github.com/pooja-bs-3003/twentyone/raw/main/imgs/21_logo.png" alt="logo" style="zoom: 80%;" />

---

Project 21 is an AutoML engine that aims to make the life of Data Scientists a lot easier by automating the process of generating, tuning and testing the best model according to their dataset.
You provide the data, we provide the best model along with the required expertise to get you started in the field of ML.

Get started now!
[Note: Project 21 is a work in progress. This repo will undergo major changes in the coming months]

---

To run the project do the following - 
1. Fork this repository.

2. `git clone <url>` - put the url of your forked repo.

3. Create a virtual environment inside the project folder using the following:
   
   ```shell
   python3 -m venv venv
   ```
   
4. Activate the virtual environment using:

   ```shell
   source venv/bin/activate
   ```

5. Once the environment is activated, install the dependencies using:

   ```shell
   pip3 install -r requirements.txt
   ```

---

# Table of Contents

-  [Getting Started](# Getting-Started)

-  [Architecture of Auto ML 21](## BLOCKS)

-  [Features of Auto ML 21](# Features-of-Auto-ML-21)

-  [ML Models](# ML-Models)

  # Getting Started

  

  
  ![](/home/pooja/Downloads/twentyone (1).jpeg)





# Architecture of AUTO ML 21

## BLOCKS

### Main concepts

1. Task: task includes the problem type (classification, regression,  seq2seq), the pointer to the data and evaluation metric to be used to  build a model.
2. Data: data holds the raw content and the meta information about the  type of data (text, images, tabular etc.) and its characteristics (size, target, names, how to process etc).
3. Model: is either a machine learning or time series or deep learning model which is needed to learn the relation in the data.
4. Model Universe: is a collection of models, its hyper parameters and the tasks to which it has to be considered.

![top](https://github.com/pooja-bs-3003/twentyone/raw/main/imgs/Blocks.PNG)



## Top level architecture of TwentyOne



![top](https://github.com/pooja-bs-3003/twentyone/raw/main/imgs/top.PNG)

Top level architecture provides how things works in twentyone.



# Features of Auto ML 21

- TwentyOne is designed to leverage transfer learning as much as possible. For  many problems the data requirement for 21 is minimal. This saves a lot  of time, effort and cost in data collection. Model training is also  greatly reduced.

- TwentyOne tries to be an auto ML engine, it can be used as an augmented ML  engine which can help data scientist to quickly develop models. This can bring best of both worlds leading to "Real Intelligence = Artificial  Intelligence + Human Intelligence"

- 21 builds "Robust Models"

  

  <img src="https://www.pngitem.com/pimgs/m/72-726551_shocked-emoji-omg-freetoedit-wow-emoji-hd-png.png" alt="Shocked Emoji Omg Freetoedit - Wow Emoji, HD Png Download , Transparent Png  Image - PNGitem" style="zoom: 33%;" />21 requires less amount of data  

- Cost for development is minimal (mainly compute cost, rest is reduced).

- 21 provides Data Security and Privacy

- 21 takes less amount of time to build a model.

  

  # ML Models

  In 21 user can build two categories of machine learning models. They are:

  - **CLASSIFICATION**

  - **REGRESSION**

    

    ### CLASSIFICATION

    Machine learning algorithms is to recognize objects and being able to  separate them into categories. This process is called classification,  and it helps us segregate vast quantities of data into discrete values,  i.e. :distinct, like 0/1, True/False, or a pre-defined output label  class.

    ![Machine Learning: Types of Classification Algorithms](https://serokell.io/files/fx/fxpez2t8.7_(4)_(1).jpg)

    

  

## Logistic Regression

- Logistic regression is a supervised learning classification algorithm  used to predict the probability of a target variable. The nature of  target or dependent variable is dichotomous, which means there would be  only two possible classes.

- It is one of the simplest ML algorithms that can be used for various  classification problems such as spam detection, Diabetes prediction,  cancer detection etc.

- Metrics to evaluate a logistic regression model such as confusion matrix, ROC curve.

- **Confusion Matrix:** It is nothing but a tabular representation of Actual vs Predicted  values. This helps us to find the accuracy of the model and avoid  overfitting. 

  

  

  ## ![How to Remember all these Classification Concepts forever | by Jerry An |  The Startup | Medium](https://miro.medium.com/max/1200/0*-oGC3SE8sPCPdmxs.jpg)

- **ROC Curve:** Receiver Operating Characteristic(ROC) summarizes the model’s performance by  evaluating the trade offs between true positive rate (sensitivity) and  false positive rate(1- specificity).

- The area under curve (AUC), referred to as index of accuracy(A) or  concordance index, is a perfect performance metric for ROC curve. Higher the area under curve, better the prediction power of the model.

  

  ![logitstic regression, roc curve, logit function](https://www.analyticsvidhya.com/wp-content/uploads/2015/11/logit_roc-300x292.png)

##  Naive Bayes

- Naive Bayes methods are a set of supervised learning algorithms based on applying Bayes’ theorem with the “naive” assumption of conditional independence between every pair of features given the value of the class variable.
- Performance of Naive Bayes is evaluated by accuracy,precision,re-call, f1-score,confusion matrix & ROC Curve.

## Decision Tree

- Decision Tree is a **Supervised learning technique**  that can be used for both classification and Regression problems. It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.

- In a Decision tree, there are two nodes, which are the **Decision Node** and **Leaf Node.** Decision nodes are used to make any decision and have multiple  branches, whereas Leaf nodes are the output of those decisions and do  not contain any further branches. 

  ### Performance metrics for Decision Tree

  

  

<img src="https://www.researchgate.net/profile/Celestine-Iwendi/publication/342410608/figure/fig3/AS:909206194507778@1593783057258/Evaluation-metrics-for-decision-tree.png" alt="| Evaluation metrics for decision tree." style="zoom:50%;" />

# Random Forest

- Random forests creates decision trees on randomly selected data samples, gets prediction from each tree and selects the best solution by means  of voting. It also provides a pretty good indicator of the feature  importance.

- It runs efficiently on large data bases and gives estimates of what variables are important in the classification.         

  <img src="https://builtin.com/sites/default/files/styles/ckeditor_optimize/public/inline-images/two-tree-random-forest.png" alt="two tree random forest" style="zoom:50%;" />

- Performance of random forest is evaluated by Precision, Recall, F1-score & Accuracy.

## Regression

- Regression is a supervised learning technique which helps in finding the correlation between variables and enables us to predict the continuous output variable based on the one or more  predictor variables.
- Regression shows a line or curve that passes through all the datapoints on target-predictor graph in such a way that the vertical  distance between the datapoints and the regression line is minimum.
- Regression Algorithms are Linear Regression,Polynomial Regression, Support Vector Regressor,Random Forest,Decision Tree & K-NearestNeighbors.

## Linear Regression

- Linear Regression is a supervised machine learning algorithm where the predicted output is continuous and has a constant slope.

- Linear regression shows the linear relationship, which means it finds  how the value of the dependent variable is changing according to the  value of the independent variable.

  

<img src="https://static.javatpoint.com/tutorial/machine-learning/images/linear-regression-in-machine-learning.png" alt="Linear Regression in Machine Learning" style="zoom:50%;" />

- Evaluation metrics are a measure of how good a model performs and how well it approximates the relationship. The table below  shows performance metrics for

  regression.

   

  ![How to evaluate regression models? | by Vimarsh Karbhari | Acing AI | Medium](https://miro.medium.com/max/2524/1*G6aSSAJuMDF5RYvPeKqPzg.png)

  #### 

## Polynomial Regression

- Polynomial Regression is a regression algorithm that models the  relationship between a dependent(y) and independent variable(x) as nth  degree polynomial. The Polynomial Regression equation is given below:

```
y= b0+b1x1+ b2x12+ b2x13+...... bnx1n
```

- In Polynomial regression, the original features are  converted into Polynomial features of required degree (2,3,..,n) and  then modeled using a linear model.

  -  The graph below shows different between linear & polynomial regression.

  ![ML Polynomial Regression](https://static.javatpoint.com/tutorial/machine-learning/images/machine-learning-polynomial-regression.png)

## Support Vector Machine

- Support Vector Machine or SVM is one of the most popular Supervised  Learning algorithms, which is used for Classification as well as  Regression problems.

- The goal of the SVM algorithm is to create the best line or decision  boundary that can segregate n-dimensional space into classes so that we  can easily put the new data point in the correct category in the future. This best decision boundary is called a hyperplane.

  

  <img src="https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm.png" alt="Support Vector Machine Algorithm" style="zoom:67%;" />

### Maintained By

This repo is maintained by  **Shivaramkrs** curl team members and contibutors **NikhilAgarwal**, **Paarth S Barkur**, **Pooja BS**, **Rishabh Bhatt** & **Shubham Kumar Shaw**.
