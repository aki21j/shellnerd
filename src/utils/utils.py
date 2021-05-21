import os
import sys

# import apt
from PyInquirer import prompt ,style_from_dict, Token
from elevate import elevate

from .logger import logger
from src import cli
from src.questions import retrieve_questions

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def is_root():
    return os.getuid() == 0

def get_script_path(dir_path,script_name):
  script_path = os.path.join(dir_path, "commands/%s" % script_name)
  return script_path

def default_menu_or_exit(selection):
  if selection == "Go to Main Menu" or selection == "main-menu":
    cli.main()
  elif selection == "Exit" or selection == "exit":
    # inp_exit = prompt(retrieve_questions('exit'), style=style)
    # if inp_exit['exit']:
    logger.info("Exiting...")
    sys.exit(0)
  else:
    return

# def check_package_existence(pkg_name):
#     try:
#         cache = apt.Cache()
#         if cache[pkg_name].is_installed:
#             return True
#         else:
#             return False
#     except Exception as e:
#         logger.error(e)
#         return False


# def install_package(pkg_name):
#     cache = apt.cache.Cache()
#     cache.update()
#     cache.open()

#     pkg = cache[pkg_name]
#     if pkg.is_installed:
#         logger.info("{pkg_name} already installed".format(pkg_name=pkg_name))
#     else:
#         print("before ", is_root())

#         if not is_root():
#             elevate()

#         pkg.mark_install()

#         try:
#             cache.commit()
#         except Exception as e:
#             logger.error(sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(e)))
