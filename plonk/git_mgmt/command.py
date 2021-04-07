import json
import os
import subprocess
import sys

from plonk import cli
from PyInquirer import prompt
from plonk.utils.logger import logger
from plonk.utils.utils import style, get_script_path

home = os.environ['HOME']
SSH_CONFIG_PATH = os.path.join(home, ".ssh", "ssh-config.json")

dir_path = os.path.dirname(os.path.realpath(__file__))

questions = [
    {
        'type': 'list',
        'name': 'git-config',
        'message': 'What do you want?',
        'choices': [
            {
                'key': 0,
                'name': 'Add user account',
                'value': 'add'
            },
            {
                'key': 1,
                'name': 'Remove user account',
                'value': 'remove'
            },
            {
                'key': 2,
                'name': 'Switch to account:',
                'value': 'switch'
            },
            {
                'key': 3,
                'name': 'Go to Main Menu',
                'value': 'main-menu'
            },
            {
                'key': 4,
                'name': 'Exit',
                'value': 'exit'
            }
        ]
    }
]

add_account_username = {
    'type': 'input',
    'name': 'add_acc_username',
    'message': 'Enter username:'
}

add_account_email = {
    'type': 'input',
    'name': 'add_acc_email',
    'message': 'Enter email:'
}

add_account_hostname = {
    'type': 'input',
    'name': 'add_acc_hostname',
    'message': 'Enter hostname:'
}


def read_config_file():
    if os.path.exists(SSH_CONFIG_PATH):
        with open(SSH_CONFIG_PATH, 'r') as infile:
            return json.load(infile)
    return {}


def write_config_to_file(config_obj):
    with open(SSH_CONFIG_PATH, 'w') as outfile:
        json.dump(config_obj, outfile, indent=2)
    return


def init_git():
    selected = prompt(questions, style=style)
    if selected['git-config'] == "add":
        inp_username = prompt(add_account_username, style=style)
        inp_email = prompt(add_account_email, style=style)
        inp_hostname = prompt(add_account_hostname, style=style)
        add_account(inp_email['add_acc_email'], inp_username['add_acc_username'], inp_hostname['add_acc_hostname'])
    elif selected['git-config'] == "remove":
        remove_account()
    elif selected['git-config'] == "switch":
        switch_account()
    elif selected['git-config'] == 'main-menu':
        cli.main()
        # print('x')
    elif selected['git-config'] == 'exit':
        logger.info("Exiting...")
        sys.exit(0)


def add_account(email, username, hostname):
    config_obj = read_config_file()

    config_obj[hostname] = {
        "hostName": hostname,
        "name": username,
        "email": email
    }
    write_config_to_file(config_obj)


def remove_account():
    config_obj = read_config_file()

    if len(config_obj) == 0:
        logger.info("No config found.")
    else:
        host_ques = [
            {
                'type': 'list',
                'name': 'git-hosts',
                'message': 'Select host to remove:',
                'choices': config_obj.keys()
            }
        ]
        selected_host = prompt(host_ques, style=style)

        del config_obj[selected_host['git-hosts']]
        write_config_to_file(config_obj)


def switch_account():
    config_obj = read_config_file()

    if len(config_obj) == 0:
        logger.info("No config found.")
    else:
        host_ques = [
            {
                'type': 'list',
                'name': 'git-hosts',
                'message': 'Select host to switch to:',
                'choices': config_obj.keys()
            }
        ]
        selected_host = prompt(host_ques, style=style)
        script_path = get_script_path(dir_path, "switch-acc.sh")
        print(script_path)
        subprocess.run(['bash', script_path, selected_host['git-hosts']])
