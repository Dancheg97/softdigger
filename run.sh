clear
# check all installed
git --version
python3.7 --version
# paths
export PATH=$PATH:/usr/local/go/bin
export PATH=$PATH:/usr/local/bin/python3.7
export PATH=$PATH:/usr/local/bin/pip3.7
# launch
nohup go run .
nohup python3.7 runner.py
