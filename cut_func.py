import jieba
import os
import re

#不存储的函数，仅返回结果，适用于处理单个句子 (list形式的)
def cut_sentence(sentence):
    text = jieba.cut(sentence,cut_all=False)
    str_out = ' '.join(text)
    str_out = re.sub(r"(?!\n)(\d|\W|_)"," ",str_out)
    return str_out


#不存储的函数，仅返回结果，适用于处理单个文档 (list形式的)
def cut_file(old_file):
    try:
        fi = open(old_file, 'r', encoding='utf-8')
    except BaseException as e:  # 因BaseException是所有错误的基类，用它可以获得所有错误类型
        print(Exception, ":", e)    # 追踪错误详细信息

    text = fi.read()  # 获取文本内容
    new_text = jieba.cut(text, cut_all=False)  # 精确模式
    str_out = ' '.join(new_text)
    str_out = re.sub(r"(?!\n)(\d|\W|_)"," ",str_out)
    
    return str_out


#数据预处理
#在根目录处运行这个程序可以将normal和spam文件夹内的所有数据进行分词
#保存在 _normal _spam文件夹内
def cut_save(old_file,path):
    global filename     # 分词之后保存的文件名
    filename = old_file + '_cut.txt'

    str_out = cut_file(old_file)
    fo = open(os.path.join('..',path,filename), 'w', encoding='utf-8')
    fo.write(str_out)
    















