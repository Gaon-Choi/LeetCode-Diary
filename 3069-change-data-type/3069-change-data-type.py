import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    result = students

    result["grade"] = result["grade"].astype('int')

    return result