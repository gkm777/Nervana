from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sys
import ecdf
import json

ADDR = "localhost"
PORT = 8000

def log(msg):
	print msg

class RequestHandler(BaseHTTPRequestHandler):		
	scores = None
	def do_POST(self):
		length = int(self.headers['Content-length'])
		data = json.JSONDecoder().decode(self.rfile.read(length))
		log(data["request"])
		self.send_response(200, "OK")
		self.end_headers()
		self.wfile.write(ecdf.percentile(data["percentile"], RequestHandler.scores))
		
def usage():
	print "usage:", sys.argv[0], "--school", "SCHOOL_NAME", "INPUT_FILE_1", "[INPUT_FILE_i]*"

def main():
	# argument parsing: ecdf.py --school "name" input_file1 input_file2 ...
	if (len(sys.argv) < 4 or sys.argv[1] != "--school"):
		usage()
		sys.exit(0)
	school_name = sys.argv[2]
	RequestHandler.scores = ecdf.loadScores(school_name, sys.argv[3:])
	
	httpd = HTTPServer((ADDR, PORT), RequestHandler)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		sys.exit()
if __name__ == "__main__":
	main()