import pandas as pd
from scipy import stats

data=pd.read_csv('hist_taxa_treat.txt', sep='\t', index_col=False, low_memory=False)

lacto=data.loc[(data['Species']=='Lactobacillus')]
#print(lacto)
x=lacto['Abundance']
print('lactos')
print(x)

para=data.loc[(data['Species']=='Parabacteroides')]
#print(para)
y=para['Abundance']
print('paras')
print(y)

tt_out=stats.ttest_ind(x,y)
print(tt_out)

#PRINT HEAD AND TAIL OF data

#MAKE species= the values in column 'Species'


#Use the describe function

#Print the sums, var, and std for data

#Make a new dataframe that only includes SampleID and Species.
#Make a second dataframe that only includes only Abundance.
#Make a third dataframe that merges the other two.



