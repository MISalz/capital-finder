from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # s = self.path
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        name = dict(query_string_list)

        if "word" in name:
            url = "https://restcountries.com/v3.1/name/"
            full_url = url + name["word"]
            response = requests.get(full_url)
            data = response.json()
            
            capitals = []
            for capital_name in data:
              caps = capital_name["capital"]
              capitals.append(caps)
              message= str(f"The capital of {name['word']} is {capitals[0][0]}.")

        else:
            message = "give me a word to define please"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
