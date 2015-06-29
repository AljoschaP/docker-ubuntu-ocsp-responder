echo "pki:$PASSWORD" | chpasswd
/etc/init.d/ssh start
mkdir /var/log/ocsp
npm config set registry http://registry.npmjs.org/
npm cache clean -f
npm install -g n
sudo n stable
/etc/init.d/openssl-ocsp start
node /opt/pki/Router/ocsp_router.js
cat
