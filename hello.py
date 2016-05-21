def app(environ, start_response): 
     # start_response('200 OK', [('Content-Type', 'text\plain')]) 
    # qs = "\r\n".join(environ['QUERY_STRING'].split("&"))
    # return qs
     
    url=env['QUERY_STRING'] 
    print('uRL ',url) 
    start_response('200 OK', [('Content-Type', 'text/plain')]) 
    return [url.replace('&','\n')] 

