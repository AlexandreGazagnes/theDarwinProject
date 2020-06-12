echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/docker.sh"

# docker
# apt -y remove docker docker-engine docker.io
# echo "return code of 63 is $?"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt -y install docker-ce docker-ce-cli containerd.io
# echo "return code of 65 is $?"
usermod -aG docker $MY_USER
# docker run hello-world
# echo "return code of 71 is $?"


# compose
curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
# docker-compose --version
# echo "return code of 83 is $?"

echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/docker.sh"