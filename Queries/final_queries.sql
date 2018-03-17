use CryptoNews;

# top domains for a currency
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(link, '/', 3), '://', -1), '/', 1), '?', 1),'www.',-2) as domain, count(*) as frequency from cryptonews where content like '%bitcoin%' group by domain order by frequency desc;

# get quotes of a currency
select date(time) as t, quote from Value where currency_name='Bitcoin' group by t order by t;