echo "\n\nstart   #####################################  $(whoami) in $(pwd) --> . ./roles/ufw.sh"

ufw default deny incoming && ufw default allow outgoing
ufw allow $MY_SSH_PORT/tcp
ufw allow $MY_INTERNET_PORT/tcp
yes |sudo ufw enable

echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/ufw.sh"