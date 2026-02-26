import pandas as pd

# Pandas merging
def combine_two_tables(person, address):
    result = person.merge(address, on="personId", how="left")[["firstName", "lastName", "city", "state"]]

    return result    