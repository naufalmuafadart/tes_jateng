import helper.database.connection as connection

def insert(user_id, number, holder, month_expired, year_expired, security_code):
    conn = connection.get()
    cur = conn.cursor()
    sql = "INSERT INTO `cards` (`id`, `user_id`, `number`, `holder`, `month_expired`, `year_expired`, `security_code`) VALUES (NULL, %s, %s, %s, %s, %s, %s);"
    cur.execute(sql, (user_id, number, holder, month_expired, year_expired, security_code))
    conn.commit()
    conn.close()

def get_by_user_id(user_id):
    conn = connection.get()
    cur = conn.cursor()
    sql = "SELECT id, number, holder, CONCAT(month_expired, '/', year_expired) expired FROM `cards` WHERE `user_id` = %s"
    cur.execute(sql, (user_id,))
    result = cur.fetchall()
    conn.close()
    field_names = [i[0] for i in cur.description]
    output = []
    for i in range(len(result)):
        output.append({})
        for j in range(len(field_names)):
            output[i][field_names[j]] = result[i][j]
    return output

def get_by_id(id):
    conn = connection.get()
    cur = conn.cursor()
    sql = "SELECT id, number, holder, CONCAT(month_expired, '/', year_expired) expired FROM `cards` WHERE `id` = %s"
    cur.execute(sql, (id,))
    result = cur.fetchall()
    conn.close()
    field_names = [i[0] for i in cur.description]
    output = []
    for i in range(len(result)):
        output.append({})
        for j in range(len(field_names)):
            output[i][field_names[j]] = result[i][j]
    return output[0]
