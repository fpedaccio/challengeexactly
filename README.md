# challengeexactly
https://mia-platform.notion.site/Python-Code-Challenge-a22d7a74316749df80e5f69bfa6863d6

---
Decidi realizar esta challenge con FASTAPI ya que provee un rapido desarrollo para una pequeña api como esta. Aportando un codigo claro y conciso.
Sin embargo este es un framework desconocido para mi. Yo trabajo con Django y nunca habia usado fastapi. 
Pero nuevamente, decidi usarlo porque iba a aportar claridad y rapidez a esta pequeña api comparado con la gran estructura de Django.
Creo que esto tambien es una demostracion de mi rapido aprendizaje y motivacion por conocer cosas nuevas.
---

### Configuaraciones
En la carpeta firestore_st se encuentra un archivo de settings. En ese archivo debe configurarse la ruta al archivo json de credenciales de firestore.

### Instalacion
- Clonar el repositorio
- moverse a la carpeta
- pip install -r requirements.txt
- uvicorn api:app --reload para correr el servidor

### endpoints
/docs - documentacion de la api pedida
/api/borrows - obtiene los ultimos 20 prestamos, los guarda en firestore y devuelte la cuenta de cuantos prestamos se han almacenado
/api/borrows/obtain/{amount} - endpoints adicional para obtener un numero de prestamos guardados en firestore
