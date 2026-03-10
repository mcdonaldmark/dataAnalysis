import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("diabetesDataset.csv")

# Define BMI order
bmi_order = ["Underweight", "Healthy", "Overweight", "Obese"]

df["bmi_category"] = pd.Categorical(
    df["bmi_category"],
    categories=bmi_order,
    ordered=True
)

# Question 1: Does BMI category affect diabetes rates?

# Diabetes percentage by BMI category
bmi_diabetes = df.groupby("bmi_category")["diabetes"].mean() * 100

print("Diabetes Percentage by BMI Category:")
print(bmi_diabetes)

# Graph
bmi_diabetes.plot(kind="bar")
plt.title("Diabetes Rate by BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Diabetes Percentage")
plt.show()

print()

# Question 2: Is smoking related to diabetes?

smoking_diabetes = df.groupby("smoking_history")["diabetes"].mean() * 100

print("Diabetes Percentage by Smoking History:")
print(smoking_diabetes)

# Graph
smoking_diabetes.plot(kind="bar")
plt.title("Diabetes Rate by Smoking History")
plt.xlabel("Smoking History")
plt.ylabel("Diabetes Percentage")
plt.show()

print()

# Question 3: Does age affect diabetes?

bins = [0,20,40,60,80,100]
labels = ["0-20","21-40","41-60","61-80","81+"]

df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

age_diabetes = df.groupby("age_group")["diabetes"].mean() * 100

print("Diabetes Percentage by Age Group:")
print(age_diabetes)

# Graph
age_diabetes.plot(kind="bar")
plt.title("Diabetes Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Diabetes Percentage")
plt.show()

print()

# Question 4: Relationship between Age + BMI and Diabetes

# Create pivot table for graph
bmi_age_table = df.pivot_table(
    values="diabetes",
    index="age_group",
    columns="bmi_category",
    aggfunc="mean"
) * 100

print("Diabetes Percentage by Age Group and BMI Category:")
print(bmi_age_table)

# Graph
bmi_age_table.plot(kind="bar")

plt.title("Diabetes Rate by Age Group and BMI Category")
plt.xlabel("Age Group")
plt.ylabel("Diabetes Percentage")
plt.legend(title="BMI Category")

plt.show()

# Heatmap for visulization of relationships between BMI + Age and Diabetes

plt.figure()

plt.imshow(bmi_age_table)

plt.title("Diabetes Risk by Age Group and BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Age Group")

plt.xticks(range(len(bmi_age_table.columns)), bmi_age_table.columns)
plt.yticks(range(len(bmi_age_table.index)), bmi_age_table.index)

plt.colorbar(label="Diabetes Percentage")

plt.show()