FROM eclipse-temurin:17
RUN apt-get update && apt-get install -y unzip
COPY xl-deploy-*.zip /opt/
RUN unzip opt/xl-deploy-*.zip -d /opt/
RUN mv /opt/xl-deploy-*-server /opt/xl-deploy-server
COPY deployit.conf /opt/xl-deploy-server/conf/
COPY deployit-license.lic /opt/xl-deploy-server/conf/
COPY deploy-repository.yaml /opt/xl-deploy-server/centralConfiguration/
CMD ["/opt/xl-deploy-server/bin/run.sh"]
