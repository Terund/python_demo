import pymysql

# �������ݿ����ӣ��������˿ڣ��û������룬����
db = pymysql.connect(
    host="localhost",# ������
    port=3306,# �˿���
    user="root",# �û���
    password="123456",# ���ݿ�����
    db="werewolf",# ���ݿ�����
)
# �õ��α�
cursor = db.cursor()
# Ҫִ�е�sql���
sql = """
    create table player(id int,addr char(32),name char(16),number int,alive_status int,info char(16));
"""
# ִ��sql���
cursor.execute(sql)
# �ύ����
db.commit()
# �ر�����
db.close()