def writeFile(fileName, fileData):
    fileName+='.log'
    with open(fileName, 'a') as monthlyLog:
        monthlyLog.write(fileData)    
    
def main():
    import re
    import sys
    import time
    import operator
    import datetime
    from urllib.request import urlretrieve
    
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'http.log'
    #LOCAL_FILE = 'sample.log'

    print('Retrieving Data...')

    file = open(LOCAL_FILE)

# Variable Declaration
    total_lines = 0
    request_unsuccessful = 0
    request_redirect = 0
    file_requests = {}
    daily_requests = {}
    weekly_requests = {}
    monthly_requests = {}
    regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

    print("\n\nParsing:")


    for line in file:
	total_lines +=1
	data = regex.split(line)
