# SalaryPrediction

This is the salary prediction from job description.

The original data contains the features: job id, company id, job type, degree, major, industry, years of experience, miles from metropolis.
With using these features, I made a model for predicting the salary.

## Data cleaning

The original data didn't contain NaN or strange value.
Some of the job has 0 salary and I removed the ones.

## Exploring the data

The distribution of salary looks like the graph below.

![salary](https://user-images.githubusercontent.com/5339011/74356121-d5253600-4d8b-11ea-980b-4c6a0c7e2cd5.png)

We can see a long tail on the right side.

There are two numerical variable; years of experience, miles from metropolis.

<img src="https://user-images.githubusercontent.com/5339011/74351853-b15ef180-4d85-11ea-9384-358a703f4d82.png" width="480">

From this table, you can see salary is positively correlated with years of experience and negatively correlated with miles from metropolis.

Also, I checked the relationships between salary and job type, degree, major and company id.
These graphs are the mean salary vs. job type, degree, major and company id.

![jobtype_vs_mean_salary](https://user-images.githubusercontent.com/5339011/74353146-7fe72580-4d87-11ea-8b1c-99a8bdf0a507.png)

![degree_vs_mean_salary](https://user-images.githubusercontent.com/5339011/74353823-77431f00-4d88-11ea-874c-ade3d54f55a7.png)

![major_vs_mean_salary](https://user-images.githubusercontent.com/5339011/74353830-79a57900-4d88-11ea-9617-85591ea82839.png)

![compid_vs_mean_salary](https://user-images.githubusercontent.com/5339011/74353833-7b6f3c80-4d88-11ea-9e45-6112376274d8.png)

Accoding to the means of categorical features, jobType and degrees are correlated with salary stronger than major and companyId.

## Establish a baseline
For the baseline, I decided to predict the salary only by the years of experience.
I used the ```LinearRegresson ``` to make a model
The MSE for this model is 1288.

## Hypothesize solution

I used all the features without companyId and encoded the categorical value.
Then I use these methods: Linear Regression, Gradient boosting and Random forest regressor.

## Develop
For all the model, the first trial MSEs are listed below.
Std means the standard deviation of MSE.
| Model  | MSE | Std  |
| ------------- | ------------- | ------------- |
| Linear regression  | 384  | 1.78 |
| Gradient boosting  | 375  | 1.82 |
| Random forest  | 466  | 1.50 |

Now Gradient boosting is the best.

## Turning Gradient boosting model
I tried tuning the number of estimators.

| # of estimators | MSE | Std |
| ------------- | ------------- | ------------- |
| 100 (default)  | 375  | 1.82 |
| 200  | 359  | 1.44 |
| 1000  | 355  | 1.45 |

When the number of estimators is 200 or 1000, the MSE is lower than 360.

## feature importance
Using the gradient boosting model with n_estimators=200, I checked the features importance.
Ignoring the categorical value, years of experience and miles from metropolis are the important features.

![feature_importance](https://user-images.githubusercontent.com/5339011/81083418-8670dd80-8f2f-11ea-81a2-d0aa5089f15f.png)
