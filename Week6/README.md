# LinkedIn Learning Week 6

## Date Methods Part 2

Time is often important value when it is available in a dataset. Dates or datetimes need to be parsed and structured properly before utilizing them. 

Pandas provides a couple options when it comes to establishing dates or datetimes in the datasets. When loading in a dataset from a csv, we can use pandas <code>read_csv</code> function passing the optional parameter <code>parse_dates</code> to establish the time. We can also pass <code> dayfirst </code> to specify the date or datetime format.
 
The time an action or event is recorded can show seasonality or opportunities when exploring the data. This is why it is important to properly set-up the values in the data. 
