# Email scapper/dumper

This tool takes webpage URL(You can give multiple also) as input gets the webpage using requests library,
than it uses regular Expressions(REGEX) to find all email addresses using specified pattern and displays it on terminal.

The regex pattern that I have used is : "[a-zA-Z0-9-_.]+@[a-zA-Z0-9_]+[.][a-zA-Z.]+"

While it is very hard to search for Emails manually on websites, this can make it easy; 
sometimes it also finds Emails that are not visible e.g. given in matatag or hidden tags etc.

Used python libraries and their description:

requests : Requests allows you to send HTTP/1.1 requests extremely easily.
re : re library provides features for regular expressions (REGEX) in Python.


I have used User Agent headers to make request.
It is always advisable to use proxies while scrapping.


