#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('pokemon.csv')


# In[3]:


df.head()


# In[5]:


df.describe()


# # Distribution of Pokemon Types:

# In[60]:


df['Type 1'].value_counts().plot(kind='pie', title="Type 1 Pokemon", ylabel="", autopct='%1.1f%%', cmap='tab20c', figsize=(10, 8))

plt.savefig('Type 1 Pokemon Piechart.png')

plt.show()


# In[61]:


df['Type 2'].value_counts().plot(kind='pie', title="Type 2 Pokemon", ylabel="", autopct='%1.1f%%', cmap='tab20c', figsize=(10, 8))

plt.savefig('Type 2 Pokemon Piechart.png')

plt.show()


# # Distribution of Pokemon Totals:

# In[62]:


df['Total'].plot(kind='hist', title="Pokemon Totals", figsize=(5, 4))

plt.savefig('Pokemon Totals Histogram.png')

plt.show()


# In[63]:


df['Total'].plot(kind='box', title="Pokemon Totals", vert=False, figsize=(5, 4))

plt.savefig('Pokemon Totals Boxplot.png')

plt.show()


# # Distribution of Legendary Pokemons:

# In[64]:


df['Legendary'].value_counts().plot(kind='pie', title="Legendary Pokemon", ylabel="", autopct='%1.1f%%', cmap='Set3', figsize=(5, 4))

plt.savefig('Legendary Pokemon Piechart.png')

plt.show()


# # Basic Filtering

# ### How many Pokemons exist with an Attack value greater than 150?

# In[32]:


df.loc[df['Attack'] > 150]


# In[24]:


df.loc[df['Attack'] > 150].shape


# ### Answer is 18.

# In[25]:


sns.boxplot(data=df, x='Attack')


# ### Select all pokemons with a Speed of 10 or less.

# In[29]:


# Store your results in the variable slow_pokemons_df

slow_pokemons_df = df.query('Speed <= 10')

slow_pokemons_df


# ### How many Pokemons have a Sp. Def value of 25 or less?

# In[33]:


df.loc[df['Sp. Def'] <= 25]


# In[31]:


df.loc[df['Sp. Def'] <= 25].shape


# ### Answer is 18.

# ### Select all the Legendary pokemons.

# In[35]:


# Store your results in legendary_df

legendary_df = df.loc[df['Legendary']]

legendary_df.head()


# ### Find the outlier based on the scatter plot.

# In[40]:


ax = sns.scatterplot(data=df, x="Defense", y="Attack")
ax.annotate(
"Who's this guy?", xy=(228, 10), xytext=(150, 10), color='red',
arrowprops=dict(arrowstyle="->", color='red')
)


# In[41]:


df.query("Defense > 200")


# In[45]:


df.sort_values(by='Attack').head()


# ### Answer is Shuckle.

# # Advanced selection

# ### How many Fire-Flying Pokemons are there?

# In[47]:


# Answer is 6.

df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Flying')].shape


# ### How many 'Poison' pokemons are across both types?

# In[48]:


# Answer is 62.

df.loc[(df['Type 1'] == 'Poison') + (df['Type 2'] == 'Poison')].shape


# ### What pokemon of Type 1 Ice has the strongest defense?

# In[49]:


# Answer is Avalugg.

df.sort_values(by='Defense', ascending=False).loc[df['Type 1'] == "Ice"].head()


# ### What's the most common type of Legendary Pokemons?

# In[50]:


# Answer is Psychic.

df.loc[df['Legendary'],'Type 1'].value_counts()


# ### What's the most powerful pokemon from the first 3 generations, of type water?

# In[51]:


# Answer is KyogrePrimal Kyogre.

df.loc[df['Generation'].isin((1, 2, 3)) & (df['Type 1'] == 'Water')].sort_values(by='Total', ascending=False).head()


# ### What's the most powerful Dragon from the last two generations?

# In[53]:


# Answer is KyuremBlack Kyurem.

df.loc[(df['Generation'].isin((5,6))) & (df['Type 1'] == "Dragon") + (df['Type 2'] == "Dragon")].sort_values(by='Total', ascending=False).head()


# ### Select most powerful Fire-type pokemons.

# In[55]:


# Store your results in powerful_fire_df

powerful_fire_df = df.loc[(df['Type 1'] == 'Fire') & (df['Attack'] > 100)]

powerful_fire_df.head()


# ### Select all Water-type, Flying-type pokemons.

# In[56]:


# Store your results in water_flying_df

water_flying_df = df.loc[(df['Type 1'] == 'Water') & (df['Type 2'] == 'Flying')]

water_flying_df.head()


# ### Select specific columns of Legendary pokemons of type Fire.

# In[57]:


# Store your results in legendary_fire_df

legendary_fire_df = df[['Name','Attack','Generation']].loc[(df['Legendary']) & (df['Type 1'] == 'Fire')]

legendary_fire_df


# ### Select Slow and Fast pokemons.

# In[58]:


df.loc[(df['Speed'] < (df['Speed'].quantile(0.05))) + (df['Speed'] > (df['Speed'].quantile(0.95)))]


# ### Find the Ultra Powerful Legendary Pokemon.

# In[59]:


df.loc[(df['Legendary']) & (df['Defense'] > 125) & (df['Attack'] > 140)].sort_values(by='Total', ascending=False)

