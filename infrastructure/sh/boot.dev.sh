#! /bin/sh 

# vars
. ./vars/vars.dev.sh

# roles
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
. ./roles/exit.sh
echo 'done'