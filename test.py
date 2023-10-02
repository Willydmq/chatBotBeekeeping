from app import app
from utils import procesar_pregunta

pregunta = "Cual es el papel de las abejas"

with app.test_client() as client:
    resp = client.post("/respond", data={"pregunta": pregunta})
    print(resp.data)


respuesta = procesar_pregunta(pregunta)

print(respuesta)
