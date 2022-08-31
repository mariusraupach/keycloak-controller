import helper
import logging


def get_client(input_client):
    clients = helper.get('clients').json()
    try:
        output_client = next(
            client for client in clients if input_client['clientId'] == client['clientId'])
    except:
        logging.warning('client "{}" was not found'.format(
            input_client['clientId']))
        return
    return output_client


def get_client_role(client, input_role):
    roles = helper.get(
        'clients/{}/roles'.format(client['id'], input_role)).json()
    try:
        output_role = next(
            role for role in roles if input_role == role['name'])
    except:
        logging.warning('role "{}" from client "{}" was not found'.format(
            input_role, client['clientId']))
        raise
    return output_role
