# LinkedIn Learning Week 7

## Date Methods Part 3

Time is often important value when it is available in a dataset. A dataset could show trends over time or anomalities. 

In pandas, we can subset the data to separate specific time periods. Date subsetting can be passed with either a string or datetime <code>df[df.date > '2019-01-01']</code>. Another powerful datetime tool in Python is the Arrow library. With Arrow, we can subset a specific time period using <code>shift</code> to specific the parameters and <code>naive</code> to return the Arrow data type as datetime. 
 
With the date or datetime properly established, we might be interested in looking at specific time periods. With time period forecasting, it is common to save the last set of of dates in the time frame to validate predictions. 
