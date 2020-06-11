#! /bin/sh


###################################
# update upgrade --> OK
###################################

apt-get -y update && apt -y upgrade
echo "return code of l17 is $?"


###################################
# custom install --> OK
###################################

apt-get -y install nano htop curl wget ufw sudo screen vim screen inxi zsh apt-transport-https ca-certificates curl gnupg-agent software-properties-common
echo "return code of l25 is $?"


###################################
# Hots and hostname --> OK
###################################

echo $MY_HOSTNAME > /etc/hostname && echo $MY_HOSTNAME > /etc/host
echo "return code of l34 is $?"


###################################
# localtime --> OK
###################################

rm -f /etc/localtime && ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime
echo "return code of l41 is $?"


###################################
# admin create USER --> OK
###################################

# make encr pass 
pass=$(perl -e 'print crypt($ARGV[0], "password")' $MY_USER_PASSWD)
# make user 
useradd -m -s /bin/bash -p $pass $MY_USER && usermod -aG sudo $MY_USER
echo "return code of l52 is $?"
# no sudo passwd 
echo $MY_USER 'ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
echo "return code of l55 is $?" && tail -n 1 /etc/sudoers 


###################################
# docker --> OK 
###################################

# docker
# apt -y remove docker docker-engine docker.io
# echo "return code of 63 is $?"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt -y install docker-ce docker-ce-cli containerd.io
echo "return code of 65 is $?"
usermod -aG docker $MY_USER
# docker run hello-world
echo "return code of 71 is $?"

# compose
curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
# docker-compose --version
echo "return code of 83 is $?"


###################################
# ufw --> OK
###################################

ufw default deny incoming && ufw default allow outgoing
ufw allow $MY_SSH_PORT/tcp
yes |sudo ufw enable


###################################
# manage ssh connections  --> OK
###################################

# permit root no
find /etc/ssh/sshd_config -type f -exec sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' {} \;
# redirect port 
find /etc/ssh/sshd_config -type f -exec sed -i 's/#Port 22/Port 24/g' {} \;
# only ssh no login
find /etc/ssh/sshd_config -type f -exec sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g' {} \;


###################################
# user ssh --> OK
###################################

su $MY_USER
cd 
echo $MY_USER
#" PLEASE BE SURE NO PB HERE !!! "
mkdir .ssh
# generate ssh
ssh-keygen -t ecdsa -b 384 -q -N "" -f /home/$MY_USER/.ssh/id_ecdsa
# add auth keys
echo $MY_USER_ID_RSA_PUB > .ssh/authorized_keys

# compose 
# sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# sudo chmod +x /usr/local/bin/docker-compose
# docker-compose --version


###################################
# git config --> OK
###################################

cd
# git user
# git passwd
# git push ssh 
# clone
git clone $MY_GIT_REPO


####################################
#   fancy stuff
####################################

# use zsh
# sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# # change default theme
# find .zshrc -type f -exec sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="agnoster"/g' {} \;
# for better see https://www.freecodecamp.org/news/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38/


####################################
# run  --> ERROR INTERACTIVE
####################################

exit 
cd
ufw allow 1337/tcp
yes | ufw enable
# docker-compose -p theDarwinproject -f


####################################
# reload and reboot
####################################

# su and reboot
exit
reboot