import dotenv
import json
import logging

import controllers.group_controller as group_controller
import controllers.user_controller as user_controller


def main():
    with open('data/groups.json') as f:
        groups = json.load(f)
    for group in groups:
        try:
            group_controller.set_client_role_mappings(group)
        except:
            continue
    with open('data/users.json') as f:
        users = json.load(f)
    for user in users:
        try:
            user_controller.set_client_role_mappings(user)
        except:
            print('error')
            continue


if __name__ == '__main__':
    logging.basicConfig(filename='logs/main.log',
                        format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO, encoding='utf-8')
    dotenv.load_dotenv()
    main()
