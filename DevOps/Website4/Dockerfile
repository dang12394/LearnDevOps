FROM centos:centos7
RUN yum update -y \
  && yum install httpd httpd-tools -y \
  && yum install vim -y \
  && yum install epel-release -y \
  && yum update -y \
  && yum install htop -y
WORKDIR /var/www/html
EXPOSE 80
COPY . /var/www/html
ENTRYPOINT ["httpd"]
CMD [ "-D", "FOREGROUND"]