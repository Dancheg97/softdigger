# install git
sudo yum install git -y
# install python 3.7
yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel xz-devel -y
cd /usr/src  
wget https://www.python.org/ftp/python/3.7.11/Python-3.7.11.tgz
tar xzf Python-3.7.11.tgz
cd Python-3.7.11 
./configure --enable-optimizations 
make altinstall
rm /usr/src/Python-3.7.11.tgz -y
# export python and pip path 
export PATH=$PATH:/usr/local/bin/python3.7
export PATH=$PATH:/usr/local/bin/pip3.7
# install go
cd /root/
wget https://dl.google.com/go/go1.13.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.13.linux-amd64.tar.gz
# export go path
export PATH=$PATH:/usr/local/go/bin
# clone git repo
git clone https://github.com/Dancheg97/softdigger
cd softdigger
pip3.7 install -r requirements.txt