from distutils.command.upload import upload
import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import sys
from PIL import Image 
sys.path.insert(0, '/home/beto/darknet')





import run_yolo as rn

def load_image(image_file):
	img = Image.open(image_file)
	return img 



st.title("Harvest detector using YOLOv4 ")

st.image("/home/beto/yolov4/app/example.jpg",width=240,use_column_width='auto')


uploaded_file = st.file_uploader("Upload Files",type=['jpg'])


footer="<style> footer {visibility: hidden;}footer:after {content:' Made by: Jose Tupayachi 2022 Applicant for the PhD program at Tennessee Knoxville'; visibility: visible;display: block;position: relative;padding: 5px;top: 2px;} </style>"

st.markdown(footer, unsafe_allow_html=True)


if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    
    #st.write(file_details)
    img = load_image(uploaded_file)
    #save image
    path="/home/beto/yolov4/app/images/"
    with open (path+uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success ("File loaded")
    data=rn.run(path+uploaded_file.name)
    print(data)
    st.image("/home/beto/darknet/predictions.jpg")
    f = open('/home/beto/darknet/out.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()
    st.success (file_contents)
    
    
