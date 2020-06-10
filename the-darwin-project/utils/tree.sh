#! /bin/sh

sudo find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | sudo xargs rm -rf && tree -a -I '.git|env'