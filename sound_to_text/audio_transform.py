from pydub import AudioSegment  # 导入pydub库中的AudioSegment类，用于处理音频文件  
import os  

# 获取当前执行脚本的绝对路径  
current_script_path = os.path.abspath(__file__)  

# 获取当前执行脚本所在的目录  
current_directory = os.path.dirname(current_script_path)  

print("当前执行脚本所在目录:", current_directory)

def trans_mp3_to_other(filepath, hz):  # 定义一个函数，接受音频文件路径和目标格式  
    song = AudioSegment.from_mp3(filepath)  # 从指定的MP3文件加载音频  
    song.export("Newsound." + str(hz), format=str(hz))  # 将音频导出为指定格式的文件，文件名为"Newsound.目标格式"  

def trans_wav_to_other(filepath, hz):  # 定义一个函数，接受WAV文件路径和目标格式  
    song = AudioSegment.from_wav(filepath)  # 从指定的WAV文件加载音频  
    song.export("Newsound." + str(hz), format=str(hz))  # 将音频导出为指定格式的文件  

def trans_ogg_to_other(filepath, hz):  # 定义一个函数，接受OGG文件路径和目标格式  
    song = AudioSegment.from_ogg(filepath)  # 从指定的OGG文件加载音频  
    song.export("Newsound." + str(hz), format=str(hz))  # 将音频导出为指定格式的文件  

def trans_flac_to_other(filepath, hz):  # 定义一个函数，接受FLAC文件路径和目标格式  
    song = AudioSegment.from_file(filepath)  # 从指定的FLAC文件加载音频（支持多种格式）  
    song.export("Newsound." + str(hz), format=str(hz))  # 将音频导出为指定格式的文件  

def trans_m4a_to_other(filepath, hz, path):  # 定义一个函数，接受M4A文件路径和目标格式  
    song = AudioSegment.from_file(filepath)  # 从指定的M4A文件加载音频（支持多种格式）  
    song.export("Newsound." + str(hz), format=str(hz))  # 将音频导出为指定格式的文件  

# 参数1：音频路径， 参数2：转换后的格式  
trans_m4a_to_other(current_directory+"/"+"test_record.m4a", "MP3")  # 调用转换函数，将M4A文件转换为MP3格式