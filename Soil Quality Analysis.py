#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('C:/Users/RUVJA/OneDrive/Desktop/ArcheoByte/T1_Soil Quality analysis/archive (4)/soil_analysis_data.csv')


# In[3]:


data.head()


# In[4]:


data['Soil Quality'] = data[['pH Level', 'Organic Matter (%)', 'Nitrogen Content (kg/ha)', 
                             'Phosphorus Content (kg/ha)', 'Potassium Content (kg/ha)']].sum(axis=1)


# In[5]:


data['Soil Quality']


# In[6]:


grouped_data = data.groupby(['District', 'Soil Type'])


# In[7]:


mean_soil_quality = grouped_data.mean().reset_index()


# In[8]:


mean_soil_quality['Percentage Soil Quality'] = (mean_soil_quality['Soil Quality'] / mean_soil_quality['Soil Quality'].max()) * 100


# In[9]:


sorted_data = mean_soil_quality.sort_values(by='Percentage Soil Quality', ascending=False)


# In[10]:


sorted_data


# In[11]:


import seaborn as sns
import matplotlib.pyplot as plt

variables = ['pH Level', 'Organic Matter (%)', 'Nitrogen Content (kg/ha)', 'Phosphorus Content (kg/ha)', 'Potassium Content (kg/ha)']

for variable in variables:
    plt.figure(figsize=(8, 5))
    sns.barplot(x=variable, y='Percentage Soil Quality', data=sorted_data, palette='viridis')
    plt.title(f'{variable} vs. Percentage Soil Quality')
    plt.xlabel(variable)
    plt.ylabel('Percentage Soil Quality')
    plt.show()


# In[ ]:





# In[ ]:




