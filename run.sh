echo "pki:$PASSWORD" | chpasswd
/etc/init.d/ssh start
/etc/init.d/openssl-ocsp start
node /opt/pki/Router/ocsp_router.js
cat
