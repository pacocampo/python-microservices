import webapp2
from paste import httpserver

class Goodbye(webapp2.RequestHandler):
    def get(self):
         self.response.write("Goodbye world! :)")

httpserver.serve(webapp2.WSGIApplication([('/', Goodbye)]), host='0.0.0.0', port='80')