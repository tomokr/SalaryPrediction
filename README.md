# SalaryPrediction

This is the salary prediction from job description.

The original data contains the features: job id, company id, job type, degree, major, industry, years of experience, miles from metropolis.
With using these features, I made a model for predicting the salary.

## Data cleaning

The original data didn't contain NaN or strange value.
Some of the job has 0 salary and I removed the ones.

## Exploring the data

There are two numerical variable; years of experience, miles from metropolis.
![numerical values relation](https://user-images.githubusercontent.com/5339011/74351853-b15ef180-4d85-11ea-9384-358a703f4d82.png)
From this table, you can see salary is positively correlated with years of experience and negatively correlated with miles from metropolis.

Also, I checked the relationships between salary and job type, degree, major and company id.
These graphs are the mean salary vs. job type, degree, major and company id.
![jobtype_vs_mean_salary](https://user-images.githubusercontent.com/5339011/74353146-7fe72580-4d87-11ea-8b1c-99a8bdf0a507.png)

