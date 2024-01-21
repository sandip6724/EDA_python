#!/usr/bin/env python
# coding: utf-8

# In[1]:


from warnings import filterwarnings
filterwarnings('ignore')


# In[2]:


import os
os.chdir('E:/Datasets/')


# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv('laptopPrice.csv')
df.head()


# In[5]:


df.shape


# In[6]:


df.columns


# ### Step 2: Data Quality Check

# In[7]:


df.info()


# In[8]:


df.duplicated().sum()


# ### Drop the duplicates

# In[9]:


df = df.drop_duplicates(keep='first')
df.head()


# In[10]:


df.duplicated().sum()


# ### Cat con seperation for df

# In[11]:


df.columns


# In[12]:


df.dtypes


# In[13]:


cat =list(df.columns[df.dtypes=='object'])
cat


# In[14]:


con = list(df.columns[df.dtypes!='object'])
con


# ### Perform descriptive analytics for cat and con features

# In[15]:


df[cat].describe().T


# In[16]:


df['os'].value_counts()


# In[17]:


df[con].describe().T


# In[18]:


df['Price'].value_counts()


# ### Perform Data Visualization

# In[19]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[20]:


for i in cat:
    plt.figure(figsize=(12,6))
    sns.countplot(data=df,x=i)
    plt.title(f'count plot for {i}')
    plt.show()


# In[21]:


for i in con:
    plt.figure(figsize=(12,5))
    sns.histplot(data=df,x=i,kde=True)
    plt.title(f'countplot for {i}')
    plt.show()


# ### Multivariate analysis

# ![image.png](attachment:image.png)

# In[22]:


con


# In[23]:


plt.figure(figsize=(12,6))
sns.scatterplot(data=df,x='Number of Ratings',y='Price')
plt.title(f'scatterplot for no of Rating v price')
plt.show()


# ### Number of ratings and Number of Reviews are Linearly dependent on each other

# #### Correlation Plot

# In[24]:


cor = df[con].corr()


# In[25]:


cor


# In[26]:


sns.heatmap(cor,annot=True)
plt.show()


# In[27]:


sns.boxplot(data=df,x='brand',y='Price')
plt.show()


# In[28]:


cat


# In[29]:


con


# In[30]:


plt.figure(figsize=(12,6))
sns.boxplot(data=df,x='brand',y='Price')
plt.title(f'Boxplot for LAPTOP BRAND vs PRICE')
plt.show()


# In[31]:


for i in cat:
    plt.figure(figsize=(12,6))
    sns.boxplot(data=df,x=i,y='Price')
    plt.title(f'Boxplot for {i} vs PRICE')
    plt.show()


# ### Cateogical vs Categorical - Crosstab heatmap

# In[32]:


cat


# In[33]:


ctab1 = pd.crosstab(df['processor_brand'],df[ 'processor_gnrtn'])
ctab1


# In[34]:


sns.heatmap(ctab1,annot=True, fmt='d')
plt.show()


# In[35]:


ctab2 = pd.crosstab(df['brand'],df['rating'])
ctab2


# In[36]:


sns.heatmap(ctab2, annot=True, fmt='d')


# ### Multivarite analysis - Pairplot

# In[37]:


sns.pairplot(data=df)


# In[38]:


cat


# In[39]:


sns.pairplot(data=df,hue='processor_brand')
plt.show()


# In[40]:


sns.pairplot(data=df,hue='Touchscreen')


# # EDA for tips datasets

# In[41]:


import os
os.chdir('E:/Datasets/')


# In[42]:


df1 = pd.read_csv('tips.csv')


# In[44]:


df1.head()


# In[47]:


list(df1.columns)


# In[48]:


df1.isna().sum()


# In[57]:


df1.duplicated().sum()


# In[58]:


D = df1.drop_duplicates(keep='first')


# In[140]:


df1


# In[61]:


D.duplicated().sum()


# In[62]:


D.dtypes


# In[63]:


D.info()


# In[65]:


cat = list(D.columns[D.dtypes=='object'])
cat


# In[68]:


con = list(D.columns[D.dtypes!='object' ])
con


# In[75]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[115]:


D = df
D


# In[116]:


cat


# In[117]:


con


# ## Univariate plot

# In[105]:


plt.figure(figsize=(12, 6))
sns.countplot(data=D, x='smoker')
plt.title('Countplot for Smoker')
plt.show()


# In[143]:


plt.figure(figsize=(12,6))
sns.countplot(data=df1,x='total_bill')
plt.show()


# In[127]:


df


# In[141]:


plt.figure(figsize=(12,6))
sns.countplot(data=df1, x ='day')
plt.show()


# In[151]:


sns.countplot(data=df1,x='tip')
plt.show()


# In[ ]:




