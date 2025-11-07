# Lab 9

## Team Members
- Alex Frederic (GitHub: alex-frederic, arfreder@usc.edu)

## Lab Question Answers

Answer to Question 1a:

We are using certificate-based authentication via SSL. This type of
authentication requires a public key and a private key.
(https://www.geeksforgeeks.org/computer-networks/how-does-certificate-based-authentication-work/
https://www.ssl.com/article/private-and-public-keys/)


Answer to Question 1b:

The public key is used to send the session key from the client to the server.
Then, once both nodes agree on the session key, the session key is used to
encrypt all further data transport during the session.
(https://en.wikipedia.org/wiki/Transport_Layer_Security)

The client can include a client certificate in its message verifying that it
is a specific verified client. Alternatively, on a higher level, a username/
email and password pair can be used to authenticate a connecction.
(https://en.wikipedia.org/wiki/Public_key_certificate#TLS/SSL_client_certificate)


Answer to Question 2:

The private key is "server-key.pem" and the public key is "server-cert.pem".


Answer to Question 3:

A certificate authority is an organization that issues and keeps track of
digital certificates proving that the owner is the rightful owner of a certain
public key. This prevents man-in-the-middle attacks.