import pandas as pd

real_yields = pd.read_csv('../data/raw/monthly-realyields.csv', index_col =0, parse_dates = True)
nominal_yields = pd.read_csv('../data/raw/daily-yields.csv', index_col=0,parse_dates= True)
gold = pd.read_csv('../data/raw/monthly-gold.csv', index_col = 0, parse_dates = True)

#Change names of collumns and indexes
gold = gold.rename(columns = {'Price':'Gold Price'})
nominal_yields = nominal_yields.rename(columns = {'DGS10':'US10Y Yield'})
real_yields = real_yields.rename(columns = {'FII10' : 'Real Yield'})
real_yields.index = real_yields.index.rename('Date')
nominal_yields.index = nominal_yields.index.rename('Date')


#Calculate monthly mean for daily data and make dates allign
nominal_yields= nominal_yields.resample('ME').mean()
real_yields = real_yields.resample('ME').last()
gold = gold.resample('ME').last()


#Calculate change
gold['Gold Price (% Change)'] = gold['Gold Price'].pct_change()*100
nominal_yields['US10Y Yield (bp Change)'] = nominal_yields['US10Y Yield'].diff()*100
real_yields['Real Yield (bp Change)'] = real_yields['Real Yield'].diff()*100


#Gold and yields into one larger dataframe
comparison = gold.join([nominal_yields,real_yields], how = 'inner').dropna()


comparison.to_csv('../data/processed/full_table.csv')