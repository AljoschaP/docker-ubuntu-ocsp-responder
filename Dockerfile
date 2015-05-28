FROM ubuntu:vivid
MAINTAINER ch@mosaiksoftware.de

# Install required packages
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python

EXPOSE 22 80 
CMD ["/bin/bash"]
