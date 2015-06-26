FROM ubuntu:vivid
MAINTAINER ch@mosaiksoftware.de

#default password for pki user
ENV PASSWORD pki123 
# Install required packages
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python sudo vim screen git python-twisted python-twisted-web python-twisted-web2 bash openssh-server monit nodejs build-essentials 

RUN useradd -r -g sudo pki

EXPOSE 22 80 443 
COPY run.sh /run.sh
ENTRYPOINT ["/bin/bash"]
CMD ["/run.sh"]
