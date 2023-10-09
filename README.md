# Asterisk_CID_Translator


# Installation: 

mkdir /opt/cid

cd /opt/cid

git clone 

# Install Virtual environment
pip install virtualenv

virtualenv venv

venv\Scripts\activate

source venv/bin/activate

# Install Flask base with pip
pip install flask


# Install in Redhat base you can run 
yum install python-flask-* or python3-flask-*

# Add Service

cp cid.service /lib/systemd/system

systemctl daemon-reload

systemctl enable --now cid


# Lookup Test Script:
sh /opt/lookup.sh 982112345678

# The number should be 
# local 8 number
# or 11 digit number start with 0
# or 12 number start with 98 then area code then 8 digit 
# or 0098 at the begining
# then it will be translated.


#Issable modification
cp functions.inc.php /var/www/html/admin/modules/cidlookup/functions.inc.php

# Issable add the CID Lookup 
For the Issable PBX you should do the CallerID Lookup and select the HTTP model then 
Server: localhost
Port: 5000
Username: ----
Password: ----
Path: /lookup/
Query: did=[NUMBER]

After this in each Inbound Router you can select the CallerID Source to the CID Lookup you created.

