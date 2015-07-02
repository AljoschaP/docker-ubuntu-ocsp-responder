# Docker Container with a Ubuntu-based OCSP-Responder
  - Provides an OpenSSL-OCSP behind a Node.js Router, monitored by Monit. In case of failure the OCSP will be restarted      automatically by Monit.
  - OCSP: /opt/pki/OCSP
  - index.txt /opt/pki/ca
  - Router: /opt/pki/Router
  
Start/Stop OCSP : /etc/init.d/ocsp <start|stop>

