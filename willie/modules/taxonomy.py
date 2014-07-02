
from willie import web

from willie.module import NOLIMIT, commands, example
import json
import re

REDIRECT = re.compile(r'^REDIRECT (.*)')

def mw_search(server, query, num):
    """
    Searches the specified MediaWiki server for the given query, and returns
    the specified number of results.
    """
    search_url = ('http://%s/w/api.php?format=json&action=query'
                  '&list=search&srlimit=%d&srprop=timestamp&srwhat=text'
                  '&srsearch=') % (server, num)
    search_url += web.quote(query.encode('utf-8'))
    query = json.loads(web.get(search_url))
    query = query['query']['search']
    return [r['title'] for r in query]


#action=parse

def mw_snippet(server, query):
    """
    Retrives a snippet of the specified length from the given page on the given
    server.
    """
    #snippet_url = ('https://en.wikipedia.org/w/api.php?format=json'
    #               '&action=query&prop=extracts&exintro&explaintext'
    #               '&exchars=300&redirects&titles=')
    
    snippet_url = ('http://en.wikipedia.org/w/api.php?action=parse'
                   '&format=json'
                   '&redirects'
                   '&text={{automatic taxobox|taxon = %s}}' % query)
    
    #print snippet_url
    
    #snippet_url += web.quote(query.encode('utf-8'))
    snippet = json.loads(web.get(snippet_url))
    
    print json.dumps( snippet_url )    
    print json.dumps( snippet )
    
    snippet = snippet['parse']['text']
    


    # For some reason, the API gives the page *number* as the key, so we just
    # grab the first page number in the results.
    snippet = snippet[snippet.keys()[0]]

    return snippet
    


def getpage( query):
    """
    Retrives a snippet of the specified length from the given page on the given
    server.
    """
    
    query = query.replace(' ', '_')
    
    snippet_url = ('http://en.wikipedia.org/wiki/'+query)
    
#    snippet_url += web.quote(query.encode('utf-8'))
    #snippet = json.loads(web.get(snippet_url))
    snippet = web.get(snippet_url)

    print ( snippet_url )    
    print ( snippet )
    return snippet
    

@commands('genus')
def genus(bot, trigger):
  query = trigger.group(2)
  
  if query == "" or query is None:
    bot.say("Why you asking for the genus temp of nuffin?")
  else:
    snippet = getpage( query)  
       
    m = re.search(r'<span class="genus" style="white-space:nowrap;"><i><a href="/wiki/(.*)" title="(.*)">(.*)</a></i></span>', snippet)

    if m:
      bot.say("Genus of "+query+" is '" + m.group(3) + "'") 
      return
    
    m = re.search(r'<span class="genus" style="white-space:nowrap;"><i><b>(.*)</b></i></span>', snippet)

    if m:
      bot.say("Genus of "+query+" is '" + m.group(1) + "'") 
      return
    
@commands('family')
def family(bot, trigger):
  query = trigger.group(2)
  
  if query == "" or query is None:
    bot.say("Why you asking for the family of nuffin?")
  else:
    snippet = getpage( query)  
       
    m = re.search(r'<span class="family" style="white-space:nowrap;"><a href="/wiki/(.*)" title="(.*)">(.*)</a></span>', snippet)

    if m:
      bot.say("Family of "+query+" is '" + m.group(3) + "'") 
      return  
       
    m = re.search(r'<span class="family" style="white-space:nowrap;"><b>(.*)</b></span>', snippet)

    if m:
      bot.say("Family of "+query+" is '" + m.group(1) + "'") 
      return
    
      
    

@commands('order')
def order(bot, trigger):
  query = trigger.group(2)
  
  if query == "" or query is None:
    bot.say("Why you asking for the order of nuffin?")
  else:
 

    snippet = getpage( query)  
       
    m = re.search(r'<span class="order" style="white-space:nowrap;"><a href="/wiki/(.*)" title="(.*)">(.*)</a></span>', snippet)

    if m:
      bot.say("Order of "+query+" is '" + m.group(3) + "'") 
      return
    
       
    m = re.search(r'<span class="order" style="white-space:nowrap;"><b>(.*)</b></span>', snippet)

    if m:
      bot.say("Order of "+query+" is '" + m.group(1) + "'") 
      return
         
    

@commands('kingdom')
def kingdom(bot, trigger):
  query = trigger.group(2)
  
  if query == "" or query is None:
    bot.say("Why you asking for the order of nuffin?")
  else:
 

    snippet = getpage( query)  
       
    m = re.search(r'<span class="kingdom" style="white-space:nowrap;"><a href="/wiki/(.*)" title="(.*)">(.*)</a></span>', snippet)

    if m:
      bot.say("Kingdom of "+query+" is '" + m.group(3) + "'") 
      return
    
       
    m = re.search(r'<span class="kingdom" style="white-space:nowrap;"><b>(.*)</b></span>', snippet)

    if m:
      bot.say("Kingdom of "+query+" is '" + m.group(1) + "'") 
      return
    
   
