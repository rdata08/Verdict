import csv
from textblob import TextBlob

def avg_question_count_by_race(filename):
    with open(filename, 'r') as voirdiredata:
        csv_reader = csv.reader(voirdiredata)
        
        # skips header of table
        next(csv_reader)

        hashMap = {}

        # quantifies number of questions asked to ind.
        totalCount = 0

        for row in csv_reader:
            race = row[2]
            q_count = int(row[7])
            totalCount += q_count
            if race in hashMap:
                hashMap[race] += q_count
            else:
                hashMap[race] = q_count
       
        ans = {}
        for race in hashMap:
            q_count = hashMap[race] 
            ans[race] = q_count / totalCount
            
        print(ans)
        return ans

def sentiment_by_race(filename):
    with open(filename, 'r') as voirdiredata:
        csv_reader = csv.reader(voirdiredata)
        
        # skips header of table
        next(csv_reader)  

        people = {}
        
        for row in csv_reader:
            question = row[6]
            person = row[0]
            
            blob = TextBlob(question)
            sentiment = blob.sentiment.polarity

            if person in people:
                people[person] += sentiment
            else:
                people[person] = sentiment
        
        for polarity in people.values():
            people[person] = polarity / get_question_count(person)
            
avg_question_count_by_race('voirdiredata.csv')
sentiment_by_race('voirdiredata.csv')
