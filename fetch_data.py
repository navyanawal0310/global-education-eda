import wbdata
import pandas as pd
from datetime import datetime

INDICATORS = {
    "SE.XPD.TOTL.GD.ZS": "education_spending_gdp",
    "SE.ADT.LITR.ZS": "adult_literacy",
    "SE.ADT.1524.LT.ZS": "youth_literacy",
    "SE.SEC.ENRR": "secondary_enrollment",
    "IT.NET.USER.ZS": "internet_users",
    "NY.GDP.PCAP.CD": "gdp_per_capita",
    "SP.URB.TOTL.IN.ZS": "urban_population"
}

def fetch_world_bank_data():
    print("Fetching data from World Bank API...")

    data_date = (datetime(2018, 1, 1), datetime(2023, 1, 1))

    df = wbdata.get_dataframe(INDICATORS, date=data_date)
    df = df.reset_index()

    df = df.sort_values("date").drop_duplicates(subset="country", keep="last")

    df = df.dropna(thresh=4) #too many missing values

    df.columns = df.columns.str.lower()

    print("Data fetched successfully.")
    print("Dataset shape:", df.shape)

    return df


if __name__ == "__main__":
    df = fetch_world_bank_data()
    df.to_csv("global_education_dataset.csv", index=False)
    print("Saved to global_education_dataset.csv")