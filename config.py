import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://employee_db_qapl_user:DGcoJouawYJcSVudzP4SYiJ7E0TBuiBs@dpg-crs1knlds78s73dvfhfg-a.oregon-postgres.render.com/employee_db_qapl')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234567'
