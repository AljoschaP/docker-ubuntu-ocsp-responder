openssl ocsp -index /opt/pki/ca/index.txt -port 8888 -rsigner /opt/pki/va/oscp.cert.pem -rkey /opt/pki/va/oscp.key.pem -CA /opt/pki/ca/intermediate.cert.pem -text -out /var/log/ocsp/ocsp.log
