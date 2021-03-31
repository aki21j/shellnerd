import apt
import sys
import os

from logger import logger

from PyInquirer import style_from_dict, Token, prompt, Separator
from elevate import elevate


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

def check_package_existence(pkg_name):
  try:
    cache = apt.Cache()
    if cache[pkg_name].is_installed:
      return True
    else:
      return False
  except Exception as e:
    logger.error(e)
    return False
    

def install_package(pkg_name):
  cache = apt.cache.Cache()
  cache.update()
  cache.open()

  pkg = cache[pkg_name]
  if pkg.is_installed:
      logger.info("{pkg_name} already installed".format(pkg_name=pkg_name))
  else:
      print("before ", is_root())

      if not is_root():
        elevate()

      pkg.mark_install()

      try:
          cache.commit()
      except Exception as e:
        logger.error(sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(e)))
