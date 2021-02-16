FROM centos:7
MAINTAINER George McCabe <mccabe@ucar.edu>

# Required arguments
<<<<<<< HEAD
ARG TARFILE
ARG MOUNTPT

# Check that TARFILE is defined.
RUN if [ "x${TARFILE}" == "x" ]; then \
      echo "ERROR: TARFILE undefined! Rebuild with \"--build-arg TARFILE={Data tarball name}\""; \
=======
ARG TARFILE_URL
ARG MOUNTPT

# Check that TARFILE_URL is defined.
RUN if [ "x${TARFILE_URL}" == "x" ]; then \
      echo "ERROR: TARFILE_URL undefined! Rebuild with \"--build-arg TARFILE_URL={One or more URL's}\""; \
>>>>>>> feature_803_cycloneplotter_line
      exit 1; \
    fi

# Check that MOUNTPT is defined.
RUN if [ "x${MOUNTPT}" == "x" ]; then \
<<<<<<< HEAD
      echo "ERROR: MOUNTPT undefined! Rebuild with \"--build-arg MOUNTPT={Mount point directory}\""; \
      exit 1; \
    fi

ENV CASE_DIR /data/input/METplus_Data
RUN mkdir -p ${CASE_DIR}

RUN curl -SL https://github.com/dtcenter/METplus/releases/download/${VERSION}/${TARFILE} | tar -xzC ${CASE_DIR}

VOLUME ${MOUNTPT}
=======
      echo "ERROR: MOUNTPT undefined! Rebuild with \"--build-arg MOUNTPT={VOLUME mount directory}\""; \
      exit 1; \
    fi

ENV CASE_DIR=/data/input/METplus_Data
RUN mkdir -p ${CASE_DIR}

RUN for URL in `echo ${TARFILE_URL} | tr "," " "`; do \
      echo "Downloading: ${URL}"; \
      curl -SL ${URL} | tar -xzC ${CASE_DIR}; \
    done

# Define the volume mount point
VOLUME ${MOUNTPT}

>>>>>>> feature_803_cycloneplotter_line
USER root
CMD ["true"]

