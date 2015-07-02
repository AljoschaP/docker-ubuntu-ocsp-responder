echo "pki:$PASSWORD" | chpasswd
start ssh
mkdir /var/log/ocsp
touch /opt/pki/ca/index.txt.attr
npm config set registry http://registry.npmjs.org/
npm cache clean -f
npm install -g n
npm install -g forever
n stable
start ocsp
start ocsp-router
/usr/sbin/sshd -D
