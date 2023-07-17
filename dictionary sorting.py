#!/usr/bin/env python
# coding: utf-8

# In[46]:


#sorting the dictionary by keys

dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0, 6:3, 5:9}
{k: v for k, v in sorted(dictionary.items(), key=lambda item: item[0])}


# In[ ]:





# In[ ]:





# In[47]:


#sorting the dictionary by values

dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0, 6:3, 5:9}
{k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}



# In[ ]:





# In[ ]:




