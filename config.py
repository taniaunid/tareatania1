import web

db_host = 'wvulqmhjj9tbtc1w.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'v7faclb4mmjul7tb'
db_user = 'krh9wiqawitogjot'
db_pw = 'j7zzfidzmjlfbx58'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
