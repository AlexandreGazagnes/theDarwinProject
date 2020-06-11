

# make encr pass 
pass=$(perl -e 'print crypt($ARGV[0], "password")' $MY_USER_PASSWD)

# make user 
useradd -m -s /bin/bash -p $pass $MY_USER && usermod -aG sudo $MY_USER
echo "return code of l52 is $?"

# no sudo passwd 
echo $MY_USER 'ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
echo "return code of l55 is $?" && tail -n 1 /etc/sudoers 

