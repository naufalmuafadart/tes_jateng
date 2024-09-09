import helper.database.connection as connection

def insert(_id, token):
    conn = connection.get()
    cur = conn.cursor()
    sql = "INSERT INTO `auth` (`id`, `user_id`, `token`) VALUES (NULL, %s, %s);"
    cur.execute(sql, (_id, token))
    conn.commit()
    conn.close()

def delete(user_id):
    conn = connection.get()
    cur = conn.cursor()
    sql = "DELETE FROM `auth` WHERE `user_id` = %s;"
    cur.execute(sql, user_id)
    conn.commit()
    conn.close()
