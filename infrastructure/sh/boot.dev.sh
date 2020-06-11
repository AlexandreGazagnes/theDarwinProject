#! /bin/sh 

# vars
. ./vars/vars.dev.sh

# roles
# echo "start #####################################  $(whoami) --> . ./roles/update_upgrade.sh"
# . ./roles/update_upgrade.sh
# echo "end #####################################  $(whoami) --> . ./roles/update_upgrade.sh"


echo "start #####################################  $(whoami) --> . ./roles/install.sh"
. ./roles/install.sh
echo "end #####################################  $(whoami) --> . ./roles/install.sh"


echo "start #####################################  $(whoami) --> . ./roles/localtime.sh"
. ./roles/localtime.sh
echo "end #####################################  $(whoami) --> . ./roles/localtime.sh"


echo "start #####################################  $(whoami) --> . ./roles/hostname.sh"
. ./roles/hostname.sh
echo "end #####################################  $(whoami) --> . ./roles/hostname.sh"


echo "start #####################################  $(whoami) --> . ./roles/create_user.sh"
. ./roles/create_user.sh
echo "end #####################################  $(whoami) --> . ./roles/create_user.sh"


echo "start #####################################  $(whoami) --> . ./roles/docker.sh"
. ./roles/docker.sh
echo "end #####################################  $(whoami) --> . ./roles/docker.sh"


echo "start #####################################  $(whoami) --> . ./roles/ufw.sh"
. ./roles/ufw.sh
echo "end #####################################  $(whoami) --> . ./roles/ufw.sh"


echo "start #####################################  $(whoami) --> . ./roles/ssh_config.sh"
. ./roles/ssh_config.sh
echo "end #####################################  $(whoami) --> . ./roles/ssh_config.sh"


echo "start #####################################  $(whoami) --> . ./roles/ssh_user.sh"
. ./roles/ssh_user.sh
echo "end #####################################  $(whoami) --> . ./roles/ssh_user.sh"


echo "start #####################################  $(whoami) --> . ./roles/git.sh"
. ./roles/git.sh
echo "end #####################################  $(whoami) --> . ./roles/git.sh"


echo "start #####################################  $(whoami) --> . ./roles/exit.sh"
. ./roles/exit.sh
echo "end #####################################  $(whoami) --> . ./roles/exit.sh"


echo "end #####################################  $(whoami) --> done"

