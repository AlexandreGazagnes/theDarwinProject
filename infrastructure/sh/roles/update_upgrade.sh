echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/update_upgrade.sh"

apt-get -y update && apt -y upgrade

echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/update_upgrade.sh"

