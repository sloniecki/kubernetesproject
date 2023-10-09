import jwt, datetime, os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

pswd = os.environ.get("MYSQL_PASSWORD")
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://auth_user:{pswd}@host.minikube.internal:3306/auth'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.app_context().push()
db = SQLAlchemy(server)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
User = Base.classes.user




@server.route("/login", methods=["POST"])

def login():
    auth = request.authorization
    if not auth:
        return 401
    res = db.session.query(User).filter(User.email == auth.username)
    if res > 0:
        
        for resault in res:
            email = resault.email
            password = resault.password
        
        if auth.username != email or auth.password != password:
            402
        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)

    else:
        return 401


@server.route("/validate", methods=["POST"])
def validate():
    encoded_jwt=request.headers["Authorization"]
    if not encoded_jwt:
        return 401
    encoded_jwt = encoded_jwt.split(" ")[1]

    try:
        decoded = jwt.decode(encoded_jwt, os .environ.get("JWT_SECRET"), algorithms=["HS256"])
    except:
        return 403
    
    return decoded


def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.datetime.utc)+datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)

    

