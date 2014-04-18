import pandas
from math import log10, floor
 
def most_significant_digit(x):
    e = floor(log10(x))
    return int(x*10**-e)

def f(x):
    return most_significant_digit(abs(x))

# read in the ticker data
tick = pandas.read_csv('./your_ticker_data.csv')
tick_ret = tick.diff()
 
# count leading digits
data = tick_ret[tick_ret!=0]
counts = data.fillna(method='bfill').apply(f).value_counts()

total = counts.sum()
 
# expected number of each leading digit per Benford's law
benford = [total*log10(1 + 1./i) for i in range(1, 10)]


# plot actual vs expected
bins = np.arange(9)
error_config = {'ecolor': '0.3'}

r1 = plt.bar(bins, counts.values, 0.35, alpha=0.4, color='b', error_kw=error_config, label = 'actual')
r2 = plt.bar(bins + 0.35, benford, 0.35, alpha=0.4, color='r', error_kw=error_config, label = 'expected')
plt.xlabel('Most significant digit')
plt.ylabel('Occurence count')
plt.title('Leading digits in BTC-E ticker volume')
plt.xticks(bins + 0.35, bins+1)
plt.legend()

plt.show()

