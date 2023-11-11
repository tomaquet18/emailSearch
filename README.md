## Usage
### Help

```
$ python3 main.py --help
___________                 .__ .__     _________                               .__     
\_   _____/  _____  _____   |__||  |   /   _____/  ____  _____  _______   ____  |  |__  
 |    __)_  /     \ \__  \  |  ||  |   \_____  \ _/ __ \ \__  \ \_  __ \_/ ___\ |  |  \ 
 |        \|  Y Y  \ / __ \_|  ||  |__ /        \\  ___/  / __ \_|  | \/\  \___ |   Y  \
/_______  /|__|_|  /(____  /|__||____//_______  / \___  >(____  /|__|    \___  >|___|  /
        \/       \/      \/                   \/      \/      \/             \/      \/ 
                                                                     by: tomaquet18
usage: main.py [-h] [-n NAME] [-l LASTNAME] [-d DOMAIN]

Mail permutation

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name
  -l LASTNAME, --lastname LASTNAME
                        Lastname
  -d DOMAIN, --domain DOMAIN
                        Domain
```

### Examples
Command:
```
$ python3 main.py -n john -l doe -d "example.com"
```

Result:
```
___________                 .__ .__     _________                               .__     
\_   _____/  _____  _____   |__||  |   /   _____/  ____  _____  _______   ____  |  |__  
 |    __)_  /     \ \__  \  |  ||  |   \_____  \ _/ __ \ \__  \ \_  __ \_/ ___\ |  |  \ 
 |        \|  Y Y  \ / __ \_|  ||  |__ /        \\  ___/  / __ \_|  | \/\  \___ |   Y  \
/_______  /|__|_|  /(____  /|__||____//_______  / \___  >(____  /|__|    \___  >|___|  /
        \/       \/      \/                   \/      \/      \/             \/      \/ 
                                                                     by: tomaquet18
2 emails found in Google:
someone@example.com
AnaLopez@example.com

No separators detected in email

Generated emails using default list of separators:
john.doe@example.com
j.doe@example.com
doe.john@example.com
john-doe@example.com
j-doe@example.com
doe-john@example.com
johndoe@example.com
jdoe@example.com
doejohn@example.com
```