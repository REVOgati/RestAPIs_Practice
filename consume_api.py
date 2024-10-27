import requests
import json

response1 = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
#print(response1)
# [200] means response was successful and the specific resource was returned.
#print(response1.json())

#Explore items specifically

#print(response1.json()['items'])

#To print the specific question and links in each item

'''for data_x in response1.json()['items']:
    print(data_x['title'])
    print(data_x['link'])
    print(' ')
    '''
    
#Too print those questions where the answer count is less than 5

for data_x in response1.json()['items']:
    if data_x['answer_count'] < 5:  
        print(data_x['title'])
        print(data_x['link'])
        print(' ')
    
    else:
        print("skipped") # For those with more than 5 answers
    
    