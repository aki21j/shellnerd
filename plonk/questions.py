from copy import deepcopy
from PyInquirer import prompt, Separator

QUESTIONS = {
  "cli": {
    "main": [
      {
          'type': 'list',
          'name': 'init_choice',
          'message': 'What do you want to do?',
          'choices': [
              {
                  'key': 0,
                  'name': 'ZSH Management',
                  'value': 'zsh-mgmt'
              },
              {
                  'key': 1,
                  'name': 'GIT Config Management',
                  'value': 'git-mgmt'
              },
              {
                  'key': 2,
                  'name': 'SSH Config Management',
                  'value': 'ssh-mgmt'
              },
              Separator(),
              {
                  'key': 3,
                  'name': 'Exit',
                  'value': 'exit'
              }
          ]
        }
    ]
  },
  "zsh": {
    "init": [
        {
            'type': 'list',
            'name': 'zsh',
            'message': 'What do you want?',
            'choices': [
                {
                    'key': 0,
                    'name': 'Install ZSH',
                    'value': 'install'
                },
                {
                    'key': 1,
                    'name': 'List available themes',
                    'value': 'ls-themes'
                },
                {
                    'key': 2,
                    'name': 'Set theme',
                    'value': 'set-theme'
                },
                Separator(),
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
      ],
    "set_theme": {
          'type': 'input',
          'name': 'set_theme_name',
          'message': 'Enter name of the theme to be set:'
      }
    },
  "git": {
    "init": [
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
                Separator(),
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
    ],
    "add_account_username": {
      'type': 'input',
      'name': 'add_acc_username',
      'message': 'Enter username:'
    },
    "add_account_email": {
        'type': 'input',
        'name': 'add_acc_email',
        'message': 'Enter email:'
    },
    "add_account_hostname": {
        'type': 'input',
        'name': 'add_acc_hostname',
        'message': 'Enter hostname:'
    }
  },
  "ssh": {
    "init": [
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
              Separator(),
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
    ],
    "add_server_username": {
        'type': 'input',
        'name': 'add_server_username',
        'message': 'Enter Username:'
    },
    "add_server_host": {
        'type': 'input',
        'name': 'add_server_host',
        'message': 'Enter host address:'
    },
    "add_server_alias": {
        'type': 'input',
        'name': 'add_server_alias',
        'message': 'Enter Alias Name:'
    },
    "path_to_id_rsa" :{
        'type': 'input',
        'name': 'id_rsa_path',
        'message': 'Enter Path to identity file aka id_rsa. This is optional if already configured globally.'
    }
  },
  "exit": [
    {
        'type': 'confirm',
        'message': 'Do you want to exit?',
        'name': 'exit',
        'default': False,
    }
  ],
  "confirm_remove": [
    {
        'type': 'confirm',
        'message': 'Are you sure you want to remove it?',
        'name': 'remove_confirmation',
        'default': False,
    }
  ],
  "default_exits": [
      Separator(),
      'Go to Main Menu',
      'Exit'
  ]
}

def retrieve_questions(*keys):
    out = deepcopy(QUESTIONS)
    for key in keys:
        try:
            out = out[key]
        except KeyError:
            return None
    return out
