import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['check'] = (employees['employee_id'] %2 != 0) & (~employees['name'].str.startswith('M'))
    employees['bonus'] = employees['salary'].where(employees['check'],0)
    return employees[['employee_id','bonus']].sort_values('employee_id')
