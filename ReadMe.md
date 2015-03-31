Description

Base Challenge Description
--------------------------------
Suppose you have multiple text files, each containing lines of the form:
student_id,course_name,school_name,test_date,test_score

An example valid line could look like the following (note that the files will not have headers):
9812345,¡¨Algebra¡¨,¡¨Port Chester University¡¨,2015-03-17,75.5

Write a program to compute the empirical cumulative distribution function of the average test score of students who attended a particular school, which is specified as a parameter to the program.

An example invocation of the program would be:
python ecdf.py --school ¡§Port Chester University¡¨ input_file1.csv input_file2.csv

The expected output from invoking such a program would be of the following form (use a single tab character to delimit field values, and display the results to standard output):

Port Chester University students

percentile    mean_test_score
1                  0
2                  0
3                  5.25
¡K                ¡K
100              100


Bonus Challenge #1
-----------------------
(The following is optional)
Extend your solution in the base challenge to a client-server model or RESTful architecture to accomplish the following:

------
Server starts and computes the percentile list from the given input files.

Server begins listening for client requests.

Client sends server a string message of the following form:
¡§please send the Xth percentile to client Y¡¨   (where X is replaced with a numeric percentile value, and Y is an arbitrary identifying string).

Server sends client the appropriate Xth percentile value and logs the string and the current timestamp in its request history.

Repeat until the server process is terminated
-----

Client and server can reside on the same machine

Client and server can communicate directly with each other or you can use an intermediate process that manages the communication between client and server

You can use existing packages/frameworks/programs if you¡¦d like


Bonus Challenge #2
-----------------------
(The following is optional)
Extend your solution to parse and render the output in some visual manner on screen.  Again you can use any existing packages/frameworks/programs to assist.