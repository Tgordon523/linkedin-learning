# LinkedIn Learning Week 10

## Date Methods Part 6

The data we receive is likely not always clean. In some cases, we might have information in sentences that need to be extracted. Date and time can be tricky to extract given the format. 

If the time format and sentence structure is standardized, the simple route would be using pandas string manipulation to separate the date and pass <code> to_datetime </code>. The arrow library can be helpful if the time format is consistent. 

This is an important step in retrieving data. Data provided could be direct from logs or complex spreadsheets which append a timestamp to multiple actions. This provides us the tools to measure these events. 
