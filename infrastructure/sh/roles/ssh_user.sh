echo "before su $MY_USER"
sudo su $MY_USER
echo "after su $MY_USER"

cd 
echo $MY_USER
#" PLEASE BE SURE NO PB HERE !!! "
mkdir .ssh
# generate ssh
ssh-keygen -t ecdsa -b 384 -q -N "" -f /home/$MY_USER/.ssh/id_ecdsa
# add auth keys
echo $MY_USER_ID_RSA_PUB > .ssh/authorized_keys