echo "\n\nstart #####################################  $(whoami) in $(pwd) --> . ./roles/git.sh"

cd /home/$MY_USER
# git user
# git passwd
# git push ssh 
# clone
git clone $MY_GIT_REPO
chown -R master:master $MY_PROJECT_NAME
cd

echo "\n\nend   #####################################  $(whoami) in $(pwd) --> . ./roles/git.sh"
