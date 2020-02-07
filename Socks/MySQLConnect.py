import mysql.connector

def main():
    cnx = mysql.connector.connect(user='wso2soadb', password='1qaz2wsx!QAZ@WSX',
                                  host='127.0.0.1')
    cursor = cnx.cursor()
    selectQuery = "SELECT * FROM socks.sample"
    insertQuery = "INSERT into `socks`.`sample` (ToeColor, Color, Length, Thickness) VALUES ('green','gray','low','wooly');"
    cursor.execute(selectQuery)
    result = cursor.fetchall()
    for x in result:
        print(x)

    cursor.execute(insertQuery)

    cursor.execute(selectQuery)
    result = cursor.fetchall()
    for x in result:
        print(x)

if __name__ == '__main__':
    main()