# Use prep-env utility
**NOTE:** This utility is written to be compatible with python2.
Instructions:
```sh
$ sudo apt-get install python-pip ## install pip package manager for python 2.7.12
$ cd infra/prep-env
$ pip install -r requirements.txt ## install required packages
## make the utility executable
$ chmod +x prep-env.py
```
Example usage:
```sh
NOTE: The arguments are evaluated in the following order: delete, create, insert-data
$ ./prep-env.py --help
usage: prep-env.py [-h] [--create] [--delete] [--insert-data]

optional arguments:
  -h, --help     show this help message and exit
  --create       Create DB Structure
  --delete       Delete DB Structure
  --insert-data  Insert mockup data
```
Delete entire db structure
```sh
$ ./prep-env.py --delete
Delete DB Structure
MongoDB shell version: 2.6.10
connecting to: 127.0.0.1:27017/test
switched to db securitydb
true
true
true
{ "dropped" : "securitydb", "ok" : 1 }
bye
```
Create db structure
```sh
$ ./prep-env.py --create
Create DB Structure
MongoDB shell version: 2.6.10
connecting to: 127.0.0.1:27017/test
switched to db securitydb
{ "ok" : 1 }
{ "ok" : 1 }
{ "ok" : 1 }
bye
```
Insert mockup data
```sh
$ ./prep-env.py --insert-data
Insert mockup data
insert permission: {'_id': '1', 'permission': 'READ'}
permissionid: 1
insert permission: {'_id': '2', 'permission': 'EDIT'}
permissionid: 2
--- truncated output ---
insert role: {'_id': '1', 'role': 'MEMBER', 'permissions': ['1', '2', '3', '4']}
operationid: 1
insert role: {'_id': '2', 'role': 'PRIVILEDGE_MEMBER', 'permissions': ['1', '2', '3', '4', '5']}
operationid: 2
--- truncated output ---
insert user: {'registerdate': datetime.datetime(2018, 11, 14, 23, 37, 57, 800608), 'password': 'jasbed123', 'phonenumber': '7319486251', 'firstname': 'Charels', 'lastname': 'Hernandez', 'role': '1', '_id': '9', 'email': 'chernandez@gmail.com'}
userid: 9
insert user: {'registerdate': datetime.datetime(2018, 11, 14, 23, 37, 57, 801560), 'password': 'ecsady123', 'phonenumber': '5826419735', 'firstname': 'Eric', 'lastname': 'Carson', 'role': '2', '_id': '10', 'email': 'ecarson@gmail.com'}
userid: 10
```
