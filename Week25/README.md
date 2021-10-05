# LinkedIn Learning Week 25

## Feature Selection

Select features with strong correlation. 

I use a custom function to select features with strong linearly correlation (positively/negatively >= .6) to the target.

This function helps by excluding features which may add noise to the model. Remember Correlation != causation