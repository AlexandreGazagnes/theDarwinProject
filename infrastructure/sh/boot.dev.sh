#! /bin/sh 

# vars
. ./vars/vars.dev.sh

# roles
echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/update_upgrade.sh"
. ./roles/update_upgrade.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/update_upgrade.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/install.sh"
. ./roles/install.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/install.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/localtime.sh"
. ./roles/localtime.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/localtime.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/hostname.sh"
. ./roles/hostname.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/hostname.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/create_user.sh"
. ./roles/create_user.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/create_user.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/docker.sh"
. ./roles/docker.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/docker.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/ufw.sh"
. ./roles/ufw.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/ufw.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/ssh_config.sh"
. ./roles/ssh_config.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/ssh_config.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/ssh_user.sh"
. ./roles/ssh_user.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/ssh_user.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/git.sh"
. ./roles/git.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/git.sh"


echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/exit.sh"
. ./roles/exit.sh
echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/exit.sh"


echo "\n\nend   #####################################  $(whoami) in $(pwd) --> done"

