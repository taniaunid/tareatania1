import web

db_host = 'o3iyl77734b9n3tg.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'tiendasp'
db_user = 'nbzpgtxci4njmbjh'
db_pw = 'iplnypvz0xzh0vqv'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )