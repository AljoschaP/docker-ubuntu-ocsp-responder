FROM ubuntu:12.04
MAINTAINER ch@mosaiksoftware.de

#default password for pki user
ENV PASSWORD pki123 
# Install required packages
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python sudo vim screen git python-twisted python-twisted-web python-twisted-web2 bash openssh-server monit nodejs build-essential

RUN useradd -r -g sudo pki

EXPOSE 22 80 443 
COPY monit/monitrc /etc/monit/
COPY Router /home/pki/
COPY ca /home/pki/
COPY va /home/pki/
COPY init.d/openssl-ocsp /etc/init.d/
COPY run.sh /run.sh
ENTRYPOINT ["/bin/bash"]
CMD ["/run.sh"]
