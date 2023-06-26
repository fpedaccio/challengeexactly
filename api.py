from fastapi import FastAPI
from settings import SUBGRAPH_ENDPOINT
from graphqlclient import GraphQLClient
import json
from firestore_st.firestore import save_borrows, count_borrows, get_borrows
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()


@app.get("/api/borrows")
async def borrows_api_get():

    ''' Obtiene los ultimos 20 prestamos y los guarda en firestore '''

    client = GraphQLClient(SUBGRAPH_ENDPOINT)

    query = """
    {
        borrows(first: 20, orderBy: timestamp, orderDirection:desc) {
            id
            market
            timestamp
            caller
            receiver
            borrower
            assets
        }
    }
    """

    response = client.execute(query)
    data = json.loads(response)
    save_borrows(data['data']['borrows'])

    return count_borrows()


@app.get("/api/borrows/obtain/{amount}")
async def borrows_api_obtain(amount: int):

    ''' Devuelve {amount} cantidad de prestamos prestamos '''

    return get_borrows(amount)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API documentation")

@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return get_openapi(title="API documentation", version="1.0.0", routes=app.routes)