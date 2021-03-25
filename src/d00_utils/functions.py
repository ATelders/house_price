def columns_with_missing_values(dataframe, coef) :
    '''
    Returns a list of columns with more than a coefficient of missing values.
    i.e. coef=0.3 : 30% 
    '''
    columns = []
    for column in dataframe :
        if dataframe[column].isna().sum() / dataframe.shape[0] > coef :
            columns.append(column)
    return columns
