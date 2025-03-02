import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # multiply by 2 into each rows of "salary"
    employees['salary'] *= 2

    return employees