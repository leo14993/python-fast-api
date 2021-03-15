# Set image argument - NÃO REMOVER ESSE ARG
ARG IMG=python:3.7-slim
# set image dynamically
FROM ${IMG}

# Set arguments to environment variable
ARG HOST=0.0.0.0
ARG PORT=8000


ARG DATABASE_ENGINE
ARG DATABASE_USER
ARG DATABASE_PASSWORD
ARG DATABASE_HOST
ARG DATABASE_PORT
ARG DATABASE_NAME
ARG REDIS_CACHE_HOST
ARG REDIS_CACHE_PORT
ARG REDIS_CACHE_DB
ARG REDIS_CACHE_PASSWORD

ENV DATABASE_ENGINE=${DATABASE_ENGINE}
ENV DATABASE_USER=${DATABASE_USER}
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}
ENV DATABASE_HOST=${DATABASE_HOST}
ENV DATABASE_PORT=${DATABASE_PORT}
ENV DATABASE_NAME=${DATABASE_NAME}

ENV REDIS_CACHE_HOST=${REDIS_CACHE_HOST}
ENV REDIS_CACHE_PORT=${REDIS_CACHE_PORT}
ENV REDIS_CACHE_DB=${REDIS_CACHE_DB}
ENV REDIS_CACHE_PASSWORD=${REDIS_CACHE_PASSWORD}



# Set environment variable
ENV ENV=${ENV}
ENV HOST=${HOST}
ENV PORT=${PORT}


# create user python
RUN useradd python

# create folders
RUN mkdir /app

# change permission for folders
RUN chmod -R a=rwx /app

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY --chown=python . /app

# install all the specific requirements for a state
RUN sh requirements.sh

# Make port 8000 available to the world outside this container
EXPOSE ${PORT}

# change to python user
USER python

CMD sh run.sh ${HOST} ${PORT}
