ssh-keygen -f "/home/alex/.ssh/known_hosts" -R "178.79.163.140"
ssh root@178.79.163.140
./run.sh
ssh -p 24 master@178.79.163.140