import sys
import httplib
import json

def usage():
	print "usage:", sys.argv[0], "X", "Y"
	print "\tX: X-th percentile (range from 1 to 100)"
	print "\tY: the client name (would be logged at server side)"

def ordinalNumber(x):
	try:
		x = int(x)
	except:
		x = 0
	# note: here I only take care of x in 1 - 100
	# 0, 101, ...etc might result unexpected result
	# if 11, 12, 13 => th
	# else if single-digit is 1, 2, 3 => st, nd, rd
	return str(x)+{11:'th', 12:'th', 13:'th'}.get(x, {1:'st', 2:'nd', 3:'rd'}.get(x%10, 'th'))

def requestString(X, Y):
	return "please send the %s percentile to client %s" % (ordinalNumber(X), Y)

def main():
	if len(sys.argv) < 3:
		usage()
		sys.exit(0)
	X = sys.argv[1]
	conn = httplib.HTTPConnection("localhost:8000")
	conn.request("POST", "/", json.JSONEncoder().encode({"percentile":X, "request":requestString(X, sys.argv[2])}))
	response = conn.getresponse()
	conn.close()
	print(response.read())

if __name__ == "__main__":
	main()