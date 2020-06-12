#! /bin/sh 


# vars
echo "start VARS"
. ./vars/vars.dev.sh
echo "end   VARS"

# roles
echo "start ROLES"
. ./roles/update_upgrade.sh
. ./roles/install.sh
. ./roles/localtime.sh
. ./roles/hostname.sh
. ./roles/create_user.sh
. ./roles/docker.sh
. ./roles/ufw.sh
. ./roles/ssh_config.sh
. ./roles/ssh_user.sh
. ./roles/git.sh
. ./roles/as_service.sh
. ./roles/exit.sh
echo "end   ROLES"