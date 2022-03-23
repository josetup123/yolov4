# Mushroom Detector using YOLOv4, Streamlit and Docker

## Installation Steps:

### Create a folder in your current home directory
This folder will hold the Mushroom Detector.
```shell
mkdir mushroom_app
```

### Download the Docker image

It is required to download the application 
............ You will get a *.tar.gz

```shell
wget .....
```


### Unzip the contents using gzip

```shell

gzip -d mushroom_app_21032022_latest.tar.gz
gzip -d mushroom_app_21032022.tar.gz


```



sudo docker save -o mushroom_app_21032022_latest.tar mushroom_app:latest


#compress using gzip
sudo gzip mushroom_app_21032022_latest.tar
sudo gzip mushroom_app_21032022.tar

#uncompress
#deploy


#now create a detached container
sudo docker run -dit mushroom_app:latest
sudo docker exec cc7dd0fffe75 /app/init_script.sh -dit

