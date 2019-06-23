 # prints the polarity and subjectivity of the statements
 # the next additions will analyse data from twitter
from textblob import TextBlob

feedback="the food at Mcdonals sucks"
feedback2="the food at Mcdonals was awesome"
blob=TextBlob(feedback)
blob2=TextBlob(feedback)

print(blob.sentiment)  # prints the polarity and subjectivity 
print(blob2.sentiment)
