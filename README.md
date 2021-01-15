# See-Al-I
An all round cli to make life easier

### Available features:
- setup: 
  - ```setup``` : This should be run initially to install necessary dependecies for see-al-i to work flawlessly.
  
- zsh specific commands:
  - ```zsh install``` : Install zsh and oh-my-zsh and set as default shell.
  - ```zsh ls-themes``` : List all available zsh themes.
  - ```zsh set-theme <theme-name>``` : Set a theme from the list of available zsh themes.

- git configs: In case you have multiple accounts on your device, switching configs can be made easier using this options.
  - ```git ls``` : List all available git configs.
  - ```git use <config-name>``` : Set the user name and email from the config to be used actively.
  NOTE: this feature requires the use of a file called ssh-config.json, it should have the hostname email and username of each config. Sample template available under ```templates/ssh-config.json```


### To use see-al-i, follow the steps: 
- clone this repository.
- cd into the ```see-al-i``` directory and run ```./see-al-i <arg1> <arg2>```.
- for help, run ```./see-al-i``` without any arguments.


#### Supported OS: 
- Ubuntu