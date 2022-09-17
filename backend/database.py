import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

class MailDatabase():
    def __init__(self, db_file):
        self.db_file= db_file
        self.mail_table = """ CREATE TABLE IF NOT EXISTS mail(
                                        id,
                                        sender,
                                        receiver,
                                        subject,
                                        content,
                                        next_id,
                                        prev_id,
                                        read,
                                        timestamp
                                    ); """

        self.conn = create_connection(self.db_file)
        self.cur = self.conn.cursor()
        create_table(self.conn, self.mail_table)
        res = self.cur.execute("SELECT MAX(id) FROM mail")
        self.curr_id = res.fetchone()[0]
        if self.curr_id is None:
            self.curr_id = -1
        print("CURR_ID", self.curr_id)

    def add_mail(self, mail):
        create_tuple = (mail.id,mail.sender,mail.receiver,mail.subject,mail.content,mail.next_id,mail.prev_id,mail.read,mail.timestamp)
        self.cur.execute("INSERT INTO mail VALUES(?,?,?,?,?,?,?,?,?)", create_tuple)
        self.conn.commit()
        return self.cur.lastrowid #just in case you want the lastrowd id created by the cursor dont think it would be necessary
        
    def get_all_mail(self):
        res = self.cur.execute("SELECT id, sender, receiver, subject, content, next_id, prev_id, read, timestamp FROM mail ORDER BY id")
        result = res.fetchall()
        return result


    def get_mail_by_id(self, id): #DK if it will work this way compared to using fetching all and searching the list but me will try it out; less lines 
        self.cur.execute("SELECT * FROM mail WHERE id=?",(id,))
        mail = self.cur.fetchone() #hopefully this will work if not im gonna have to code a regular list search function.
        return mail

    def update_mail_by_id(self, id, key, value):
        sq1 = f'''UPDATE mail
                  SET {key} = ?
                  WHERE id = ?
               '''
        self.cur.execute(sq1,(value, id))
        self.conn.commit()

    def get_new_id(self):
        self.curr_id += 1
        return self.curr_id

class GameDatabase():
    def __init__(self, db_file):
        self.db_file = db_file
        self.stats_table = """CREATE TABLE IF NOT EXISTS stats(user_id, points, emails_sent, emails_received, fastest_response); """
        self.conn = create_connection(self.db_file)
        self.cur = self.conn.cursor()
        create_table(self.conn, self.stats_table)


    #For testing purposes this will only have one user but since we're using a database can be done wiht multiple users
    def set_stats(self,user_id,points,emails_sent,emails_received,fastest_response):
        create_tuple = (user_id, points, emails_sent, emails_received, fastest_response)
        self.cur.execute("INSERT INTO stats VALUES(?,?,?,?,?)", create_tuple)
        self.conn.commit()
        return self.cur.lastrowid

    def get_stats(self):
        self.cur.execute("SELECT * FROM stats")
        stats = self.cur.fetchone()
        print(stats)
        return stats

    def update_generic(self, key, value, user_id=0): #possibly for more users in the future
        sq1 = f'''UPDATE stats
                  SET {key} = ?
                  WHERE user_id = ?
                    '''
        self.cur.execute(sq1,(value, user_id))
        self.conn.commit()

    def update_points(self,new_points):
        self.update_generic('points', new_points)

    def update_emails_sent(self, new_emails_sent):
        self.update_generic('emails_sent', new_emails_sent)

    def update_emails_received(self, new_emails_received):
        self.update_generic('emails_received', new_emails_received)

    def update_fastest_response(self, new_fastest_response):
        self.update_generic('fastest_response', new_fastest_response)

