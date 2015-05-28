FROM ubuntu:vivid
MAINTAINER ch@mosaiksoftware.de

# Install required packages
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python sudo vim screen git python-twisted python-twisted-web python-twisted-web2 bash

RUN useradd -r -g sudo pki

EXPOSE 22 80 443 
COPY run.sh /run.sh
ENTRYPOINT ["/bin/bash"]
CMD ["/run.sh"]
