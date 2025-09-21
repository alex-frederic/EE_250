# Lab 3

## Team Members
- Alex Frederic (GitHub: alex-frederic, arfreder@usc.edu)

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

They are stateless, meaning that the server doesn't retain any information on previous client
requests or hold any client sessions. This means that each client system manages and caches
important information itself.. Therefore, adding additional clients to the server adds minimal
load onto the server, allowing it to serve many client requests without significant processing
slowdown.


Question 2: According to the definition of "resources" provided in the AWS article above, What are the resources the mail server is providing to clients?

The resources are the mail entries stored in mail_db.json file on the server side. That's the data
that each client request asks to receive or delete.


Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

We did not use the PUT command, which modifies a prexisting resource on the server side. To
include this method in the mail system, we could add a functionality that let users update the
subject or body of an email that had already been sent to fix any mistakes that might have been
made in typing out the email.


Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!

They are used to authenticate users each time a request is made to the server before it responds.
This allows the server to ensure that only authorized users can access certain resources on the
server or that they can access the server at all. This protects the server from outside bad actors
accessing or modifying protected resources and allows an API to be monetized by charging for API
keys. Further, it allows the server to track who has accessed what resources and how much each
user has used the API, which is also useful for security and monetization reasons.

Sources:
	- https://aws.amazon.com/what-is/restful-api/