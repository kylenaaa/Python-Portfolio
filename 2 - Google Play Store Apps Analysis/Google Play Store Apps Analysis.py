#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[5]:


df = pd.read_csv('googleplaystore.csv')
df.sample(3)


# In[6]:


df.info()


# # Data Cleaning

# ### Which of the following column(s) has/have null values?

# In[10]:


# Answers: Rating, Current Ver, Android Ver, Content Rating

df.isna().sum().sort_values(ascending=False)


# ### Clean the Rating column and the other columns containing null values.

# In[15]:


df['Rating'].plot(kind='hist', figsize=(10,4))

# All the ratings that are not in the range of 0 to 5 should be replaced with NaN.


# In[16]:


# Set the invalid values (out of the 1 to 5 range for Rating) to NaN:

df.loc[df['Rating'] > 5, 'Rating'] = np.nan

# Clean all NaN values:

# For Rating, which is numeric:
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())

# For the other columns
df.dropna(inplace=True)


# ### Clean the column Reviews and make it numeric.

# In[64]:


df['Reviews'] = pd.to_numeric(df['Reviews'])


# ### How many duplicated apps are there?

# In[19]:


# Answer is 1979

df['App'].duplicated(keep=False).sum()


# ### Drop duplicated apps keeping the ones with the greatest number of reviews.

# In[22]:


# Sort the dataframe and understand how the apps might be duplicated:

df_sorted = df.sort_values(by=['App', 'Reviews'])

df_sorted.loc[
df_sorted['App'].duplicated(keep=False) & ~df_sorted.duplicated(keep=False),
['App', 'Reviews']
].head(5)


# In[23]:


# Delete the duplicated apps and keep the last occurrence:

df_sorted.drop_duplicates(subset=['App'], keep='last', inplace=True)

df = df_sorted


# ### Format the Category column.

# In[26]:


# Categories are all uppercase and words are separated using underscores. Instead, we want them with capitalized in the first character and the underscores transformed as whitespaces.
## Any other wrong value must be transformed into an Unknown category.

df['Category'].value_counts()


# In[29]:


# To replace _ with a whitespace	
df.loc[df['Category'].str.contains('_'), 'Category'] = df.loc[df['Category'].str.contains('_'), 'Category'].str.replace('_', ' ')

# To capitalize
df['Category'] = df['Category'].str.capitalize()

# As 1.9 is a wrong category, we transform it into ""Unknown"" category
df.loc[df['Category'] == '1.9', 'Category'] = 'Unknown'


# In[47]:


df['Category'].value_counts()


# ### Clean and convert the Installs column to numeric type.

# In[48]:


df['Installs'].value_counts()


# In[49]:


df['Installs'] = df['Installs'].str.replace('+', '')
df['Installs'] = df['Installs'].str.replace(',', '')
df['Installs'] = pd.to_numeric(df['Installs'])


# ### Clean and convert the Size column to numeric (representing bytes).

# In[52]:


# Varies with device, we set it to 0

df['Size'] = df['Size'].replace('Varies with device', "0").astype(str)


# In[53]:


# Transform M to ~1M bytes

new_value = (pd.to_numeric(
df.loc[df['Size'].str.contains('M'), 'Size'].str.replace('M', '')
) * (1024 * 1024)).astype(str)
df.loc[df['Size'].str.contains('M'), 'Size'] = new_value


# In[54]:


# Transform `k` to ~1k bytes

new_value = (pd.to_numeric(
df.loc[df['Size'].str.contains('k'), 'Size'].str.replace('k', '')
) * 1024).astype(str)
df.loc[df['Size'].str.contains('k'), 'Size'] = new_value


# In[56]:


# Get rid of `+` and `,`

df['Size'] = df['Size'].str.replace('+', '')
df['Size'] = df['Size'].str.replace(',', '')

# Transform to numeric:

df['Size'] = pd.to_numeric(df['Size'])


# ### Clean and convert the Price column to numeric.

# In[57]:


df.loc[df['Price'] == 'Free', 'Price'] = "0"
df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '.')
df['Price'] = pd.to_numeric(df['Price'])


# ### Paid or free?

# In[59]:


# Create another auxiliary Distribution column.

df['Distribution'] = 'Free'
df.loc[df['Price'] > 0, 'Distribution'] = 'Paid'


# # Analysis

# ### Which app has the most reviews?

# In[65]:


# Answer is Facebook.

df[['App', 'Reviews']].sort_values(by=['Reviews'], ascending=False).head()


# ### What category has the highest number of apps uploaded to the store?

# In[66]:


# Answer is Family Category.

df['Category'].value_counts().head()


# ### To which category belongs the most expensive app?

# In[67]:


# Answer is in Lifestyle Category.

df.sort_values(by='Price', ascending=False).head()


# ### What's the name of the most expensive game?

# In[ ]:


# I'm Rich - Trump Edition


# ### Which is the most popular Finance App?

# In[68]:


# Answer is Google Pay.

df.loc[df['Category'] == 'Finance'].sort_values(by='Installs', ascending=False).head()


# ### What Teen Game has the most reviews?

# In[74]:


# Answer is Asphalt 8: Airborne.

df.loc[(df['Content Rating'] == 'Teen') & (df['Category'] == 'Game')].sort_values(by='Reviews', ascending=False).head()


# ### Which is the free game with the most reviews?

# In[75]:


# Answer is Clash of Clans.

df.loc[(df['Distribution'] == 'Free') & (df['Category'] == 'Game')].sort_values(by='Reviews', ascending=False).head()


# ### How many TB (terabytes) were transferred (overall) for the most popular Lifestyle app?

# In[78]:


# Answr is 6484

app = df.loc[df['Category'] == 'Lifestyle'].sort_values(by='Installs', ascending=False).iloc[0]

(app['Installs'] * app['Size']) / (1024 * 1024 * 1024 * 1024)


# In[ ]:




