import random

# configuration
studentPool = xrange(1200)
inputFiles = []
for i in xrange(9):
	inputFiles.append("input_file" + str(i+1) + ".csv")
schoolPool = ["Carnegie Mellon University", "Hillman College", 
	"Faber College", "Mission College", "Port Chester University",
	"Harrison University"]
# others are not important for result
coursePool = ["Algebra", "Introduction to Computer System",
	"Web Application Development", "Cloud Computing",
	"Packet Switching and Computer Networks", 
	"Fundamentals of Embedded Systems",
	"Distributed System", "Introduction of Information Security",
	"Managerial and Economics"]
datePool = ["2015-03-17", "2015-03-18", "2015-03-19",
	"2014-03-11", "2014-03-12"]

def scorePool(studentId):
	# should depend on student, school, and course
	# to be simplied, just use a normal distribution
	score = random.normalvariate(70 + 20 * studentId / len(studentPool), 6)
	return max(0, min(score, 100))

# generate InputFiles
# in order to generate same result for test, I use seed 0
# could be replaced by None to use current time
random.seed(0)
for inputFile in inputFiles:
	with open(inputFile, 'w') as f:
		for row in xrange(random.randrange(200, 500)):
			r = random.randrange(10000000)
			f.write(str(studentPool[r%len(studentPool)]) + "," + 
				'"' + coursePool[r%len(coursePool)] + '",' + 
				'"' + schoolPool[r%len(schoolPool)] + '",' + 
				datePool[r%len(datePool)] + "," +
				str(scorePool(r%len(studentPool))) + "\n")
		f.close()

