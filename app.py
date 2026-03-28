from flask import Flask
import os
from routes.main import main_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.secret_key = "super_secret_key_A free life"

# 注册 Blueprint
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
