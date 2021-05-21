import json
import os
import subprocess
import sys

from shellnerd import cli
from PyInquirer import prompt
from shellnerd.utils.logger import logger
from shellnerd.utils.utils import style, get_script_path, default_menu_or_exit
from shellnerd.questions import retrieve_questions

home = os.environ['HOME']
SSH_PATH = os.path.join(home, '.ssh')
SSH_CONFIG_PATH = os.path.join(SSH_PATH, "ssh-config.json")

dir_path = os.path.dirname(os.path.realpath(__file__))

def read_config_file():
    if os.path.exists(SSH_CONFIG_PATH):
        with open(SSH_CONFIG_PATH, 'r') as infile:
            return json.load(infile)
    return {}


def write_config_to_file(config_obj):
    if not os.path.exists(SSH_PATH):
        os.makedirs(SSH_PATH)
    with open(SSH_CONFIG_PATH, 'w') as outfile:
        json.dump(config_obj, outfile, indent=2)    
    return


def init():
    selected = prompt(retrieve_questions('git', 'init'), style=style)
    if selected['git-config'] == "add":
        inp_username = prompt(retrieve_questions('git', 'add_account_username'), style=style)
        inp_email = prompt(retrieve_questions('git', 'add_account_email'), style=style)
        inp_hostname = prompt(retrieve_questions('git', 'add_account_hostname'), style=style)
        add_account(inp_email['add_acc_email'], inp_username['add_acc_username'], inp_hostname['add_acc_hostname'])
    elif selected['git-config'] == "remove":
        remove_account()
    elif selected['git-config'] == "switch":
        switch_account()
    else:
        default_menu_or_exit(selected['git-config'])
    init()


def add_account(email, username, hostname):
    config_obj = read_config_file()

    config_obj[hostname] = {
        "hostName": hostname,
        "name": username,
        "email": email
    }
    write_config_to_file(config_obj)
    logger.info("Finished adding account.")


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
                'choices': list(config_obj.keys()) + retrieve_questions('default_exits')
            }
        ]
        selected_host = prompt(host_ques, style=style)
        default_menu_or_exit(selected_host['git-hosts'])

        confirm_removal = prompt(retrieve_questions('confirm_remove'), style=style)
        if confirm_removal['remove_confirmation']:
            del config_obj[selected_host['git-hosts']]
            write_config_to_file(config_obj)
            logger.info("Account removal successful.")
        else:
          init()

        


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
                'choices': list(config_obj.keys()) + retrieve_questions('default_exits')
            }
        ]
        selected_host = prompt(host_ques, style=style)

        default_menu_or_exit(selected_host['git-hosts'])

        script_path = get_script_path(dir_path, "switch-acc.sh")
        username = config_obj[selected_host['git-hosts']]['name']
        email = config_obj[selected_host['git-hosts']]['email']
        subprocess.run(['bash', script_path, username, email])
