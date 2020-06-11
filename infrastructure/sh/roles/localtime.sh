echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/localtime.sh"

rm -f /etc/localtime && ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime

echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/localtime.sh"