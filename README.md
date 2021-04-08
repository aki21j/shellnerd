# PLONK-CLI
PLONK: ```to set down heavily or carelessly.```

Plonk cli was created out of necessity to cater to smaller things that can become a hassle to manage via the traditional terminal ways.
To start just type ```plonk``` after installation.

### Requirements:
- python 3.5 or higher
- pip to install the package


### Available features:
- zsh management:  
  - ```install``` : Command to Install zsh, oh-my-zsh and to set it as your default shell.
  - ```list available themes``` : List all available zsh themes.
  - ```set theme``` : Set a theme from the list of available zsh themes.

- git config management: In case you have multiple accounts on your device, switching configs can be made easier using this option.
  - ```add account``` : Add a user account to the list of available configs.
  - ```remove account``` : Remove selected user account from the list of available git configs.
  - ```switch to account``` : Set the user name and email from the config to be used actively.
  NOTE: this feature requires the use of a file called ssh-config.json, it should have the hostname email and username of each config. Sample template available under ```templates/ssh-config.json```

- ssh config management: Options related to ssh keys and available servers. 
  - ```add/update server alias``` : Add or updated the alias which can be used to connect to a remote server.
  - ```remove account``` : Remove selected server alias.
  - ```connect to server``` : Connect to a server via ssh from the list of available servers.

### Plonk can be installed in two ways:
- As a pip package from PyPi ```[Coming Soon] ```
- Build from source: To build from source do the following
  - clone this repository.
  - cd into the ```plonk-cli``` directory and run 
    - ```python setup.py sdist bdist_wheel```
    - ```pip install dist/plonk*.whl```

#### Supported OS: 
- Ubuntu
