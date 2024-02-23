from clean_data import CleanData

"""
清洗数据，去除停用词，然后分词。
"""
def process_data(filename):
    f_w=open("data/cleandata.txt", "w", encoding="utf8")
    op=CleanData("data/hit_stopwords.txt")
    with open(filename,"r",encoding="utf8") as f:
        for line in f:
            line=line.strip("\n")
            newline=op.get_result(line)
            f_w.write(newline+"\n")
    f_w.close()
process_data("data/data.txt")
"""
csv文件，tsv文件，以及excel文件以.xlsx 结尾的文件，
打开文件，读取内容
"""
import pandas as pd
import openpyxl

def deal_csv(csvfile):
    data=pd.read_csv(csvfile)
    data.to_excel("1.xlsx")

def deal_tsv(tsvfile):
    data=pd.read_csv(tsvfile,sep="\t")
    data.to_excel("2.xlsx")

def deal_excel(excelfile):
    wb=openpyxl.load_workbook(excelfile)#
    sheet=wb.active
    data=[]
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))

    csv_file='outputexcel1.csv'
    import csv
    with open(csv_file,mode='w',newline='',encoding='utf8') as f:
        writer=csv.writer(f)
        writer.writerows(data)

if __name__=="__main__":
    deal_csv(r"E:\po\pythonProject\p3\submission.csv")
    deal_tsv(r"E:\po\pythonProject\analysis\train.tsv")
    deal_excel("1.xlsx")