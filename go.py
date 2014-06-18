#!/usr/bin/env python

import time
import cherrypy
from cherrypy._cpserver import Server

class Root(object):
  @cherrypy.expose
  def index(self):
    return "Hello World!"

if __name__ == '__main__':
  cherrypy.tree.mount(Root(), '/')
  cherrypy.engine.start()

  server = Server()
  server.socket_port = 8090
  server.subscribe()

  try:
    while True:
      print('Running')
      time.sleep(1)
  except KeyboardInterrupt as e:
    pass

  print('Shutting Down...')
  cherrypy.engine.exit()
  print('Bye!!')
