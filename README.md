# Asterisk Base CID Translate!

One of the most problem of the Asterisk base PBX faced, when we want to make the **Caller ID name** and **Caller ID Number**, with the correct format **Number** **Name**, the extensions will get the name correctly from their phonebook. The reason of this project is develop a small core which listen on port 5000 TCP, then if you send the number will return with e164 format (+ country code at the beginning), in case I have this problem with the numbers from Asiatech and Pishgaman in Iran so I made the conditions for the Iranian numbers.


# Files

Files of the project is in these categories:

 - ISSABEL PBX PHP file for add the dial rule to rewrite the CallerID(num) and CallerID(name)
 - System service base on systemctl
 - python script to start and go to listen to do the number translation.
 - Bash script for test.

## Dependencies

 1. Python3 or Python 2
 2. Python Flask
 3. Git
 4. Wget
 5. Curl

## Install the Python Flask 

 - **Install with pip**
	        
	   pip install flask
	   
 - **Install with yum** 
 
       yum install flask -y
	

## Put file on PBX server

    mkdir /opt/cid
    cd /opt/cid
    git clone https://github.com/nimaam/Asterisk_CID_Translator/tree/main .
    

## Install Virtual environment
          
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate
    source venv/bin/activate



## Install Service

    cp cid.service /lib/systemd/system
    systemctl daemon-reload
    systemctl enable --now cid

## Test
   
     sh /opt/lookup.sh 982112345678



# Use it in Issabel

## Replace the function.php

    cp functions.inc.php /var/www/html/admin/modules/cidlookup/functions.inc.php

## Do Setting
In the FreePBX base system like the Issabel PBX, it is needed to add the CID Lookup Source and for this reason you should do like below:
**Host:** localhost
**Port:** 5000
**Username** and **Password** is not needed
**Path:** /lookup/
**Queuery:** did=[NUMBER]

Then in the inbound route you can add the Caller ID source you created.

