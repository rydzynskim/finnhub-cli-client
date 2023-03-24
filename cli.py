class CLI:
  def __init__(self, apiKey):
    self.apiKey = apiKey
  
  def run(self):
    cmd = ''
    while True and cmd != 'quit':
      cmd = input('> ')
      print('recieved input: ' + cmd)