import json
import helper
import logging

import controllers.controller as controller


def add_client_role_mappings(user, client_role_mappings):
    for client_role_mapping in client_role_mappings:
        client = controller.get_client(client_role_mapping)
        data = []
        for client_role in client_role_mapping['clientRoles']:
            try:
                data.append(controller.get_client_role(client, client_role))
            except:
                pass
        helper.post(
            'users/{}/role-mappings/clients/{}'.format(user['id'], client['id']), json.dumps(data))


def delete_client_role_mappings(user, role_mappings):
    try:
        client_mappings = role_mappings['clientMappings']
    except:
        return
    for client_mapping in client_mappings:
        helper.delete('users/{}/role-mappings/clients/{}'.format(
            user['id'], client_mappings[client_mapping]['id']), json.dumps(client_mappings[client_mapping]['mappings']))


def get_role_mappings(user):
    return helper.get('users/{}/role-mappings'.format(user['id'])).json()


def get_user(input_user):
    users = helper.get('users?username={}'.format(
        input_user['username'])).json()
    try:
        output_user = next(
            user for user in users if input_user['username'] == user['username'])
    except:
        logging.warning('user "{}" was not found'.format(
            input_user['username']))
        raise
    return output_user


def set_client_role_mappings(user):
    try:
        client_role_mappings = user['clientRoleMappings']
    except:
        logging.error(
            'attribute "clientRoleMappings" missing for user "{}"'.format(user['username']))
        raise
    user = get_user(user)
    role_mappings = get_role_mappings(user)
    delete_client_role_mappings(user, role_mappings)
    add_client_role_mappings(user, client_role_mappings)
