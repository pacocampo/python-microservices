import webapp2
from paste import httpserver

class Hello(webapp2.RequestHandler):
    def get(self):
         self.response.write("Hello world! :)")

httpserver.serve(webapp2.WSGIApplication([('/', Hello)]), host='0.0.0.0', port='80')