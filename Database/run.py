import sqlite3 as db

con = db.connect("Tiango.sqlite")
cur = con.cursor()

# Questions for all topics
cur.executescript('''
INSERT INTO Cplusplus VALUES("Static variable declared in a class are also called_________ .", "instance variable", "named constant", "global variable", "class variable", "class variable"); 

INSERT INTO Cplusplus VALUES("Which of the following operator is used to release the dynamically allocated memory in CPP?", "remove", "free", "delete", "Both b and c", "delete"); 

INSERT INTO Cplusplus VALUES("Which of the following is not a false statement about new operator?", "It can’t be overloaded.", "It returns garbage value when memory allocation fails.", "It automatically computes the size of the data object.", "All of these", "It automatically computes the size of the data object."); 

INSERT INTO Cplusplus VALUES("Run time polymorphism can be achieved with______ .", "Virtual Base class", "Container class", "Virtual function", "Both a and c", "Virtual function");

INSERT INTO Cplusplus VALUES("Attempting to throw an exception that is not supported by a function call results in calling _____________ library function.", "indeterminate()", "unutilized()", "unexpected()", "unpredicted()", "unexpected()");

INSERT INTO Cplusplus VALUES("Which of the following is not a file opening mode ____ .", "ios::ate", "ios::nocreate", "ios::noreplace", "ios::truncate", "ios::truncate");

INSERT INTO Cplusplus VALUES("If the derived class is struct, then default visibility mode is _______ .", "public", "protected", "private", "struct can’t inherit class", "public");

INSERT INTO Cplusplus VALUES("An operator function is created using _____________ keyword.", "iterator", "allocator", "constructor", "operator", "operator");

INSERT INTO Cplusplus VALUES("Logical expressions produce ____________ type results.", "explicit", "garbage", "bool", "static", "bool");

INSERT INTO Cplusplus VALUES("Return type of uncaught_exception() is ________________ .", "int", "bool", "char*", "double", "bool"); 
''');

cur.executescript('''
INSERT INTO Java VALUES("Which variables are created when an object is created with the use of the keyword 'new' and destroyed when the object is destroyed?", "Local variables", "Instance variables", "Class Variables", "Static variables", "Class Variables");
 
INSERT INTO Java VALUES("What can be accessed or inherited without actual copy of code to each program?", "Browser", "Applet", "Package", "None of the above", "Package"); 

INSERT INTO Java VALUES("Which cookie it is valid for single session only and it is removed each time when the user closes the browser?", "Persistent cookie", "Non-persistent cookie", "All the above", "None of the above", "Non-persistent cookie"); 

INSERT INTO Java VALUES("What invokes immediately after the start() method and also any time the applet needs to repaint itself in the browser?", "stop()", "init()", "paint()", "destroy()", "paint()");

INSERT INTO Java VALUES("Which is a perfect example of runtime polymorphism?", "Method overloading", "Method overriding", "Constructor overloading", "None of the above", "Method overriding");

INSERT INTO Java VALUES("Which specification provides runtime environment in which java byte code can be executed?", "JDK", "JVM", "JRE", "None of the above", "JVM");

INSERT INTO Java VALUES("In which the access modifier means that the field can be accessed by all classes in your application?", "private", "Public", "Package", "Protected", "Public");

INSERT INTO Java VALUES("Which is a non-static method having the same name as its class?", "Field", "Method", "Constructor", "None of the above", "Constructor");

INSERT INTO Java VALUES("Hibernate is an?", "Open Source", "Lightweight", "ORM", "All mentioned above", "All mentioned above");

INSERT INTO Java VALUES("The life cycle of the thread is controlled by ?", "JVM", "JDK", "JRE", "None of the above", "JVM");
''');

cur.executescript('''
INSERT INTO Python VALUES("Which is reserved keyword in Python", "for", "catch", "switch", "let", "for"); 
INSERT INTO Python VALUES("Which of the following is not a data structure in Python", "List", "Set", "Tuple", "Array", "Array"); 
INSERT INTO Python VALUES("Suppose list1 is [1, 3, 2], What is list1 * 2 ?", "[2, 6, 4]", "[1, 3, 2, 1, 3]", "[1, 3, 2, 1, 3, 2]", "[1, 3, 2, 3, 2, 1]", "[1, 3, 2, 1, 3, 2]"); 
INSERT INTO Python VALUES("What is the output of this expression, 3*1**3?", "27", "9", "3", "1", "3"); 
INSERT INTO Python VALUES("What is the dataype of L? L = [1, 23, ‘hello’, 1].", "List", "Dict", "Array", "Tuple", "List"); 
INSERT INTO Python VALUES("What is the result of round(0.5) - round(-0.5)?", "0", "1", "2", "None of these", "0"); 
INSERT INTO Python VALUES("Which of these in not a core datatype?", "List", "Tuple", "Class", "Dict", "Class"); 
INSERT INTO Python VALUES("All keywords in Python are in", "lower case", "UPPER CASE", "Capitalized", "None of the above", "None of the above"); 
INSERT INTO Python VALUES("Which of the following statements is used to create an empty set?", "{}", "[]", "()", "set()", "set()"); 
INSERT INTO Python VALUES("Which of the following lines of code will result in an error?", "s={abs}", "s={4, ‘abc’, (1,2)}", "s={2, 2.2, 3, ‘xyz’}", "s={san}", "s={san}"); 
''');

cur.executescript('''
INSERT INTO MySQL VALUES("On executing DELETE command, if you get an error 'foreign key constraint'- what does it imply?", "Foreign key not defined", "Table is empty", "Connectivity issue", "Data is present in the other table", "Data is present in the other table"); 
INSERT INTO MySQL VALUES("How to find out all databases starting with ‘test‘ ?", "SHOW DATABASES LIKE '%test%';", "SHOW DATABASES LIKE '%test';", "SHOW DATABASES LIKE ''test'%';", "SHOW DATABASES LIKE 'test%';", "SHOW DATABASES LIKE 'test%';"); 
INSERT INTO MySQL VALUES("How can we get the number of records or rows in a table?", "Using COUNT", "Using NUM", "Using NUMBER", "Both A and C", "Using COUNT"); 
INSERT INTO MySQL VALUES("Which of the following ways are the correct way to get the current date?", "SELECT CURTIME();", "SELECT CURDATE();", "SELECT CURRENT_TIME();", "All of the above", "All of the above");
INSERT INTO MySQL VALUES("A view is nothing but a ________ table or a stored query", "Dymanic", "Real", "Virtual", "Static", "Virtual");
INSERT INTO MySQL VALUES("'USE' keyword is used to select a ___________", "Table", "Column", "Database", "All of above", "Database");
INSERT INTO MySQL VALUES("How much storage space does DATETIME require?", "4 bytes", "2 bytes", "8 bytes", "1 bytes", "8 bytes");
INSERT INTO MySQL VALUES("Which of the following file extension is a valid MyISAM file extension?", ".ism", ".myd", ".my", ".mys", ".myd");
INSERT INTO MySQL VALUES("What is a candidate key?", "Used to uniquely identify a row", "Alias for primary key", "Used to identify a column", "Alias for foreign key", "Used to uniquely identify a row");
INSERT INTO MySQL VALUES("Which of the following is Data Control Language?", "REVOKE", "SELECT", "INSERT", "MERGE", "REVOKE"); 
''');

cur.executescript('''
INSERT INTO JavaScript VALUES("Inside which HTML element do we put the JavaScript?", "<javascript>", "<script>", "<js>", "<scripting>", "<script>"); 
INSERT INTO JavaScript VALUES("Which built-in method calls a function for each element in the array?", "while()", "loop()", "forEach()", "None of these", "forEach()"); 
INSERT INTO JavaScript VALUES("Which of the following function of Array object represents the source code of an object?",
"toSource()", "splice()", "toString()", "unshift()", "toSource()"); 
INSERT INTO JavaScript VALUES("Which of the following is not a reserved word in JavaScript?", "interface", "throws", "short", "except", "except"); 
INSERT INTO JavaScript VALUES("Which of the following is the correct syntax to print a page using JavaScript?", "window.print();", "browser.print();", "navigator.print();", "document.print();", "window.print();"); 
INSERT INTO JavaScript VALUES("Which of the following function of Number object returns a string value version of the current number?", "toString()", "toFixed()", "toLocaleString()", "toPrecision()", "toString()"); 
INSERT INTO JavaScript VALUES("Which of the following function of String object creates a string to be displayed as bold as if it were in a <b> tag?", "anchor()", "big()", "blink()", "bold()", "bold()"); 
INSERT INTO JavaScript VALUES("Which of the following function of Array object applies a function simultaneously against two values of the array (from left-to-right) as to reduce it to a single value?", "pop()", "push()", "reduce()", "reduceRight()", "reduce()"); 
INSERT INTO JavaScript VALUES("The async attribute can be set in the following ways -", "<script async>", "<script async='async'>", "<script async=''>", "All of these", "All of these"); 
INSERT INTO JavaScript VALUES("Which was the first browser to support JavaScript ?", "Netscape", "Mozilla Firefox", "Google Chrome", "IE", "Netscape"); 
''');

cur.executescript('''
INSERT INTO Aptitude VALUES("Amit covers a distance at a speed of 24 km/hr in 6 min. If he wants to cover the same distance in 8 min, what should be his speed?", "18 km/hr", "21 km/hr", "30 km/hr", "15 km/hr", "18 km/hr"); 
INSERT INTO Aptitude VALUES("If 12 men or 16 women can do a work in 172 days, how long will 21 men and 15 women to do the same work ?", "64 days", "60 days", "86 days", "75 days", "64 days"); 
INSERT INTO Aptitude VALUES("Find average of natural numbers from 1 to 65?", "33", "32.5", "130", "65", "33"); 
INSERT INTO Aptitude VALUES("54 toymakers can prepare 36 toys per day. Ajay wants 416 toys. How many toymakers should he employ to get the job done in 16 days?", "43", "39", "16", "24", "39");
INSERT INTO Aptitude VALUES("Kabir paid Rs. 9600 as interest on a loan he took 5 years ago at 16% rate of simple interest. What was the amount he took as loan?", "Rs. 16400", "Rs. 12000", "Rs. 12500", "Rs. 18000", "Rs. 12000");
INSERT INTO Aptitude VALUES(" When Jaya divided surface area of a sphere by the sphere’s volume, she got the answer as 1/18 cm. What is the radius of the sphere?", "24 cm", "6 cm", "54 cm", "4.5 cm", "54 cm");
INSERT INTO Aptitude VALUES("The ratio of two numbers is 4 : 5 and their H.C.F is 4. Find their L.C.M.", "96", "80", "73", "48", "80");
INSERT INTO Aptitude VALUES("The unit digit in the product (624 * 708 * 913 * 463) is:", "2", "5", "6", "8", "8");
INSERT INTO Aptitude VALUES("Find the least number which should be added to 2430 so that the sum is exactly divisible by 5, 4 and 2", "3", "10", "20", "33", "10");
INSERT INTO Aptitude VALUES("How many words can be formed  by using all letters of word ALIVE.", "86", "120", "100", "105", "120"); 


''')

con.commit();
cur.close();
