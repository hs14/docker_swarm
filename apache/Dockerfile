FROM centos:8

RUN yum install -y httpd
RUN echo "" >> /etc/httpd/conf/httpd.conf
RUN echo "ProxyRequests Off" >> /etc/httpd/conf/httpd.conf
RUN echo "ProxyPass / http://ap_flask:8000/" >> /etc/httpd/conf/httpd.conf
RUN echo "ProxyPassReverse / http://ap_flask:8000/" >> /etc/httpd/conf/httpd.conf

EXPOSE 80

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
