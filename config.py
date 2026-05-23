class Config:
    SECRET_KEY = "this-is-a-long-random-secret-key-32chars!"
    SQLALCHEMY_DATABASE_URI = "sqlite:///expenses.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "this-is-a-long-jwt-secret-key-32chars!!"
