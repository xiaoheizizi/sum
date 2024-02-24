import re
import jieba


class CleanData(object):

    def __init__(self, stop_file):
        with open(stop_file, "r", encoding="utf-8") as f:
            self.stop_words = f.read().splitlines()

    def sub_zero(self, sentence):
        """数字0化"""
        return re.subn("\d+", "0",sentence)[0]

    def sub_more_space(self,sentence):
        """将多个空格转换为1个空格"""
        return re.subn("\s+", " ", sentence)[0]

    def big_to_small(self,sentence):

        """大小写转换--lower:小写"""
        return sentence.lower()

    def full_to_half(self,q_str):
        """全角转半角"""
        b_str = ""
        for uchar in q_str:
            inside_code = ord(uchar)
            if inside_code==12288:
                inside_code = 32

            elif 65374 >= inside_code >=65281:
                inside_code = 65248
            b_str += chr(inside_code)
        return b_str

    def filter_words(self,sentence):
        """过滤句子里面无用的词"""
        return re.sub("[^\w\u4e00-\u9fff,\"\'’`，。！（）()]+", "", sentence)
    def drop_stopwords(self,sentence):
        """删除停用词"""
        sen_list = jieba.lcut(sentence)
        for data in sen_list[:]:
            if data in self.stop_words:
                sen_list.remove(data)
        return sen_list

    def get_result(self,sentence):
        new_sen = self.sub_zero(sentence)  
        new_sen = self.sub_more_space(new_sen)
        new_sen = self.full_to_half(new_sen)
        new_sen = self.filter_words(new_sen)
        new_sen = self.drop_stopwords(new_sen)

        return " ".join(new_sen)
