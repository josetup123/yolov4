# Mushroom Detector using yolov4, streamlit and Ubuntu server



#INSTALLATION PROCESS

mkdir mushroom_app


git clone https://github.com/josetup123/yolov4.git




#INSTALL ENV VIRTUAL
sudo apt install -y python3-venv

#GO TO DOLDER
cd mushroom_app

python3 -m venv my_env

#activate env

source my_env/bin/activate



#INSTALL GDRIVE
pip install gdown


#CREATE A FOLDER "BACKUP" IN YOLOV4
#DOWNLOAD WEIGHTS TRAINED


gdown --id 1HOZrGiSpKXkNwoaO_C4pL5UuNz2WaEsJ --output yolov4-obj_last.weights



#DOWNLOAD OBJ AND TEST ZIP IN YOLOV4 FOLDER


gdown --id 1Ct3wC4tbasUhWdkD3K6g5TrLz0yNmmbI --output obj.zip
gdown --id 1af9aCNLGORt7cyCfK0ZdU1Nh4U_PKRFA --output test.zip


#NOW YOLOv4 FOLDER IS READY




#EDIT  obj.data NEW CONTENT: (FULL PATH)
classes=1
train=/home/beto/darknet/data/train.txt
valid=/home/beto/darknet/data/test.txt
names=/home/beto/darknet/data/obj.names
backup=/home/beto/yolov4/backup


#INSTALL OPEN CV
sudo apt install libopencv-dev

#OPENCV PYTHON
pip install opencv-python





#Darknet's Repo
git clone https://github.com/AlexeyAB/darknet


#TO RUN WITH CPU ONLY
cd darknet
sed -i 's/OPENCV=0/OPENCV=1/' Makefile







#INSTALL OPENCV
pip install opencv-contrib-python



#FIX THE FILE (IF REQUIRED) -OPEN CV

#It seems there are some missing header lines in file /src/image_opencv.cpp, add these lines at the beginning than make it again.

#include "opencv2/core/core_c.h"
#include "opencv2/videoio/legacy/constants_c.h"
#include "opencv2/highgui/highgui_c.h"

#Additionally, you have to change the line IplImage ipl = m to IplImage ipl = cvIplImage(m); in the same file.




#BUILD DARKNET
make


#obj and test files FROM DARKNET FOLDER

cp ../yolov4/obj.zip ../
cp ../yolov4/test.zip ../

# unzipping in darknet folderFROM DARKNET FOLDER

unzip ../obj.zip -d data/
unzip ../test.zip -d data/


# Config File FROM DARKNET FOLDER
cp ../yolov4/yolov4-obj.cfg ./cfg


# names & data FROM DARKNET FOLDER
#NOTE: OBJ FILES DATA WAS MODIFIED INTERNALLY NOW THEY USE FULL PATH
cp ../yolov4/obj.names ./data
cp ../yolov4/obj.data  ./data

# path  FROM DARKNET FOLDER
cp ../yolov4/generate_train.py ./
cp ../yolov4/generate_test.py ./

#generate FROM DARKNET FOLDER
python3 generate_train.py 
python3 generate_test.py


#conv weight FROM DARKNET FOLDER
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137



#TRANSFORM TO UNIX DATA Y NAMES FROM DARKNET FOLDER
dos2unix data/obj.data
dos2unix data/obj.names



# Test Mode FROM DARKNET FOLDER
cd cfg
sed -i 's/batch=64/batch=1/' yolov4-obj.cfg
sed -i 's/subdivisions=16/subdivisions=1/' yolov4-obj.cfg
cd ..



#TO PREDICT FROM DARKNET FOLDER
ls "../yolov4/imagestest"




#RUN QUERY WITH FIXED PATH FROM DARKNET FOLDER
./darknet detector test /home/jose/mushroom_app/darknet/data/obj.data /home/jose/mushroom_app/darknet/cfg/yolov4-obj.cfg /home/jose/mushroom_app/yolov4/backup/yolov4-obj_last.weights /home/jose/mushroom_app/yolov4/imagestest/25.13.2.1-4.jpg  -thresh 0.4





#CREATE A PYTHON HANDLER AND FAKE FUNCTION TO RUN YOLO in darknet folder

vim run_yolo.py







import subprocess
import ast
from statistics import mean

def main():
    print("0")

def run(path):
    

    url="./darknet detector test /home/jose/mushroom_app/darknet/data/obj.data /home/jose/mushroom_app/darknet/cfg/yolov4-obj.cfg /home/jose/mushroom_app/yolov4/backup/yolov4-obj_last.weights " + str(path) +"  -dont_show -thresh 0.4"
    print(url)
    p = subprocess.Popen(url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    log=p.stdout.readlines()
    print(log,file=open("out_model.txt","w") )
    
    
    with open('out_model.txt', 'r') as f:
            mylist = ast.literal_eval(f.read())
    print(mylist)

    separated=[]
    for i in mylist:
            
            if "Mushroom" in str(i):
                    pre_s=str(i).split(" ")
                    pre_s=pre_s[-1]
                    pre_s=pre_s.split("%")
                    pre_s=pre_s[0]
                    separated.append(int(pre_s))

    value_m=str(len(separated))
    confidence=str(round(mean(separated),1))
    data="There are "+str(value_m)+ " Mushrooms in the Image"
    confidence= "The confidence level is " + confidence+ " % "
    print(data)
    print(confidence)
    print(        data  ,confidence,file=open("out.txt","w") )
    print(        data  ,confidence)



if __name__ == "__main__":
    main()



#GO TO YOLOV4/APP FOLDER 

#EDIT PATHS


#RUN STREAMLIT FROM DARKNET FOLDER


streamlit run ../yolov4/app/main.py 8501




