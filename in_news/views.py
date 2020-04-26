from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def news(request):
    
    if (request.GET.get('submit')):

        print('hei button working')


        api_key='d784d7159f1a434a9859d80398034d8f'

        newsapi = NewsApiClient(api_key)

        top_headlines = newsapi.get_top_headlines(q='covid-19',
                                            #   sources='bbc-news,the-verge',
                                            #   category='business',
                                            language='en',
                                            country='in')

        articles = top_headlines['articles']

        my_lst=[]
    
        for x,y in enumerate(articles):
            # print(f'{x}      {y["title"]}')
            my_lst.append((x,y["title"]))
            # print(x,y["title"])
        # print(my_lst)
        # print(*my_lst, sep = "\n") 
        

        return render(request,'in_news/news.html',{'articles':articles,'my_lst':my_lst})

    else:
        print('button not clicked')


    # for x,y in enumerate(articles):
    #     print(f'{x}      {y["title"]}')

    # # print(top_headlines)

    return render(request,'in_news/news.html')
