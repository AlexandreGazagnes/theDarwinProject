# permit root no
find /etc/ssh/sshd_config -type f -exec sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' {} \;
# redirect port 
find /etc/ssh/sshd_config -type f -exec sed -i 's/#Port 22/Port 24/g' {} \;
# only ssh no login
find /etc/ssh/sshd_config -type f -exec sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g' {} \;