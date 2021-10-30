def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
    pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/masculinity-survey/raw-responses.csv', usecols=['q0002','q0010_0001','q0010_0002','q0010_0003','q0010_0004','q0010_0005','q0010_0006','q0010_0007','q0010_0008'])
    .dropna()
      )

    # Method Chain 2 (Renaming , replacing varibles )

    df2 = (
    df1
     .rename(columns={"q0002": "Importance of being seen as masculine" , "q0010_0001": "Men make more money" , "q0010_0002": "Men are taken more seriously" , "q0010_0003": "Men have more choice","q0010_0004": "Men have more promotion/professional development opportunities","q0010_0005": "Men are explicitly praised more often", "q0010_0006":"Men have more support from their managers","q0010_0007":"Other" , "q0010_0008":"None of the Above"})
     .replace(cleanup_nums)
      )

    # Make sure to return the latest dataframe

    return df2 

df2




def load_and_processing(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df11 = (
    pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/masculinity-survey/raw-responses.csv', usecols=['q0002','q0011_0001','q0011_0002','q0011_0003','q0011_0004','q0011_0005'])
      .dropna()
      )

    # Method Chain 2 (Renaming , replacing varibles )

    df11_2 = (
    df11
     .rename(columns={"q0002":"Importance of being seen as masculine","q0011_0001": "Managers want to hire and promote women" , "q0011_0002": "Greater risk of being accused of sexual harassment" , "q0011_0003":"Greater risk of being accused of being sexist or racist" , "q0011_0004":"Other", "q0011_0005":"None of the above"})
     .replace(cleanup_nums)
      )

    # Make sure to return the latest dataframe

    return df11_2 