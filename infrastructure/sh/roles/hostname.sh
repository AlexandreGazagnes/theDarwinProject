echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/hostname.sh"

echo $MY_HOSTNAME > /etc/hostname && echo $MY_HOSTNAME > /etc/host

echo "\n\nend #####################################  $(whoami) in $(pwd) --> . ./roles/hostname.sh"