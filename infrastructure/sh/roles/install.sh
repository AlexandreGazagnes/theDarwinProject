echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/install.sh"

apt-get -y install nano htop curl wget ufw sudo screen vim screen inxi zsh apt-transport-https ca-certificates curl gnupg-agent software-properties-common

echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/install.sh"