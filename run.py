import os

config_name = os.getenv('FLASK_CONFIG')
app = config_name

__name__=="__main__"
app.run()
