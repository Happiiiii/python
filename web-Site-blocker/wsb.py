import time
from datetime import datetime as dt

# local file path
temp_host_path = "./temp_host.txt"
# root file path 
root_host_path = "/etc/hosts"
# list of websites to block during working hours
website_list = ["www.facebook.com","facebook.com"]
# redirect the website to the localhost
redirect = "127.0.0.1" 

# endless loop
while True:
    # working hours 8AM - 16PM (railwaytime)
    if 8 < dt.now().hour < 16:
        print "Working hours"
        # open the file in read & write mode
        with open(temp_host_path,"r+") as file:
            # read the file and store it in a variable
            content = file.read()
            # iterate each website in website_list
            for website in website_list:
                # check if website is already in the file
                if website in content:
                    # if website already exist pass the condition
                    pass
                else:
                    # else write into the file in format(redirect + " " + website + "\n")
                    file.write(redirect + " " + website + "\n")
    # Fun hours after 16PM
    else:
        print "Fun hours"  
        # open the file in read & write mode
        with open(temp_host_path,"r+") as file:
            # read each line in the file and store that array in a variable
            content = file.readlines()
            # initially the curser is in the end of the content, we have to move the curser point to the begning of the line inorder to read the file from top-bottom
            file.seek(0)
            # iterate each line in the file
            for line in content:
                # remove website that are blocked
                if not any(website in line for website in website_list):
                    # write a file without the websites in the website_list
                    file.write(line)
            # overwriting the existing file to avoid duplication
            file.truncate()

    time.sleep(5)


