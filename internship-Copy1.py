#!/usr/bin/env python
# coding: utf-8

# # Import the libraries

# In[2]:


import pandas as pd


# # Read the dataset
# 

# In[3]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.head()


# # Display all the columns of the dataset where datatypes,column name,count and overall memory

# In[4]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.info()


# # Find the total no of people based on their count age,income,gender

# In[53]:


dv["age"]=dv["age"]*50


# In[54]:


dv


# In[55]:


dv["income"]=dv["income"]*10000
dv


# # Find the value count of different data types

# In[8]:


dv["gender"].value_counts()


# In[10]:


dv["age"].value_counts()


# In[11]:


dv["visits"].value_counts()


# In[12]:


dv["illness"].value_counts()


# # Describing the info of the datatypes

# In[57]:


import pandas as pd


# In[56]:


dv.describe()


# In[15]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.dropna(axis = 1)


# In[16]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.fillna("15")


# In[17]:


dv.ffill(axis = 1)


# In[18]:


dv.bfill(axis = 1)


# In[19]:


dv.drop_duplicates()


# In[20]:


dv.drop_duplicates(subset=['private'])


# In[21]:


dv.drop_duplicates(subset=['freerepat','illness'])


# In[22]:


dv.shape


# In[23]:


dv.columns


# In[24]:


dv.isna().sum()


# # Analyzing the variables
# 

# In[25]:


import pandas as pd
dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.visits.unique()


# In[26]:


dv.gender.unique()


# In[27]:


dv.freerepat.unique()


# In[28]:


dv.private.unique()


# In[29]:


dv.nchronic.unique()


# In[30]:


dv.age.unique()


# In[31]:


dv.income.unique()


# In[32]:


dv.nunique()


# # Exploring and Plotting the data

# In[33]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[35]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.head()


# In[58]:


sns.histplot(dv['age'], bins=50)


# In[37]:


sns.histplot(dv['age'], bins=15)
plt.xlabel('Age')
plt.ylabel('visit')
plt.title('Distribution of Patients Ages')
plt.show


# In[38]:


gender_counts = dv['gender'].value_counts()
sns.barplot(x=gender_counts.index,y=gender_counts.values)
plt.xlabel('gender')
plt.ylabel('visit')
plt.title('Distribution of Patient Gender')
plt.show()


# In[59]:


sns.histplot(dv['visits'], bins=20)
plt.xlabel('visits')
plt.ylabel('income')
plt.title('visit analysis')
plt.show


# In[60]:


labels=['visits','illness','reduced','health']
sizes=[25,20,13,6]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[41]:


x = [14,12,16,18,20]
y = [12,16,18,10,8]
plt.plot(x,y)
plt.xlabel('nchronic')
plt.ylabel('Ichronic')
plt.title('Disease analysis')
plt.show()


# In[61]:


labels=['freerepat','freepoor']
sizes=[50,40]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('patient health insurance analysis')
plt.show()


# In[62]:


labels=['visits','illness']
sizes=[40,50]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[44]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[63]:


labels=['visits','illness','reduced','health']
sizes=[20,15,12,5]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[64]:


x = [15,65,50,85,15]
y = [20,35,50,65,60]
plt.scatter(x,y)
plt.xlabel('freepoor')
plt.ylabel('private')
plt.title('insurance analysis')
plt.show()


# In[47]:


import pandas as pd
dv=pd.read_excel("DoctorVisits (2).xlsx")


# In[65]:


dv.hist(figsize=(25,20))


# In[66]:


x= (dv[['health']]==1).sum()
y= (dv[['health']]==0).sum()
percent= ((x*y)/(x+y))*100
percent


# # Conclusion
# 

# #1) We analyzed the dataset which is about the visiting of patients to doctor.
# 

# #2) We analyzed all the variables of the dataset.
# 

# #3) Female gender is more in number comparable to male gender
# 

# #4) Income doesn't create any kind of difference in the dataset it made it's consistency path asusally
#  

# #5) Coming to the factor of age condition and health condition those are some what creating some kind of difference in the analytics.
# 

# #6) NO,Any patient doesn't belongs to freepoor as they didn't get any help from the government due to their low income.
# 

# #7) Many diseases are lchronic rather than nchronic.
# 

# #8) The reduced factor more equivalent to illness factor.
# 

# #9) Private doesn't play much role in the dataset.

# In[ ]:




