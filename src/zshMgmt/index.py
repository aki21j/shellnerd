from PyInquirer import style_from_dict, Token, prompt, Separator
from utils import style, check_package_existence
from pprint import pprint

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
    install()
  elif selected['zsh'] == "ls-themes":
    print('list-themes')
  elif selected['zsh'] == "set-theme":
    print('set-theme')


def install():
  is_installed = check_package_existence("zsh")
  if is_installed:
    print("zsh is already set as your default shell.")
  else:
    print("Installing zsh...")
