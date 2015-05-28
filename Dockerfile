FROM ubuntu:saucy

# Install required packages
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python

CMD ["/bin/bash"]
