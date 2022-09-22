#!/usr/bin/env python3
from artifactory import ArtifactoryPath
from requests.auth import HTTPBasicAuth
from posixpath import join as urljoin
import argparse
import os.path
import sys
import requests

url = "http://34.125.149.8:8082/artifactory/"
def remove_old_files(URL, REPONAME, auth, MINVERSION, MAXVERSION):
    path = ArtifactoryPath(URL, auth=auth, auth_type=HTTPBasicAuth, )
    MINVERSION,MAXVERSION = int(MINVERSION), int(MAXVERSION)
    for num in range(MINVERSION, MAXVERSION+1):
        num = str(num)
        VERSION = "*/"+num+".*"
        files = path.aql("items.find", {"repo": REPONAME, "name": {"$match": "*.war"}, "path": {"$match": VERSION}})
        for file in files:
            PATH,NAME = file["path"],file["name"]
            print(PATH, NAME)
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", default='buildguy', help="Artifactory user name for authentication")
    parser.add_argument("--password", "--apikey", dest='password', default="", help="Artifactory password for authentication")
    parser.add_argument("--minversion", default='1', help="Minimum version of Artifacts from which we need to list")
    parser.add_argument("--maxversion", default='4', help="Maximum version of Artifacts upto which we need to list")
    parser.add_argument("--sourcerepo", help="Repo name from where we need to list old artifacts")
    parser.add_argument("--destinationrepo", help="Repo name to where we are copying the old artifacts")
    args = parser.parse_args()
    auth = (args.user, args.password)
    remove_old_files(url, args.sourcerepo, auth, args.minversion, args.maxversion)
