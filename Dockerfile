FROM ubuntu:vivid
MAINTAINER ch@mosaiksoftware.de

# Install required packages
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python sudo vim screen git python-twisted python-twisted-web python-twisted-web2

RUN useradd -r -g sudo pki

EXPOSE 22 80 443 
CMD ["/bin/bash"]
