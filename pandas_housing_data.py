#This code was built as a part of exercise from tutorial videos on www.pythonprogramming.net

import pandas as pd
import quandl 
import html5lib
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

#Getting the state abbreiations from wikipedia
def state_list(): 
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
    #print fiddy_states[0][0]

states = state_list()
main_df = pd.DataFrame()
with open('quandl_auth_token.txt') as f:
    token = f.read()

#Iterating over the state names and getting housing data from for each state from quandl
#Creating a dataframe with housing data from all 50 states    
for abbv in states:
    query = 'FMAC/HPI_' + abbv
    #print query
    df = quandl.get(query, authtoken= token)
    df.columns = [str(abbv)]
    #print df
    #df.set_index('date')
    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df)

#Storing data in a pickle file        
pickle_out = open('fifty_states_data.pickle', 'wb')
pickle.dump(main_df, pickle_out)
pickle_out.close()    


plt.plot(main_df['TX'])
plt.show()