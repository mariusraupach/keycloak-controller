import json
import helper
import logging

import controllers.controller as controller


def add_client_role_mappings(group, client_role_mappings):
    for client_role_mapping in client_role_mappings:
        client = controller.get_client(client_role_mapping)
        data = []
        for client_role in client_role_mapping['clientRoles']:
            try:
                data.append(controller.get_client_role(client, client_role))
            except:
                pass
        helper.post(
            'groups/{}/role-mappings/clients/{}'.format(group['id'], client['id']), json.dumps(data))


def delete_client_role_mappings(group, role_mappings):
    try:
        client_mappings = role_mappings['clientMappings']
    except:
        return
    for client_mapping in client_mappings:
        helper.delete('groups/{}/role-mappings/clients/{}'.format(
            group['id'], client_mappings[client_mapping]['id']), json.dumps(client_mappings[client_mapping]['mappings']))


def get_group(input_group):
    groups = helper.get('groups').json()
    try:
        output_group = next(
            group for group in groups if input_group['name'] == group['name'])
    except:
        logging.warning('group "{}" was not found'.format(input_group['name']))
        raise
    return output_group


def get_role_mappings(group):
    return helper.get('groups/{}/role-mappings'.format(group['id'])).json()


def set_client_role_mappings(group):
    try:
        client_role_mappings = group['clientRoleMappings']
    except:
        logging.error(
            'attribute "clientRoleMappings" missing for group "{}"'.format(group['name']))
        raise
    group = get_group(group)
    role_mappings = get_role_mappings(group)
    delete_client_role_mappings(group, role_mappings)
    add_client_role_mappings(group, client_role_mappings)
