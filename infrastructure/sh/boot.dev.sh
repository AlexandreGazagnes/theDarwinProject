#! /bin/sh 

# vars
. ./vars/vars.dev.sh

# roles
# echo "\n\nstart #####################################  $(whoami) --> . ./roles/update_upgrade.sh"
# . ./roles/update_upgrade.sh
# echo "\n\nend   #####################################  $(whoami) --> . ./roles/update_upgrade.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/install.sh"
. ./roles/install.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/install.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/localtime.sh"
. ./roles/localtime.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/localtime.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/hostname.sh"
. ./roles/hostname.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/hostname.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/create_user.sh"
. ./roles/create_user.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/create_user.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/docker.sh"
. ./roles/docker.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/docker.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/ufw.sh"
. ./roles/ufw.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/ufw.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/ssh_config.sh"
. ./roles/ssh_config.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/ssh_config.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/ssh_user.sh"
. ./roles/ssh_user.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/ssh_user.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/git.sh"
. ./roles/git.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/git.sh"


echo "\n\nstart #####################################  $(whoami) --> . ./roles/exit.sh"
. ./roles/exit.sh
echo "\n\nend   #####################################  $(whoami) --> . ./roles/exit.sh"


echo "\n\nend   #####################################  $(whoami) --> done"

