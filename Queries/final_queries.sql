use CryptoNews;

# top domains for a currency
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(link, '/', 3), '://', -1), '/', 1), '?', 1),'www.',-2) as domain, count(*) as frequency from cryptonews where content like '%bitcoin%' group by domain order by frequency desc;

# get articles for currency on a given day.
select link, title from cryptonews where (title like '%bitcoin%' or content like '%bitcoin%') and date like '%2018-03-13%'; 

# get articles for currency on a given day.
select title,content from cryptonews where (title like '%bitcoin%' or content like '%bitcoin%') and date like '%2018-03-13%'; 

# get quotes of a currency
select date(time) as t, quote from Value where currency_name='Bitcoin' group by t order by t;