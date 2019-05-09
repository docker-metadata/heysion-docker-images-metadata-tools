#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Heysion
@copyright: 2019 By Heysion <heysions@gmail.com>
@license: GPL v3.0
'''
import yaml
import git
import os
import logging
import collections as xdict
from utils.core import Base
from utils.core import Fakee

logging.basicConfig(level = logging.DEBUG,
                    format='%(process)d# %(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(message)s',
                    filename='/tmp/hlibdocker.log',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')

redis_v2_repo_info = {
    "name":"redis",
    "gitrepo":"https://github.com/docker-library/redis.git",
    "commit":"dcc0a2a343ce499b78ca617987e8621e7d31515b"
}
pkg_repo_cache={}
pkgs_core = []
class PkgCore(Base):
    name = Fakee("name")
    gitrepo = Fakee("gitrepo")
    branch = Fakee("branch")
    def __init__(self):
        pass


def Load_metadata(pkgname="redis"):
    with open("data/metadata/{0}".format(pkgname)) as f:
        r = yaml.safe_load(f)
        pkg_repo_cache[r.get('name')] = r
        pkg_core = PkgCore()
        pkg_core.name = r.get("name")
        pkg_core.gitrepo = r.get("gitrepo")
        pkg_core.branch = r.get("branch")
        pkgs_core.append(pkg_core)

def Git_source(pkg,branch="master"):
    work = "cache/{n}".format(n=pkg.name)
    src =  "%s/src"%work
    if not os.path.exists(work):
        os.mkdir(work)
    if not os.path.exists("%s/.git"%src):
        git.Repo.clone_from(pkg.gitrepo,src,branch)
    else:
        repo = git.Repo(src)
        repo.remotes.origin.pull()
        repo.git.checkout(branch)
    
def Run_app():
    Load_metadata("redis")
    print(pkgs_core)
    for pkg in pkgs_core:
        print(pkg.name)
        Git_source(pkg)
        
if __name__ == "__main__":
    Run_app()

