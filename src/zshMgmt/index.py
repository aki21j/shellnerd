import subprocess
from PyInquirer import style_from_dict, Token, prompt, Separator
from utils import style, check_package_existence, install_package
from pprint import pprint
from logger import logger



questions = [
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
            }
        ]
    }
]

def init_zsh():
  selected = prompt(questions, style=style)
  if selected['zsh'] == "install":
    subprocess.run(['bash', 'shell-commands/zsh/install-zsh.sh'])
  elif selected['zsh'] == "ls-themes":
    subprocess.run(['bash', 'shell-commands/zsh/ls-themes.sh'])
  elif selected['zsh'] == "set-theme":
    subprocess.run(['bash', 'shell-commands/zsh/set-theme.sh', 'custombira'])
