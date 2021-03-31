from PyInquirer import style_from_dict, Token, prompt, Separator
import apt

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def check_package_existence(pkg_name):
  try:
    cache = apt.Cache()
    if cache[pkg_name].is_installed:
      return True
    else:
      return False
  except Exception as e:
    return False