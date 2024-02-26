import jieba
stopwords = set()
with open('hit_stopwords.txt','r',encoding='utf8')as f:
    for line in f:
        stopwords.add(line.strip())
with open('att.txt','r',encoding='utf8')as lnfile:
    lines = lnfile.readlines()
processed_lines=[]
for line in lines:
    seg_list = jieba.lcut(line)
    seg_list=[word for word in seg_list]
    processed_line = ' '.join(seg_list)
    processed_lines.append(processed_line)
with open('Att-t.txt.txt','w',encoding='utf8')as outfile:
    outfile.writelines('\n'.join(processed_lines))
