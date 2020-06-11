#! /bin/sh 

# vars
. ./vars/vars.dev.sh

# roles
# . ./roles/update_upgrade.sh

. ./roles/install.sh
echo "#####################################  $(whoami) --> . ./roles/install.sh"


. ./roles/localtime.sh
echo "#####################################  $(whoami) --> . ./roles/localtime.sh"


. ./roles/hostname.sh
echo "#####################################  $(whoami) --> . ./roles/hostname.sh"


. ./roles/create_user.sh
echo "#####################################  $(whoami) --> . ./roles/create_user.sh"


. ./roles/docker.sh
echo "#####################################  $(whoami) --> . ./roles/docker.sh"


. ./roles/ufw.sh
echo "#####################################  $(whoami) --> . ./roles/ufw.sh"


. ./roles/ssh_config.sh
echo "#####################################  $(whoami) --> . ./roles/ssh_config.sh"


. ./roles/ssh_user.sh
echo "#####################################  $(whoami) --> . ./roles/ssh_user.sh"


. ./roles/git.sh
echo "#####################################  $(whoami) --> . ./roles/git.sh"


. ./roles/exit.sh
echo "#####################################  $(whoami) --> . ./roles/exit.sh"


echo "#####################################  $(whoami) --> done"

