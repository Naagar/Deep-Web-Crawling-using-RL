import numpy as np
import random
import matplotlib.pyplot as plt
%matplotlib inline
from bs4 import BeautifulSoup # pulling data from HTML or XML files
import requests #for making HTTP requests in Python
from get_urls import get_urls
from get_reward import crawler, MySentences
initial_url = 'https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query=Injection&search_type=all&isCpeNameSearch=false'
# urls = 'https://nvd.nist.gov'
url_wiki = 'https://en.wikipedia.org/wiki/SQL_injection'
wiki_text = crawler(crawler)
# get the list of url to visit for web crawling
urls_list = get_urls(initial_url)

# calculate the similarity/ reward 
# reward = get_reward(url, url_wiki)

url =  'https://nvd.nist.gov' + urls_list[1] 

np.random.seed(5)    
n = 10 # no of pages fro start
arms = np.random.rand(n) # initial random values for the 10 websites
# print(arms)
# similarity 
eps = 0.1 #probability of exploration action, goto next page
# defining the reward using similarty of the visited page and wiki page
# print(similarity[0][0])
def reward(prob):
    reward = 0
    for i in range(10):
        similarity = get_reward(url, url_wiki)
        if similarity[0][0] > prob:
            reward += 1
    return reward
#initialize memory array; has 1 row defaulted to random action index
av = np.array([np.random.randint(0,(n+1)), 0]).reshape(1,2) #av = action-value
# print(av)
#greedy method to select best page based on memory array
def bestPage(a):
    bestPage = 0 #default to 0
    bestMean = 0
    for u in a:
        avg = np.mean(a[np.where(a[:,0] == u[0])][:, 1]) #calculate mean reward for each action
        if bestMean < avg:
            bestMean = avg
            bestPage = u[0]
    return bestPage


# plot the rewards and the visit of the page     
plt.xlabel("Number of times visit page")
plt.ylabel("Average Reward")
for i in range(500):
    if random.random() > eps: #greedy exploitation action
        choice = bestPage(av)
        thisAV = np.array([[choice, reward(arms[choice])]])
        av = np.concatenate((av, thisAV), axis=0)
    else: #exploration action
        choice = np.where(arms == np.random.choice(arms))[0][0]
        thisAV = np.array([[choice, reward(arms[choice])]]) #choice, reward
        av = np.concatenate((av, thisAV), axis=0) #add to our action-value memory array
    #calculate the mean reward
    runningMean = np.mean(av[:,1])
    plt.scatter(i, runningMean)