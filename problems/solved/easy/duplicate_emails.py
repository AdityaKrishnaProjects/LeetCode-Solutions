import pandas as pd

#pandas dataframes
def duplicate_emails(person: pd.Dataframe):
    duplicates = person[person.duplicated(subset=["email"])]

    return duplicates[["email"]].drop_duplicates()