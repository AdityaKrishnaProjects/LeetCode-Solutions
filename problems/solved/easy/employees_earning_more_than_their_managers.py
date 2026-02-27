import pandas as pd

# dataframe management
def find_employees(employee):
    merged = employee.merge(
        employee,
        left_on="managerId",
        right_on="id",
    )

    result = merged[merged["salary_x"] > merged["salary_y"]]

    return result[["name_x"]].rename(columns={"name_x": "Employee"})