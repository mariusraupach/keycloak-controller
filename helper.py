import os
import requests


def delete(path, data):
    url = get_url(path)
    headers = get_headers()
    return requests.request('DELETE', url, data=data, headers=headers)


def get(path):
    access_token = get_access_token()
    url = get_url(path)
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    return requests.request('GET', url, headers=headers)


def get_access_token():
    host = os.getenv('HOST')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    url = '{}realms/master/protocol/openid-connect/token'.format(host)
    data = 'client_id=admin-cli&username={}&password={}&grant_type=password'.format(
        username, password)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.request('POST', url, data=data, headers=headers).json()['access_token']


def get_headers():
    access_token = get_access_token()
    return {'Authorization': 'Bearer {}'.format(access_token), 'Content-Type': 'application/json'}


def get_url(path):
    host = os.getenv('HOST')
    realm = os.getenv('REALM')
    return '{}admin/realms/{}/{}'.format(host, realm, path)


def post(path, data):
    url = get_url(path)
    headers = get_headers()
    return requests.request('POST', url, data=data, headers=headers)
