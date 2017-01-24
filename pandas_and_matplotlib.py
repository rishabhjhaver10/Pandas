from matplotlib import pyplot as plt
import pickle
import pandas as pd
from matplotlib import style
style.use('ggplot')

pickle_in = open('fifty_states_data.pickle', 'rb')
data = pickle.load(pickle_in)
data1 = data['TX']

plt.figure()
plt.plot(data['AK'])
plt.title('Housing Price Index AK')
plt.xlabel('Year')
plt.ylabel('Price')
plt.fill_between(data.index, data['AK'], data['AK'][0], where=(data['AK']>data['AK'][0]), facecolor='green', alpha=1)
plt.fill_between(data.index, data['AK'], data['AK'][0], where=(data['AK']<data['AK'][0]), facecolor='yellow', alpha=1)


plt.figure()
plt.plot(data['TX'])
plt.title('Housing Price Index TX')
plt.xlabel('Year')
plt.ylabel('Price')
plt.fill_between(data.index, data['TX'], 70, facecolor='blue', alpha=0.5)


plt.figure()
plt.scatter(data['TX'], data['WY'], color = 'orange')
plt.title('Texas vs Wyoming')
plt.xlabel('Texas')
plt.ylabel('Wyoming')
plt.show()