from flask import Flask, jsonify, render_template_string
from pokenea import POKENEAS
import random
import os
import boto3
import socket
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
    region_name=os.getenv("AWS_REGION"),
)

S3_BUCKET = os.getenv("S3_BUCKET", "pokenea-camilamartinezm")

@app.route("/app/pokenea")
def pokenea_json():
    p = random.choice(POKENEAS)
    return jsonify({
        "id": p.id,
        "nombre": p.nombre,
        "altura": p.altura,
        "habilidad": p.habilidad,
        "container_id": socket.gethostname(),
    })

@app.route("/")
def pokenea_view():
    p = random.choice(POKENEAS)
    imagen_url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": S3_BUCKET, "Key": p.imagen_key},
        ExpiresIn=3600
    )

    print("🔗 Imagen URL:", imagen_url)  

    html = """
    <h1>{{ nombre }}</h1>
    <div>
      <img src="{{ imagen_url }}" style="max-width:300px;"><br>
      <em>{{ frase }}</em><br>
      <small>Container: {{ container_id }}</small>
    </div>
    """
    return render_template_string(
        html,
        nombre=p.nombre,
        imagen_url=imagen_url,
        frase=p.frase,
        container_id=socket.gethostname()
    )

@app.route("/pokeneas")
def listar_pokeneas():
    listado = []
    for p in POKENEAS:
        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": S3_BUCKET, "Key": p.imagen_key},
            ExpiresIn=3600
        )
        listado.append({
            "id": p.id,
            "nombre": p.nombre,
            "imagen_url": url
        })

    html = """
    <h1>Listado de Pokeneas</h1>
    <ul>
      {% for item in listado %}
        <li>
          <strong>{{ item.nombre }}</strong><br>
          <img src="{{ item.imagen_url }}" width="200"><br>
        </li>
      {% endfor %}
    </ul>
    """
    return render_template_string(html, listado=listado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)