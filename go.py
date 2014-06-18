#!/usr/bin/env python

import time

import cherrypy
from webapp.testproj.wsgi import application

def startWebServer():
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

