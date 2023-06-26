
from google.cloud import firestore
from firestore_st.ft_settings import CREDENTIAL_FILE


db = firestore.Client.from_service_account_json(CREDENTIAL_FILE)


def save_borrows(borrows):
    ''' Guarda una lista de diccionarios de prestamos en firestore'''

    batch = db.batch()

    for borrow in borrows:
        doc_ref = db.collection(u'borrows').document(borrow['id'])
        batch.set(doc_ref, borrow)

    batch.commit()


def count_borrows():
    ''' Cuenta la cantidad de prestamos en firestore'''

    borrows_ref = db.collection(u'borrows')
    borrows = borrows_ref.stream()
    return len(list(borrows))


def get_borrows(amount):
    ''' Devuelve {amount} cantidad de prestamos prestamos '''

    borrows_ref = db.collection(u'borrows')
    borrows = borrows_ref.limit(amount).stream()
    return [borrow.to_dict() for borrow in borrows]
