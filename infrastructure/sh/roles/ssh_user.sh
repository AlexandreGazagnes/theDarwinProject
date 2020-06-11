cd /home/$MY_USER
#ssh
mkdir .ssh
# generate ssh
ssh-keygen -t ecdsa -b 384 -q -N "" -f /home/$MY_USER/.ssh/id_ecdsa
# add auth keys
echo $MY_USER_ID_RSA_PUB > .ssh/authorized_keys
# all rights 
chown -R alex:alex .ssh
cd
