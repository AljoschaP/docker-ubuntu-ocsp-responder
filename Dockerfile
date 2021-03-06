FROM ubuntu:12.04
MAINTAINER aljoscha.poertner@fh-bielefeld.de

#default password for pki user
ENV PASSWORD pki123 
# Install required packages
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python sudo vim screen git python-twisted python-twisted-web python-twisted-web2 bash psmisc openssh-server monit nodejs npm curl build-essential

RUN useradd -r -g sudo pki

RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config

EXPOSE 22 80 443 
COPY monit/monitrc /etc/monit/
COPY Router /opt/pki/Router
COPY ca /opt/pki/ca
COPY va /opt/pki/va
COPY endpoint /opt/pki/endpoint
COPY OCSP /opt/pki/OCSP
COPY init.d/ocsp /etc/init.d/
COPY init.d/ocsp-router /etc/init.d/
COPY init.d/endpoint /etc/init.d/
COPY run.sh /run.sh
ENTRYPOINT ["/bin/bash"]
CMD ["/run.sh"]
