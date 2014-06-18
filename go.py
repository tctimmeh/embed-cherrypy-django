#!/usr/bin/env python
import os

import time

import cherrypy
from webapp.testproj.wsgi import application

def startWebServer():
  staticFilesPath = os.path.join(os.path.abspath(os.getcwd()), 'webapp', 'testapp', 'static')
  staticHandler = cherrypy.tools.staticdir.handler(section = '/', dir = '', root = staticFilesPath)

  cherrypy.tree.mount(staticHandler, '/static')
  cherrypy.tree.graft(application, '/')
  cherrypy.engine.start()

def stopWebServer():
  cherrypy.engine.exit()

def mainLoop():
  try:
    while True:
      print('Doing important things...')
      time.sleep(1)
  except KeyboardInterrupt as e:
    pass

if __name__ == '__main__':
  startWebServer()
  mainLoop()
  stopWebServer()

