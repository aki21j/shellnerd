import json
import os
import subprocess
import sys

from plonk import cli
from PyInquirer import prompt
from plonk.utils.logger import logger
from plonk.utils.utils import style, get_script_path

home = os.environ['HOME']
SSH_PATH = os.path.join(home, '.ssh')
SSH_CONFIG_PATH = os.path.join(SSH_PATH, "config")
ALL_CONFIG_PATH = os.path.join(SSH_PATH, "all_config.json")

dir_path = os.path.dirname(os.path.realpath(__file__))

questions = [
    {
        'type': 'list',
        'name': 'ssh-config',
        'message': 'What do you want?',
        'choices': [
            {
                'key': 0,
                'name': 'Add/update server alias',
                'value': 'add'
            },
            {
                'key': 1,
                'name': 'Remove server alias',
                'value': 'remove'
            },
            {
                'key': 2,
                'name': 'Connect to server',
                'value': 'connect-to'
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

add_server_username = {
    'type': 'input',
    'name': 'add_server_username',
    'message': 'Enter Username:'
}

add_server_host = {
    'type': 'input',
    'name': 'add_server_host',
    'message': 'Enter host address:'
}

add_server_alias = {
    'type': 'input',
    'name': 'add_server_alias',
    'message': 'Enter Alias Name:'
}

path_to_id_rsa = {
    'type': 'input',
    'name': 'id_rsa_path',
    'message': 'Enter Path to identity file aka id_rsa. This is optional if already configured globally.'
}

def init():
    selected = prompt(questions, style=style)
    if selected['ssh-config'] == "add":
        inp_username = prompt(add_server_username, style=style)
        inp_host = prompt(add_server_host, style=style)
        inp_alias = prompt(add_server_alias, style=style)
        inp_id_rsa = prompt(path_to_id_rsa, style=style)
        add_account(inp_host['add_server_host'], inp_username['add_server_username'], inp_alias['add_server_alias'], inp_id_rsa['id_rsa_path'])
    elif selected['ssh-config'] == "remove":
        remove_account()
    elif selected['ssh-config'] == "connect-to":
        connect_to_server()
    elif selected['ssh-config'] == 'main-menu':
        cli.main()
    elif selected['ssh-config'] == 'exit':
        logger.info("Exiting...")
        sys.exit(0)

def read_config_file():
    if os.path.exists(ALL_CONFIG_PATH):
        with open(ALL_CONFIG_PATH, 'r') as infile:
            return json.load(infile)
    return {}


def write_config_to_file(config_obj):
    if not os.path.exists(SSH_PATH):
        os.makedirs(SSH_PATH)
    with open(ALL_CONFIG_PATH, 'w') as outfile:
        json.dump(config_obj, outfile, indent=2)
    cmd = ['scj', 'restore', ALL_CONFIG_PATH]
    subprocess.call(cmd)
    return


def get_config():
  if os.path.exists(SSH_CONFIG_PATH):
    cmd = ['scj', 'dump', ALL_CONFIG_PATH]
    subprocess.call(cmd)
    return True
  return False
  

def add_account(host_address, username, host_alias, identity_file_path):
    has_config = get_config()
    if not has_config:
      logger.error("No Config Found. New config will be created.")
    config_obj = read_config_file()

    available_servers = []
    is_duplicate = False
    for i in range(0,len(config_obj)):
        if 'Host' in config_obj[i] and host_alias == config_obj[i]['Host']:
          is_duplicate = True
        if 'HostName' in config_obj[i] and host_address == config_obj[i]['HostName']:
          is_duplicate = True

    # {
    #     "Host": "prod-nginx-server",
    #     "HostName": "13.229.114.12",
    #     "User": "ubuntu"
    #     "IdentityFile": "~/.ssh/id_rsa_personal"
    # },

    if is_duplicate:
      logger.error("Duplicate Entry. Please try again:")
      init()
    else:
      new_conf = {
          "Host": host_alias,
          "User": username,
          "HostName": host_address
      }
      if identity_file_path is not None or identity_file_path != "":
        new_conf["IdentityFile"] = identity_file_path

      config_obj.append(new_conf)
      write_config_to_file(config_obj)
      logger.info("Finsihed adding server to config. You can now connect to the recently added server.")


def remove_account():
    config_obj = read_config_file()

    if len(config_obj) == 0:
        logger.info("No config found.")
    else:
        available_servers = []
        for i in range(0,len(config_obj)):
            if 'Host' in config_obj[i]:
              available_servers.append({
                  'key': i,
                  'name': config_obj[i]['Host'],
                  'value': i,
                })
        host_ques = [
            {
                'type': 'list',
                'name': 'ssh-hosts',
                'message': 'Select host to remove:',
                'choices': available_servers
            }
        ]
        selected_host = prompt(host_ques, style=style)

        config_obj.pop(selected_host['ssh-hosts'])
        write_config_to_file(config_obj)
        logger.info("Finished removing config.")


def connect_to_server():
    has_config = get_config()
    if not has_config:
      logger.error("No Config Found.")
    else:
      config_obj = read_config_file()

      if len(config_obj) == 0:
          logger.info("No config found.")
      else:
          available_servers = []
          for conf in config_obj:
            if 'Host' in conf:
              available_servers.append(conf['Host'])
          host_ques = [
              {
                  'type': 'list',
                  'name': 'ssh-hosts',
                  'message': 'Select server to connect to:',
                  'choices': available_servers
              }
          ]
          selected_host = prompt(host_ques, style=style)
          cmd = ['ssh', selected_host['ssh-hosts']]
          print(cmd)
          subprocess.call(cmd)
