 def app(environ, start_response): 
     print('hello world')
     start_response('200 OK', [('Content-Type', 'text\plain')]) 
     qs = "\r\n".join(environ['QUERY_STRING'].split("&"))
     print (qs)
     return qs

# from urlparse import parse_qs


#def application(environ, start_response):
#    query = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
#    body = []
#    for key, value in query.items():
#        for item in value:
#            body.append(key + "=" + item + "\r\n")

 #   status = '200 OK'
 #   headers = [
 #       ('Content-Type', 'text/plain')
 #   ]

 #   start_response(status, headers)
 #   return body

# def app(environ, start_response): 
     # start_response('200 OK', [('Content-Type', 'text\plain')]) 
    # qs = "\r\n".join(environ['QUERY_STRING'].split("&"))
    # return qs
     
#    url=env['QUERY_STRING'] 
#    print('uRL ',url) 
#    start_response('200 OK', [('Content-Type', 'text/plain')]) 
#    return [url.replace('&','\n')] 

