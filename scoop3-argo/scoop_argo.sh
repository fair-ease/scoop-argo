#!/bin/bash
SCOOP3_JAR=./scoop_argo/scoop3-argo-controller-1.40-executable.jar
PROPERTIES=./properties
/usr/bin/java -Xms1024m -classpath ${PROPERTIES}:${SCOOP3_JAR} fr.ifremer.scoop3.argo.application.ArgoApplication
