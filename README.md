# Mushroom Detector using YOLOv4, Streamlit and Docker

## Installation Steps:

## Docker image download:

* The installation requires Docker to be installed in the server
* Optional:
[Docker installation on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

### Create a folder in your current home directory

* This folder will hold the Mushroom Detector.

```shell
mkdir mushroom_app
```

### Download the Docker image

* It is required to download the application (*.tar.gz) file via ftp

```shell
ftp sadie.ise.utk.edu

```
* user: anonymous
* pass: anonymous


```shell
tick
```

* By using tick you can monitor progress

```shell
get mushroom_app_21032022_latest.tar.gz
```

* Close and exit the ftp conection

```shell
exit
```

## Installation:

### Unzip the contents using gzip

* Now, the Docker image will be ready to load it into your docker installation

```shell
gzip -d mushroom_app_21032022_latest.tar.gz
```
* By applying "load" the image will be uploaded to the current Docker installation

```shell
sudo docker load -i mushroom_app_21032022_latest.tar
```

## Set up and start:

* Now create a detached container

```shell
sudo docker run -dit mushroom_app:latest
```

* get ID of container


```shell
sudo docker exec cc7dd0fffe75 /app/init_script.sh -dit
```


