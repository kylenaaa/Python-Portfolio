#!/usr/bin/env python
# coding: utf-8

# #### In Anaconda Prompt

# In[ ]:


# C:\Users\Kyle>python
# C:\Users\Kyle>pip install mysql-connector-python
# import mysql
# quit()


# In[38]:


import mysql.connector


# In[39]:


db = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="123password",
    database ="coffee_park"
)


# In[40]:


cursor = db.cursor()


# In[44]:


cursor.execute('SELECT o.order_id, i.item_price, o.quantity, i.item_cat, i.item_name, o.created_at, a.del_address_1, a.del_city, a.del_zipcode, o.delivery FROM orders o LEFT JOIN items i ON o.item_id=i.item_id LEFT JOIN address a ON o.add_id=a.add_id;')

for x in cursor:
    print(x)

