import kdxf_stt
import audio_transform
import os  

# 获取当前执行脚本的绝对路径  
current_script_path = os.path.abspath(__file__)  

# 获取当前执行脚本所在的目录  
current_directory = os.path.dirname(current_script_path)  

APP_ID = "a2120650"
SECRET_KEY = "4a73c6a803f7517f924a04ecc7755cf8"

print(current_directory)