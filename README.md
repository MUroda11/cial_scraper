# Technical assignment

A Python command-line application that, given a list of website URLs as input, visits them
and finds, extracts and outputs the websites’ logo image URLs and all phone numbers (e.g.
mobile phones, land lines, fax numbers) present on the websites.

Libraries used: beautifulsoup4, json, joblib, re, requests, sys, urlib

# How to use: 

- clone the repository or download the ZIP file
- create a text file with website urls - one per line
- navigate to the directory of the cloned repository
- run the application by inputing the text file via standard input:
```Bash 
	cat websites.txt | python -m main
```
- or load the docker image and run it by inputing the text file:
```docker
	docker load -i cial_scraper
	cat websites.txt | docker run -i main.py
```
- application will write the results via standard output - one line per website
