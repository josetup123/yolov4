# Mushroom Detector using YOLOv4, Streamlit and Docker

## Installation Steps:

* The installation requires Docker to be installed in the server
* Optional: [Docker installation on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

## Docker image download:

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

## Set up and start:

### Unzip the contents using gzip

* Now, the Docker image will be ready to load it into your docker installation

```shell
gzip -d mushroom_app_21032022_latest.tar.gz
```
* By applying "load" the image will be uploaded to the current Docker installation

```shell
sudo docker load -i mushroom_app_21032022_latest.tar
```

* Now create a detached container

```shell
sudo docker run -dit -p  8501:8501 mushroom_app:latest
```

* Get the container_id
```shell
sudo docker ps -a
```

* Execute initialization script
```shell
sudo docker exec <container_id> /app/init_script.sh -dit
```

## Use:

* The mushroom detector now is working at <your_server_ip_addr>:8501

* You can try the application at: > [Mushroom detector](http://160.36.50.64:8501/)

![Preview](http://160.36.50.64:8501/media/f5e9bd86cfdbfc0a28b0410077eb7e8f61ae923ddb2286054d8e9820.jpeg)








