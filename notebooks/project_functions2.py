import pandas as pd
import numpy as np

def load_and_process(pathname):

    # Method Chain 1 (Load data and deal with missing data)

    s1 = (pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/masculinity-survey/raw-responses.csv")
.loc[:, ['q0011_0002',
 'q0012_0001',
 'q0012_0002',
 'q0012_0003',
 'q0012_0004',
 'q0012_0005',
 'q0012_0006',
 'q0012_0007',
 'q0015',
 'q0029',
 'q0034',
 'age3']]
.dropna().reset_index()
.drop('index', axis=1)
         )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    s2 = (
          s1
          .rename(columns={"q0011_0002" :"It’s a disadvantage to be a man at your work right now due to: Greater risk of being accused of sexual harassment","q0012_0001" :"Responded to a sexual harassment incident by: Confronted the accused person","q0012_0002" : "Responded to a sexual harassment incident by: :Contacted the HR department","q0012_0003": "Responded to a sexual harassment incident by: Contacted the manager of the accused person", "q0012_0004": "Responded to a sexual harassment incident by: Reached out to the victim to offer support","q0012_0005": "Responded to a sexual harassment incident by: Did not respond at all","q0012_0006": "Responded to a sexual harassment incident by: Never witnessed sexual harassment","q0012_0007": "Responded to a sexual harassment incident by: Other","q0015" : "As a man, would you say you think about your behavior at work differently in the wake of #MeToo?","q0029" :"What was the last school you completed?","q0034" : "What is your yearly income?","age3" : "How old are you?"})
.replace('Other (please specify)','Yes')
.replace('Confronted the accused person','Yes').replace('Contacted the HR department','Yes').replace('Contacted the manager of the accused person','Yes').replace('Reached out to the victim to offer support','Yes').replace('Did not respond at all','Yes').replace('Never witnessed sexual harassment','Yes').replace('Greater risk of being accused of sexual harassment','Yes').replace('Not selected','No')
.sort_values(by=['How old are you?'])
      )
    # Make sure to return the latest dataframe

    return s2 

load_and_process("https://raw.githubusercontent.com/fivethirtyeight/data/master/masculinity-survey/raw-responses.csv")