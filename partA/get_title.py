import pymysql
import requests
from bs4 import BeautifulSoup as bs
import time

def select_form(url_list):
    db = pymysql.connect(host = "localhost", user = "root", password = "Apply@1997", database = "sys")

    cursor = db.cursor()

    sql = "select title from parse_url"
    # sql = "select * from parse_url where id>=29189 and id <= 29245"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            url = row[0]
            if url_list.count(url) == 0:
                url_list.append(url)

    except Exception as e:
        print("查询出错：case%s"%e)

    finally:
        cursor.close()
        db.close()

def insert_form(url_list):
    # 打开数据库连接
    db = pymysql.connect(host = "localhost", user = "root", password = "Apply@1997", database = "sys")
    cur = db.cursor()
    url = ""
    # SQL 查询语句
    sql = "UPDATE parse_url SET title = '%s' WHERE title = '%s' "
    title = ""
    for url in url_list:
        try:
            title = getTitle(url)
            title = handleTitle(title)
            cur.execute(sql % (title, url))  # 像sql语句传递参数
            db.commit()
        except Exception as e:
            print("first try")
            print(url)
            print(e)
            db.rollback()

    print(title)

    db.close()

def handleTitle(title):
    title = title.replace("\n", " ")
    title = title.replace("'", " ")
    return title

def getTitle(url):
    title = ""
    try:
        res = requests.get(url)
        res.encoding = 'utf-8'  #
        soup = bs(res.text, 'lxml')
        title = soup.title.text
    except Exception:
        print("error")
    print(title)
    return title

def main():
    # getTitle('https://t.co/Dwk6u8GzsC')
    url_list = []
    select_form(url_list)
    print(url_list)
    insert_form(url_list)


if __name__ == '__main__':
    main()
