openssl ocsp -index /opt/pki/ca/index.txt -port 8888 -rsigner /opt/pki/va/va-cert.crt -rkey /opt/pki/va/va-key.pem -CA /opt/pki/ca/ca-cert.pem -text -out /var/log/ocsp/ocsp.log
