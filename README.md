# Overview

The purpose of this project is to enhance my skills as a software engineer by performing a practical data analysis task on a real-world health dataset. By exploring the data programmatically, I aim to improve my ability to manipulate datasets, visualize trends, and extract meaningful insights that can support data-driven decision-making.

The dataset I analyzed is the Diabetes Dataset, which contains patient information including age, gender, BMI, hypertension, heart disease, smoking history, HbA1c levels, blood glucose levels, and whether the patient has diabetes. I added a couple of extra columns to indicate ethnicity and BMI category to determine where to classify individuals. The dataset was obtained from Kaggle: https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset

The purpose of creating this software was to analyze health-related factors that may contribute to diabetes, visualize patterns, and answer questions regarding correlations among several factors that could influence the likelihood of having diabetes.

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

Question 1: Does BMI category affect diabetes rates?

Patients in the Overweight and Obese BMI categories show significantly higher diabetes prevalence compared to those categorized as Healthy or Underweight.

This indicates that higher BMI is strongly associated with an increased risk of diabetes.

Question 2: Is smoking related to diabetes?

Current and former smokers tend to have higher diabetes rates compared to patients who never smoked.

While the effect is moderate, smoking history appears to contribute to a slightly higher likelihood of developing diabetes.

Question 3: Does age affect diabetes?

Diabetes prevalence increases with age. Patients in the older age groups (41-60, 61-80) show the highest rates.

Younger age groups (0-20, 21-40) have comparatively lower incidence of diabetes.

Question 4: How does the relationship between Age + BMI affect Diabetes?

Combining age and BMI reveals that older patients who are Overweight or Obese have the highest diabetes rates.

Younger patients with healthy BMI have the lowest prevalence, suggesting a compounding effect of age and BMI on diabetes risk.

# Development Environment

Programming Language: Python

Key Libraries:

pandas – for data manipulation and analysis

matplotlib – for data visualization

Development Tools:

Visual Studio Code for code editing

GitHub for version control and project management

# Useful Websites

Python 3.14.3 documentation: https://docs.python.org/3/

Kaggle Datasets: https://www.kaggle.com/datasets

Matplotlib: https://matplotlib.org/stable/users/index.html

Pandas Documentation: https://pandas.pydata.org/docs/

# Future Work

Implement more advanced data visualizations including interactive dashboards.

Add machine learning models to predict diabetes risk based on patient features.

Clean and preprocess missing or inconsistent data to improve analysis accuracy.

Extend analysis to include correlations and statistical tests between multiple health factors.
