import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    a = animals[animals['weight']>100]
    a = a.sort_values(by='weight',ascending=False)
    a = a[['name']]
    return a
    
