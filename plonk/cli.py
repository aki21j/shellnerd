import sys

from PyInquirer import prompt

from .utils.logger import logger
from .utils.utils import style
from .zsh_mgmt import command as Zsh
from .git_mgmt import command as Git
from .ssh_mgmt import command as Ssh
from .questions import retrieve_questions

def main():
    selected = prompt(retrieve_questions('cli', 'main'), style=style)
    if selected['init_choice'] == "zsh-mgmt":
        # show zsh options
        Zsh.init()
    elif selected['init_choice'] == "git-mgmt":
        # show git options
        Git.init()
    elif selected['init_choice'] == "ssh-mgmt":
        # show git options
        Ssh.init()
    elif selected['init_choice'] == 'exit':
        inp_exit = prompt(retrieve_questions('exit'), style=style)
        if inp_exit['exit']:
          logger.info("Exiting...")
          sys.exit(0)
        else:
          main()
