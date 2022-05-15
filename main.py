import base64
import firebase_admin

from firebase_admin import firestore
from bs4 import BeautifulSoup
import requests

def main(self):
    
    firebase_admin.initialize_app()
    db = firestore.client()
    dict = {'postTitle' : [], 
            'price' : [],
            'condition' : [],
            'postTime' : [],
            'buyNowOption' : [],
            'bidOption' : [],
            'postLink' : []}
    titleList = []

    htmlText = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=rtx+3080&_sacat=0&_sop=10&_ipg=240').text
    soup = BeautifulSoup(htmlText, 'lxml')
    gpuListings = soup.find_all('li', class_ = 's-item s-item__pl-on-bottom s-item--watch-at-corner')

    for listing in gpuListings:
        #convert this to string
        postTitle = listing.find('h3', class_ = 's-item__title').text

        #price of item
        postPrice = listing.find('div', class_ = 's-item__detail s-item__detail--primary').span.text

        #if item condition information not present, print unknown
        if not listing.find('span', class_ = 'SECONDARY_INFO'):
            postCondition = 'Condition Unkown'
        else:
            postCondition = listing.find('span', class_ = 'SECONDARY_INFO').text

        #time item was posted
        postTime = listing.find('span', class_ = 'BOLD').text

        #if item doesnt have buy now option, print none
        if listing.find('span', class_ = 's-item__purchase-options-with-icon'):
            buyNow = listing.find('span', class_ = 's-item__purchase-options-with-icon').text
        else:
            buyNow = 'None'
        
        #if item does not have bid option, print deactivated
        if listing.find('span', class_ = 's-item__bids s-item__bidCount'):
            bid = listing.find('span', class_ = 's-item__bids s-item__bidCount').text
        else:
            bid = 'Deactivated'
        
        #link for item page
        link = listing.find('div', class_ = 's-item__info clearfix').a['href']

        titleList.append(postTitle)
        if (postTitle in titleList):
            if titleList.count(postTitle) > 1:
                titleList.pop()  
            else:
                dict['postTitle'] = postTitle
                dict['price'] = postPrice
                dict['condition'] = postCondition
                dict['postTime'] = postTime
                dict['buyNowOption'] = buyNow
                dict['bidOption'] = bid
                dict['postLink'] = link
                
    db.collection('Listing Information').add(dict)
    


    

