FROM ubuntu:vivid
MAINTAINER ch@mosaiksoftware.de

# Install required packages
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python sudo vim screen git

RUN useradd -r -g sudo pki

EXPOSE 22 80 
CMD ["/bin/bash"]
