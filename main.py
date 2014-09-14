#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def processFormData(self):
  hacker = Hacker()
  hacker.first_name = self.request.get('firstname')
  hacker.last_name = self.request.get('lastname')
  hacker.email = self.request.get('email')
  hacker.school = self.request.get('school')
  hacker.major = self.request.get('major')
  hacker.github = self.request.get('github')
  if self.request.get('firstHackathon'):
    hacker.first_hackathon = True
  if self.request.get('vegetarian'):
    hacker.vegetarian  = True
  hacker.dietary_restrictions = self.request.get('dietaryRestrictions')
  hacker.shirt_size = self.request.get('shirtsize')
  hacker.resume = self.request.get('resume')
  hacker.put()
  return True


class Hacker(ndb.Model):
  first_name=ndb.StringProperty()
  last_name=ndb.StringProperty()
  email=ndb.StringProperty()
  school=ndb.StringProperty()
  major=ndb.StringProperty()
  github=ndb.StringProperty()
  first_hackathon=ndb.BooleanProperty()
  vegetarian=ndb.BooleanProperty()
  dietary_restrictions=ndb.StringProperty()
  shirt_size=ndb.StringProperty()
  resume=ndb.BlobProperty()
  date=ndb.DateTimeProperty(auto_now_add=True)


class MainHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('/template/home.html')
    self.response.write(template.render())


class RegistrationHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('/template/registration.html')
    self.response.write(template.render())


class SubmitHandler(webapp2.RequestHandler):
  def post(self):
    if processFormData(self):
      self.redirect("/success")
    else:
      self.response.write('uhhh...')

class SuccessHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('/template/success.html')
    self.response.write(template.render())


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/register', RegistrationHandler),
  ('/submit', SubmitHandler),
  ('/success', SuccessHandler)
], debug=True)
