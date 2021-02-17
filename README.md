# SUBDOMAINS SEARCH

##### Description:

A new method to search for subdomains of many domains. can be used as a pentesting tool, this tool also gives you the IP addresses for those subdomains.



##### How to install & use:

This simple script was tested on Python 3.7, follow the steps to make it work. and requires two modules: Censys to search for the certificates and socket to get their IP

- Signup in https://censys.io/ and get the userid and secret and put it inside the script
- Install Python on your device.
- install the modules using `pip install censys socket`
- Start the script using `python subdomains.py`
- Input the domain name you want to test without `www or http://` example: google.com
