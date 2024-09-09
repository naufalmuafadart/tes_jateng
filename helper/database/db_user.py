import helper.database.connection as connection
import helper.json_web_token as json_web_token

def check_login(phone_number, password):
    conn = connection.get()
    cur = conn.cursor()
    sql = "SELECT id, name FROM users WHERE phone_number = '{}' and password = '{}';".format(phone_number,
                                                                                                      password)
    cur.execute(sql)
    output = cur.fetchall()
    if len(output) == 0:
        raise Exception('Phone number or password not found')
    access_token = json_web_token.generate_token(output[0][0], output[0][1], True)
    refresh_token = json_web_token.generate_token(output[0][0], output[0][1], False)
    return access_token, refresh_token, output[0][0]
