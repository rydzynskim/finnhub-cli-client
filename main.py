from cli import CLI
import os

if __name__ == '__main__':
  # get api token from environment variables
  apiKey = os.getenv('FINNHUB_API_KEY')
  # start the cli
  interface = CLI(apiKey)
  interface.run()
