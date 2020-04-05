#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[2]:


url = "https://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)


# In[3]:


soup = BeautifulSoup(html,'lxml') 


# In[4]:


print(type(soup))


# In[5]:


title = soup.title
print(title)


# In[7]:


soup.style


# In[8]:


print(soup.get_text)


# In[9]:


print(soup.link)


# In[10]:


soup.find_all('link')


# In[11]:


soup.find_all('a')


# In[12]:


soup.find_all('table')


# In[13]:


all_links = soup.find_all('a')
for link in all_links:
    print(link.get("href"))


# In[14]:


rows = soup.find_all('tr') # tr stands for TableRows
a = rows[:10]
for i in a:
    print(i)


# In[15]:


for row in a:     # td stans for TableCells
    row_td = row.find_all('td')
print(row_td)  


# In[16]:


str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells,'lxml').get_text()
print(cleantext)


# In[17]:


import re
list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean,'',str_cells))
    list_rows.append(clean2)
    print(clean2)


# In[18]:


df = pd.DataFrame(list_rows)
df.head(10)


# In[19]:


df1 = df[0].str.split(',',expand=True)
df1.head(10)


# In[20]:


df1[0] = df1[0].str.strip('[')
df1.head(10)


# In[21]:


col_labels = soup.find_all('th') # th stands for TableHeaders


# In[22]:


all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str,'lxml').get_text()
all_header.append(cleantext2)
print(all_header)


# In[23]:


df2 = pd.DataFrame(all_header)
df2.head()


# In[24]:


df3 = df2[0].str.split(',',expand = True)
df3.head()


# In[25]:


frames = [df3,df1]
df4 = pd.concat(frames)
df4.head(10)


# In[26]:


df5 = df4.rename(columns=df4.iloc[0])
df5.head()


# In[27]:


df6 = df5.dropna(axis=0,how='any')


# In[28]:


df7 = df6.drop(df6.index[0])
df7.head()


# In[32]:


df7.rename(columns={'[Place':'Place'},inplace = True)
df7.rename(columns={' Team]':'Team'},inplace=True)
df7.head()


# In[33]:


df7['Team']=df7['Team'].str.strip(']')
df7.head()


# In[34]:


df7[' Name']


# In[35]:


df7.shape


# In[36]:


df7.info()


# In[ ]:




