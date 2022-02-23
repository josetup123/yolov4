# yolov4
# yolov4

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

#IM USING UBUNTU

#go to /home/beto/ folder
cd /home/beto

#PASTE yolov4 folder google drive in /home/beto

#EDIT  obj.data NEW CONTENT:
classes=1
train=/home/beto/darknet/data/train.txt
valid=/home/beto/darknet/data/test.txt
names=/home/beto/darknet/data/obj.names
backup=/home/beto/yolov4/backup

#INSTALL DPKG
sudo dpkg --configure -a

#INSTALL OPEN CV
sudo apt install libopencv-dev

#OPENCV PYTHON
pip install opencv-python


#DELETE FOLDER IF ALREADY INSTALLED
rm -rf darknet


#Darknet's Repo
git clone https://github.com/AlexeyAB/darknet


#TO RUN WITH CPU ONLY
cd darknet
sed -i 's/OPENCV=0/OPENCV=1/' Makefile







#INSTALL OPENCV
pip install opencv-contrib-python
sudo apt install libopencv-dev


#FIX THE FILE IF REQUIRED
#It seems there are some missing header lines in file /src/image_opencv.cpp, add these lines at the beginning than make it again.

#include "opencv2/core/core_c.h"
#include "opencv2/videoio/legacy/constants_c.h"
#include "opencv2/highgui/highgui_c.h"

#Additionally, you have to change the line IplImage ipl = m to IplImage ipl = cvIplImage(m); in the same file.




#BUILD DARKNET
make


#obj and test files
cp ../yolov4/obj.zip ../
cp ../yolov4/test.zip ../

# unzipping in darknet folder
unzip ../obj.zip -d data/
unzip ../test.zip -d data/


# Config File
cp ../yolov4/yolov4-obj.cfg ./cfg


# names & data
#NOTE: OBJ FILES DATA WAS MODIFIED INTERNALLY NOW IT USES FULL PATH
cp ../yolov4/obj.names ./data
cp ../yolov4/obj.data  ./data

# path 
cp ../yolov4/generate_train.py ./
cp ../yolov4/generate_test.py ./

#generate
python3 generate_train.py 
python3 generate_test.py

#VERIFY CONTENT
ls data/

#conv weight
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137



#TRANSFORM TO UNIX DATA Y NAMES
dos2unix data/obj.data
dos2unix data/obj.names



# Test Mode
cd cfg
sed -i 's/batch=64/batch=1/' yolov4-obj.cfg
sed -i 's/subdivisions=16/subdivisions=1/' yolov4-obj.cfg
cd ..



#TO PREDICT
ls "../yolov4/imagestest"




#RUN QUERY WITH FIXED PATH
./darknet detector test /home/beto/darknet/data/obj.data /home/beto/darknet/cfg/yolov4-obj.cfg /home/beto/yolov4/backup/yolov4-obj_last.weights /home/beto/yolov4/imagestest/25.13.2.1-4.jpg  -thresh 0.3

#SEE IT IN YOUR FTP FOLDER
sudo cp predictions.jpg /srv/ftp/new_location




#CREATE A PYTHON HANDLER AND FAKE FUNCTION TO RUN YOLO in darknet folder

vim run_yolo.py







import subprocess
import ast
from statistics import mean

def main():
    print("0")

def run(path):
    url="./darknet detector test /home/beto/darknet/data/obj.data /home/beto/darknet/cfg/yolov4-obj.cfg /home/beto/yolov4/backup/yolov4-obj_last.weights " + str(path) +"  -dont_show -thresh 0.4"
    #CREATES A PREDICTION
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
