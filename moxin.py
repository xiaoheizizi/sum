from gensim.models import Word2Vec


model = Word2Vec(vector_size=100,window=5, min_count=5,workers=4)
model.build_vocab(corpus_file=r"aa(1).txt")
to_word = sum(len(sentence.split()) for sentence in open(r"aa(1).txt", 'r', encoding='utf-8'))
model.train(corpus_file=r"aa(1).txt",total_words=to_word,total_examples=model.corpus_count,epochs=5)
model.save('wenbenmoxing.bin')
print(model.wv.similarity('情侣', '夫妻'))
# for w in model.wv.index_to_key:
#     print(w)
#     input()
# list = [2,7,11,15]
# n = len(list)
# target=9
# res = []  # 空列表
# r = n - 1  # 列表长度减一
# for l in range(n):  # 循环列表的长度
#     #         列表的第一位
#     # print(list[l])
#     # print(list[r])
#     while list[l] + list[r] > target:
#         r -= 1
#     if list[l] + list[r] == target:
#         print([l + 1, r + 1])
