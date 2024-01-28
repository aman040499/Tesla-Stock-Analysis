#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file = 'TSLA.csv'
tesla_stock_data = pd.read_csv(file)


# In[3]:


#checking if the data is loaded to the dataframe
tesla_stock_data.head()


# In[4]:


#this will check for the missing values for each column
tesla_stock_data.isnull().sum()


# In[5]:


#converting 'Date' to datetime format
tesla_stock_data['Date'] = pd.to_datetime(tesla_stock_data['Date'])


# In[7]:


tesla_stock_data.describe()


# In[8]:


#check if the date is converted to datetime format
tesla_stock_data.info()


# In[12]:


#ensuring the data is in chronological order
tesla_stock_data.sort_values(by='Date', inplace=True)


# In[11]:


# checking for any duplicates
print(tesla_stock_data.duplicated().sum())


# In[14]:


# Plotting line plot for analyzing if there are any outliers in the closing prices of Tesla's stock.
import matplotlib.pyplot as plt

# Plotting to visualize potential outliers in closing prices over time
plt.figure(figsize=(10, 6))
plt.plot(tesla_stock_data['Date'], tesla_stock_data['Close'])
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()


# In[ ]:





# In[18]:


tesla_stock_data.to_csv('C:/Tesla project files/tesla_stock_data.csv', index=False)


# In[ ]:




