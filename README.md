# Asterisk_CID_Translator


# Installation: 

mkdir /opt/cid

cd /opt/cid

git clone 

pip install virtualenv

virtualenv venv

venv\Scripts\activate

source venv/bin/activate

pip install flask


#  in Redhat base you can run 
yum install python-flask-* or python3-flask-*

# Add Service

cp cid.service /lib/systemd/system

systemctl daemon-reload

systemctl enable --now cid


# Test:

sh /opt/test.sh 982112345678

# The number should be 
# local 8 number
# or 11 digit number start with 0
# or 12 number start with 98 then area code then 8 digit 
# or 0098 at the begining
# then it will be translated.
