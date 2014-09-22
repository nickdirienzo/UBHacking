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
import json
import datetime

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
  try:
    hacker.first_name = self.request.get('firstname')
    hacker.last_name = self.request.get('lastname')
    hacker.email = self.request.get('email')
    hacker.school = self.request.get('school')
    hacker.major = self.request.get('major')
    hacker.github = self.request.get('github')
    if self.request.get('firstHackathon'):
      hacker.first_hackathon = 'yes'
    if self.request.get('vegetarian'):
      hacker.vegetarian  = 'yes'
    hacker.dietary_restrictions = self.request.get('dietaryRestrictions')
    hacker.shirt_size = self.request.get('shirtsize')
    hacker.time = datetime.strftime()
    hacker.put()
  except:
    return False
  return True


class Hacker(ndb.Model):
  first_name=ndb.StringProperty()
  last_name=ndb.StringProperty()
  email=ndb.StringProperty()
  school=ndb.StringProperty()
  major=ndb.StringProperty()
  github=ndb.StringProperty()
  first_hackathon=ndb.StringProperty()
  vegetarian=ndb.StringProperty()
  dietary_restrictions=ndb.StringProperty()
  shirt_size=ndb.StringProperty()
  date=ndb.StringProperty()


class MainHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('/template/home.html')
    self.response.write(template.render())


class RegistrationHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('/template/registration.html')
    self.response.write(template.render())


class SplashHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('/template/splash.html')
    self.response.write(template.render())


class SubmitHandler(webapp2.RequestHandler):
  def post(self):
    if processFormData(self):
      self.redirect("/successful")
    else :
      self.redirect("/unsuccessful")


class SuccessHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('/template/successful.html')
    self.response.write(template.render())


class UnsuccessHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('/template/unsuccessful.html')
    self.response.write(template.render())

class GetData(webapp2.RequestHandler):
  def get(self):
      queries = Hacker.query()
      hackers = []
      for query in queries:
        hackers.append(query.to_dict())
      self.response.headers["Content-Type"] = "application/json"
      self.response.write(json.dumps(hackers))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/register', RegistrationHandler),
  ('/submit', SubmitHandler),
  ('/successful', SuccessHandler),
  ('/unsuccessful', UnsuccessHandler),
  ('/getdata', GetData)
])
# app = webapp2.WSGIApplication([
#   ('/', SplashHandler)
# ])
