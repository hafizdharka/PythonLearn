import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id']==views['viewer_id']][['author_id']]
    df = df.rename(columns={'author_id':'id'})
    df = df.sort_values('id',ascending=True)
    df = df.drop_duplicates()
    
    return df
    
