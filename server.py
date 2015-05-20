from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sys
import ecdf
import json
import logging

ADDR = "localhost"
PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):		
	scores = None
	html = None
	logger = None
	def do_GET(self):
		self.send_response(200, "OK")
		self.end_headers()
		self.wfile.write(RequestHandler.html)
	def do_POST(self):
		length = int(self.headers['Content-length'])
		data = json.JSONDecoder().decode(self.rfile.read(length))
		RequestHandler.logger.info(data["request"])
		self.send_response(200, "OK")
		self.end_headers()
		self.wfile.write(ecdf.percentile(data["percentile"], RequestHandler.scores))

def main():
	(school_name, RequestHandler.scores) = ecdf.parseArguments()
	# argument parsing: ecdf.py --school "name" input_file1 input_file2 ...
		
	with open ("template.html", "r") as template:
		RequestHandler.html = template.read()

	RequestHandler.logger = logging.getLogger('RequestHandler')
	hdlr = logging.FileHandler('request_history.log')
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	RequestHandler.logger.addHandler(hdlr) 
	RequestHandler.logger.setLevel(logging.INFO)
		
	httpd = HTTPServer((ADDR, PORT), RequestHandler)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		sys.exit()

if __name__ == "__main__":
	main()