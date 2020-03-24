from scipy import stats
x=[1,2,3,4,5]
y=[10,11,12,13,14]

print(stats.theilslopes(y,x))

kw_out=stats.kruskal(y,x)
print(kw_out)

tt_out=stats.ttest_ind(y,x)
print(tt_out)
