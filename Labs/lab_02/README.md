# Lab 2

## Team Members
- Alex Frederic (GitHub: alex-frederic, arfreder@usc.edu)

## Lab Question Answers

Answer for Question 1A:
 
About half of the messages from client to server randomly didn't make it
through. This is because under UDP, the client only tranmits each packet to the
server once without checking if it made it through. In fact, since there's no
two-way connection, the client can't know if a message didn't make it through.
Therefore, when packets are lost (which will happen half the time at random due
to the forced loss on the environment), the client can't react and just keeps
sending subsequent messages, ignoring the loss.


Answer for Question 2A:

All of the messages from client to server came through in both cases. This is
because TCP establishes a two-way connection between client and server. This
allows the client to be able to wait until the server sends a returning message
confirming it got the last packet the client sent before the client attempts to
send the next. If the client doesn't receive a confirmation back from the
server in a reasonable amount of time, it can try again and again until an
results in confirmation from the server, at which point the client moves onto
the next message. Thus, even when the forced loss caused half of the messages
to fail, the TCP connection could try again and again until an attempt
succeeded.


Answer for Question 3A:

About half of the messages from client to server randomly took longer to come
through than expected, while the rest remained instant. When that happened, if
any messages were sent in between a delayed message being sent and it appearing
on the server, they were also delayed until the delayed message appeared on the
server, at which point all messages sent up to that point appeared at once.
The other half of messages appeared basically instantly on the server. This
occurred because when a message attempt fails under TCP, the client waits
until a sufficient amount of time with no reply from the server has ellapsed to
confirm that the packet was lost and then repeats the process over and over
again until the server confirms that the message was received. During that
time, subsequent messages to the client are queued to be sent to the server but
aren't actually sent until the message that was stuck gets through to ensure
messages arrive in the same order that they are sent in. Therefore, when a
message is lost due to the 50% forced loss, the waiting and the multiple
attempts take more time than the basically instant amount of time it takes to
make a single attempt. Once the problematic message has been properly sent, the
subsequent messages can be sent no problem in a single attempt each.


Answer for Question 1C:

"argc" is the parameter of the C program that counts how many command-line
arguments are passed to the program when the program is run on the command
line. This includes the call to run the program itself. "argv" is an array of
pointers each pointing to strings containing the arguments passed to the
program at the command line. The array is ordered in the same order in which
the arguments were passed at the command line with the program name itself
located at index 0 of the array.


Answer for Question 2C:

A UNIX file descriptor is a unique integer value given to any currently running
process that might use I/O, like opening a file or running an executable. This
helps the kernel keep track of which process/file is which. A file descriptor
table is a table that the kernel keeps of all the file descriptors of the
currently running processes. This helps it keep track not only of the currently
running processes, but also of the connections between them, what files they
belong to (if any), and what permissions they have.


Answer for Question 3C:

A struct is a way to group multiple different variables with different types
and different names into one variable. A format for a type of struct can be
defined in order to make multiple different struct objects with the same
format. sockaddr_in is a struct type that contains the following sub-variables
for keeping track of IP address information:
	- sin_family (type: short): stores what address family that the server will
	  be using to communicate over IP
	- sin_port (type: unsigned short): stores the 16-bit port that the server 
	  will bind to
	- sin_addr (type: struct in_addr, which contains an unsigned long called
	  s_addr): stores the 32-bit IP address that the server will bind to
	- sin_zero (type: char[8]): determines the amount of unused padding space


Answer for Question 4C:

The first input parameter is "domain" (takes an int), which specifies the
communication domain/address family over which the server will be
communicating. In this case, it's AF_INET for IPv4. The second parameter is 
type" (takes an int), which specifies which type of communication that the
server will use, TCP or UDP. In this case, SOCK_STREAM specifies that TCP will
be used. The third parameter is "protocol", which controls what protocol will
be used to support the communication. This case 0 specifies IP will be used.
The function returns an integer value containing the file descriptor of the
process running the socket endpoint (or -1 if it failed to establish a socket).


Answer for Question 5C:

For bind(), the input parameters are:
	- sockfd (int): file descriptor of the active socket
	- addr (struct sockaddr): struct specifying what IP address and port number
	  to bind the server to
	- addrlen (struct socklen_t): struct giving the length of addr
For listen(), the input parameters are:
	- sockfd (int): file descriptor of the active socket
	- backlog (int): number of connection requests in queue waiting to
	connected to the server


Answer for Question 6C:

The while(1) loop continually checks for new connection requests so that the
server will be able to connect to a client regardless of when the request is
received and can continue operating indefinitely for as long as needed. It is
also the simplest way to achieve this. The problem with this is that if
multiple clients connect simultaneously, the first client will be connected and
have the code for accepting and sending messages executed for it, but the
others will be stuck waiting for the server to close the connection with the
first client before it loops back around to the accept() statement to connect
with them. This bottlenecks performance by only allowing one connect at a time
sequentially, making some clients wait unnecesssarily long instead of
connecting them simultaneously. Additionally, if a later connection in the
queue is stuck waiting for long enough, the connection may time out, meaning it
won't get a chance to connect to the server at all if there are too many
connection requests ahead of it.


Answer for Question 7C:

You could use fork() to create a child process upon accepting a client
connection request. This child process could then enter an if statement
checking if the return value of fork() function is 0 to separate the child
process from the parent process. In the if statement, the child would deal with
the code for accepting the message from the client and sending one back
(current lines 76-88). Outside of the if statement, the parent would
continue checking for other client connection requests, potentially creating
subsequent children if another connection request is made while the first child
is still working on handling the first connection. Therefore, multiple
clients can be connected to and handled in parallel to each other instead of
one after the other, improving execution time and ensuring no client
connection requests are timed out. At the end of the child's if statement, the
client socket should be closed and the child process should be ended with
"return 0;" to close out of the main() function. This helps prevent the
program's RAM from being cluttered with unnecessary socket objects or child
processes continuing to run on top of the original process.


Answer for Question 8C?
(I wasn't sure if the question about systems calls at the end was meant to be
answered or not, so I'm answering it here just in case; ignore if irrelevant):

A system call is when a program running on your system makes a request to the
OS for some system-level process, like outputing text to the console or
receiving input from a device. This helps mediate between the program and the
OS while allowing the OS to manage the permissions of the process.


Answer for Question 4A:

I did not touch LLMs for any part of this lab. The only coding assistance I had
was from the python socket tutorial provided in the lab manual
(https://realpython.com/python-sockets/). I copied some of the individual lines
of code from this website, but I did not use the "with" statement
implementation they used there. Instead I followed the comments in the provided
py file to develop a more typical, standard version of the socket client
program flow.