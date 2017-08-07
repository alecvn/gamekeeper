from __future__ import with_statement
import os
from fabric.api import *

# ===== Usage =====                                                                                                                                                                                                

usage = """                                                                                                                                                                                                        
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
--------                                                                                                                                                                                                           
staging       : > fab host_impd deploy:<branch>                                                                                                                                                                    
gamekeeper test   : > fab host_gamekeeper_test deploy:<branch>                                                                                                                                                             
gamekeeper prod   : > fab host_gamekeeper_prod deploy:<branch>                                                                                                                                                             
                                                                                                                                                                                                                   
"""

def help():
    print usage

# ===== hosts ======                                                                                                                                                                                               

def host_impd():
    env.user = 'impd'
    env.hosts = ['gamekeeper.impd.co.za']
    env.code_dir = '/home/gamekeeper'

# ===== top level commands ======                                                                                                                                                                                  

def deploy(branch_name="master"):
    print("   Deploying: ** %s **" % branch_name)
    with cd(env.code_dir):
        run("git reset --hard HEAD")
        run("git fetch origin")
        run("git checkout origin/%s" % branch_name)
        run("git pull origin %s" % branch_name)
        run("./scripts/deploy_server.sh")

    print("Deployed to: %s" % env.hosts[0])
