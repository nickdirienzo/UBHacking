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


class Hacker(ndb.Model):
  first_name=ndb.StringProperty()
  last_name=ndb.StringProperty()
  email=ndb.StringProperty()
  school=ndb.StringProperty()
  year=ndb.StringProperty()
  major=ndb.StringProperty()
  github=ndb.StringProperty()
  firstHackathon=ndb.BooleanProperty()
  dietaryRestrictions=ndb.StringProperty()
  shirtSize=ndb.StringProperty()
  resume=ndb.BlobProperty()
  date=ndb.DateTimeProperty(auto_now_add=True)


class MainHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render())


class RegistrationHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('register/index.html')
    self.response.write(template.render())


class SubmitHandler(webapp2.RequestHandler):
  def post(self):
    self.redirect('/success')


class SuccessHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('success/index.html')
    self.response.write(template.render())


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/register', RegistrationHandler),
  ('/submit', SubmitHandler),
  ('/success', SuccessHandler)
], debug=True)
