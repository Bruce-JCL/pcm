import os
from pocketsphinx import AudioFile, get_model_path

model_path = get_model_path() #获取声学模型、语言模型及语言字典模型库地址
model_path = model_path + "/en-us"
file_path = "output.wav"  #导入要进行语音识别的音频文件
config = {
    'verbose': False,  #设置运行的时候不显示详细信息
    'audio_file': file_path,  #用于转换的音频文件的路径
    'buffer_size': 2048,  #读取的数据大小为2048字节
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'en-us'),  #声学模型路径
    'lm': os.path.join(model_path, 'en-us.lm.bin'),  #语言模型路径
    'dict': os.path.join(model_path, 'cmudict-en-us.dict')  #语音字典路径
}


print("正在转换 " + file_path + "到文字.....")
audio = AudioFile(**config)
for phrase in audio: #循环识别
    print(phrase)
