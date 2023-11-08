import requests
from dateutil.parser import parse

def get_time():
  response = requests.get('https://worldtimeapi.org/api/timezone/Europe/London')
  time = response.json()['datetime']
  parsed_time = parse(time)
  formatted_time = parsed_time.strftime('%Y-%m-%d %H:%M:%S')
  return formatted_time

if __name__ == '__main__':
  print(get_time())
