import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("global_education_dataset.csv")

print("Dataset Preview:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

if "date" in df.columns: #remove data col
    df = df.drop(columns=["date"])
focus_cols = [
    "education_spending_gdp",
    "internet_users",
    "gdp_per_capita",
    "adult_literacy",
    "secondary_enrollment"
]

corr = df[focus_cols].corr()

plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Focused Correlation Matrix - Key Education Indicators")
plt.savefig("focused_correlation_matrix.png")
plt.show()


plt.figure()
sns.scatterplot(
    x="education_spending_gdp",
    y="adult_literacy",
    data=df
)
plt.title("Education Spending vs Adult Literacy")
plt.xlabel("Education Spending (% GDP)")
plt.ylabel("Adult Literacy (%)")
plt.savefig("spending_vs_literacy.png")
plt.show()


plt.figure()
sns.scatterplot(
    x="education_spending_gdp",
    y="secondary_enrollment",
    data=df
)
plt.title("Education Spending vs Secondary Enrollment")
plt.savefig("spending_vs_enrollment.png")
plt.show()


plt.figure()
sns.scatterplot(
    x="internet_users",
    y="youth_literacy",
    data=df
)
plt.title("Internet Usage vs Youth Literacy")
plt.savefig("internet_vs_youth_literacy.png")
plt.show()


plt.figure()
sns.scatterplot(
    x="gdp_per_capita",
    y="education_spending_gdp",
    data=df
)
plt.title("GDP per Capita vs Education Spending")
plt.savefig("gdp_vs_spending.png")
plt.show()