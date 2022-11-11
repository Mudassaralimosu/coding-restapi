import requests
import json


def topArticles(limit):

    # Set variables
    title = {}
    story_title = {}
    
    # comment_count
    comments = {}


    page = 1
    totalPages = 1
    index = 0

    while page <= totalPages:

        # make request for each page
        apiRequest = requests.get("https://jsonmock.hackerrank.com/api/articles?page="+str(page))
        articles = apiRequest.json()['data']

        # set totalPages value
        if page == 1:
            totalPages = apiRequest.json()['total_pages']

        
        for value in articles:
            title[index] = value['title']
            story_title[index] = value['story_title']
            if value['num_comments'] != None:
                comments[value['num_comments']] = index
            else:
                comments[0] = index
            index += 1
        
        

        page += 1

    
    # for i in range(limit):
    #     comm = comments.keys()
    #     max_comment = max(comm)
    #     # print(max_comment)

    #     if title[comments[max_comment]] != None:
    #         print(title[comments[max_comment]])
    #     else:
    #         print(story_title[comments[max_comment]])
        
    #     del comments[max_comment]

    
    comments = dict(sorted(comments.items(), reverse = True))
    comm = list(comments.keys())
    # print(comm[:limit])
    

    res = {}
    for i in range(limit):

        if title[comments[comm[i]]] != None :
            if comments[comm[i]] not in res:
                res[comments[comm[i]]] = list()
                res[comments[comm[i]]].append(title[comments[comm[i]]])
            else:
                res[comments[comm[i]]].append(title[comments[comm[i]]])
        else:
            if comments[comm[i]] not in res:
                res[comments[comm[i]]] = list()
                res[comments[comm[i]]].append(story_title[comments[comm[i]]])
            else:
                res[comments[comm[i]]].append(story_title[comments[comm[i]]])

    
    for key,value in res.items():
        for i in sorted(res[key]):
            print(i)


topArticles(2)