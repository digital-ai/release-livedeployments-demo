FROM eclipse-temurin:21
RUN apt-get update && apt-get install -y unzip
COPY xl-release-*.zip /opt/
RUN unzip opt/xl-release-*.zip -d /opt/
RUN mv /opt/xl-release-*-server /opt/xl-release-server
COPY xl-release-server.conf /opt/xl-release-server/conf/
COPY xl-release-license.lic /opt/xl-release-server/conf/
CMD ["/opt/xl-release-server/bin/run.sh"]
