echo "pki:$PASSWORD" | chpasswd
start ssh
mkdir /var/log/ocsp
touch /opt/pki/ca/index.txt.attr
npm config set registry http://registry.npmjs.org/
npm cache clean -f
npm install -g n
n stable
start ocsp
nohup node /opt/pki/Router/ocsp_router.js &
cat
