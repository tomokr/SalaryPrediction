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

### Model 1: Adding degree and jobtype as variables
I think the degree and jobtype are also the key to predict the salary. It's because the means of salary and degree depend on what they are.

I applied one-hot encoding to "jobType" and "degree". Then I predict the relationship between salary with variables, which are years of experience, degree and jobtype.

### Model 2: Model1 + salary scaling
At first, scale saraly, then use model 1. This is because the distribution of salary is skewed.

### Model 3: All the features without companyID
All the features without companyID are considered as linearly correlated with salary.

## Develop
For all the model, I used ```LinearRegression``` for modeling.

The MSEs are listed below.
| Model # | MSE |
| ------------- | ------------- |
| 1  | 659.8  |
| 2  | 659.8  |
| 3  | 384.4  |

Now the model 3 is the best for MSE.

## Turning model 3
With using the features I used at model3, I tried some other regression.
The table shows the results.

| Regression Method | MSE |
| ------------- | ------------- |
| Linear Regression  | 384.4  |
| Random Forest  | 135.0  |
| SGD Regressor  | 1.681e22  |
| Gradient Boosting  | 736.8  |


