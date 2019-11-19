import pymysql


class OperateMysql:
    def __init__(self, host=None, port=None, password=None, db=None, user=None):
        """
        �������ݿ�
        :param host: ����ip
        :param port: �˿ں�
        :param password: ���ݿ�����
        :param db: ���ݿ���
        :param user: ���ݿ��û�
        """
        self.db = pymysql.connect(
            host=host,
            port=port,
            password=password,
            db=db,
            user=user
        )

    def operate(self, sql):
        """
        ��ȡ����
        :param sql: Ҫִ�е�sql���
        :return: ���ز�ѯ�õ��Ľ��
        """
        cursor = self.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        self.db.commit()
        return result

    def __del__(self):
        """
        �ر����ݿ�����
        :return:�޷���ֵ
        """
        self.db.close()
