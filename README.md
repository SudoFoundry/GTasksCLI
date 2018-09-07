# GTasksCLI
A Google Tasks API command line interface tool. Tool written poorly by @jameshi16.

This tool interfaces with the Google Tasks API using a client ID. The bash script can be entirely converted to a Python script, however, @jameshi16 decided to use Bash instead because he wanted to learn scripting for Ubuntu. Cross-platform compatibility? What's that?

## Pre-requisites
- This repository
- Python 3.6.5
- curl 7.58.0
- getopt from util-linux 2.31.1
- date from GNU coreutils 8.28
- sed (GNU sed) 4.4

This tool is built with the above pre-requisite, and it is in no way fully definitive.

You will also need to acquire a Client ID and Client Secret from your nearest [Google API Console](https://console.cloud.google.com/apis/credentials), because you would need it to initialize the tool.

## Usage
### First time
1) Log onto the [Google API Console](https://console.cloud.google.com/apis/).
2) Create a new project. The name does not matter.
3) Click on 'Credentials' on the sidebar.
4) Select 'OAuth consent screen', and set up the required fields. These contents on these fields do not matter.
5) Select 'Credentials', and click on 'Create credentials', selecting 'OAuth client ID' in the dropdown list.
6) Under 'Application type', select 'Web application'. Some form fields should pop out.
7) Fill in whatever for the 'Name' field.
8) Fill in 'http://127.0.0.1' for the 'Authorized redirect URIs'.
9) Click 'Create'.
10) Take note of the client ID and client secret generated.
11) Run `./gtaskscli -h` found in this folder
12) When prompted for the client ID and secret, paste them into the script. (Note: Pasting them will sometimes cause the terminal to automatically skip the next prompt. Please perform `rm ~/.gtaskscli` before trying again. We recommend you to copy the client ID and secret to another location, before copy+pasting it into the script.)
13) You will be prompted to open your browser for authentication. If you choose not to, a link will be provided for you to perform authentication.
14) After authentication, you can close the window when prompted. Back at the terminal, you should notice that the help page should have printed. From here on out, you will not be prompted for your information again until you revoke access to this app through your Google Account. In that case, please perform `rm ~/.gtaskscli` to restart the registration process

### After first time
Please perform `~/.gtaskscli -h` to view the help, or, alternatively, refer to `cmdHelp.txt` in the same repository.

## Tested Operating Systems
- Ubuntu 18.04

## License
Licensed under [MIT License](https://github.com/TeamSudoCoders/GTasksCLI/LICENSE.md).
