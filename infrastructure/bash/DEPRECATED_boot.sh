#! /bin/sh


###################################
HOSTNAME='your hostname # ie server-dev, www-master etc etc'
PORT='501010101010' # the open port
USER='i-am-a-user' # user

###################################

# update  && install basics
apt -y update && apt -y upgrade # &&
# apt -y install sudo nano htop curl wget inxi ufw supervisor nginx chromium-browser firefox apt-transport-https ca-certificates software-properties-common zsh

# change localhost and date
echo $HOSTNAME > /etc/hostname && echo $HOSTNAME > /etc/host && \
sudo rm -f /etc/localtime && sudo ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime

# admin create USER interactive
adduser $USER && usermod -aG sudo $USER && sudo reboot # reconnect as USER

# disable ssh connection for root
# nano /etc/ssh/sshd_config # set #PermitRootLogin yes --> No
sudo systemctl restart sshd  # or sudo reboot

# ssh
ssh-keygen
# add hostkeys from local laptop
# cat .ssh/id_rsa.pub | ssh [user]@[server_ip] 'cat >> .ssh/authorized_keys'
# add keygen to git hub or gitlab
# www.gitlab.com

# docker
sudo apt -y remove docker docker-engine docker.io && \
sudo curl -fsSL get.docker.com -o get-docker.sh && \
sh get-docker.sh && sudo usermod -aG docker $USER

# micro
curl https://getmic.ro | bash

# block 80 with ufw
sudo ufw default deny incoming && sudo ufw default allow outgoing && \
sudo ufw deny 80/tcp && sudo ufw allow 22/tcp && sudo ufw allow ssh && \
sudo ufw allow $PORT/tcp && sudo ufw enable && sudo ufw status verbose

# install zsh
sudo apt -y install zsh && chsh -s $(which zsh) && sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# python
# sudo apt -y install python3.8 python3.7 python3-pip python3-venv python3-apt
# cd ~ && python3 -m venv env 
# source env/bin/activate && \
# python3 -m pip install pandas flask SQLAlchemy Flask-WTF IPython aiohttp selenium requests numpy matplotlib seaborn lxml flask-cors flask_sqlalchemy Flask-Session flask-bcrypt flask-login Flask-Mail flask-marshmallow gunicorn pytest

# git repo
git clone git@gitlab.com:alexandreCPMHK/server.git

# .zshrc
cat /home/$USER/server/.zshrc >> /home/$USER/.zshrc

# /etc
# from local
#  scp /etc/[project].json [user]@[ip_adress]:/etc/
