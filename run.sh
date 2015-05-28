echo "pki:$PASSWORD" | chpasswd

tail -f /var/log/messages
