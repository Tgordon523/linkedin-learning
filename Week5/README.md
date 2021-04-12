# LinkedIn Learning Week 5

## Date Methods

Time is often important value when it is available in a dataset. Dates or datetimes need to be parsed and structured properly before utilizing them. 

Pandas provides a couple options when it comes to establishing dates or datetimes in the datasets. With the dataset already in memory, we can use pandas <code>to_datetime</code> function to establish the time. This function requires at least the year, month, and day of the observation which can be passed all at once. If we are missing the day, we can pass a default value if working with only the year and month.
 
The time an action or event is recorded can show seasonality or opportunities when exploring the data. This is why it is important to properly set-up the values in the data. 
