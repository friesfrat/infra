#!/usr/bin/python

import argparse
import subprocess
import csv
import datetime
import time


from pymongo import MongoClient
from decimal import Decimal



parser = argparse.ArgumentParser()

## define arguments
parser.add_argument('--create', help='Create DB Structure', action='store_true')
parser.add_argument('--delete', help='Delete DB Structure', action='store_true')
parser.add_argument('--insert-data', help='Insert mockup data', action='store_true')

args = parser.parse_args()


def create_structure():
    ## it is assumed that mongo runs locally or in a container, also locally;
    p = subprocess.Popen('mongo --host="127.0.0.1:27017" < mongo-scripts/prep-db-struct.js',
                         shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    for line in p.stdout.readlines():
        print line,
    p.wait() ## wait until process is finished


def delete_structure():
    ## it is assumed that mongo runs locally or in a container, also locally;
    p = subprocess.Popen('mongo --host="127.0.0.1:27017" < mongo-scripts/delete-db-struct.js',
                         shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    for line in p.stdout.readlines():
        print line,
    p.wait() ## wait until process is finished


def insert_data():
    ## it is assumed that mongo runs locally or in a container, also locally;

    client = MongoClient('mongodb://localhost:27017/')


    with open('data/permissions_list.txt', mode='r') as csv_file:
        permissions = client.securitydb.permissions
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            permission = {
                "_id": row["id"],
                "permission": row["permission"]
            }
            print "insert permission: {}".format(permission)
            result = permissions.insert_one(permission)
            print "permissionid: {}\n".format(result.inserted_id)


    with open('data/roles_list.txt', mode='r') as csv_file:
        roles = client.securitydb.roles
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            role = {
                "_id": row["id"],
                "role": row["role"],
                "permissions": list(row["permissions"])
            }
            print "insert role: {}".format(role)
            result = roles.insert_one(role)
            print "operationid: {}\n".format(result.inserted_id)


    with open('data/users_list.txt', mode='r') as csv_file:
        users = client.securitydb.users
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            user = {
                "_id": row["id"],
                "firstname": row["firstname"],
                "lastname": row["lastname"],
                "email": row["email"],
                "password": row["password"],
                "phonenumber": row["phonenumber"],
                "registerdate": datetime.datetime.utcnow(),
                "role": row["role"]
            }
            print "insert user: {}".format(user)
            result = users.insert_one(user)
            print "userid: {}\n".format(result.inserted_id)

    client.close()


def parse_arguments():
    if (args.delete):
        print "Delete DB Structure"
        delete_structure()

    if (args.create):
        print "Create DB Structure"
        create_structure()

    if (args.insert_data):
        print "Insert mockup data"
        insert_data()


if __name__ == "__main__":
    parse_arguments()
