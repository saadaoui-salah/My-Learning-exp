
# All imports 
import sys
import os

# All variables
commands= {}
commands["-p"] =  "C:\\Users\\pc\\Desktop\\est"
commands["-v"] = "venv" 
commands["-d"] =  "project"

Env_Path = "cd "+commands["-p"]+'&'+commands["-v"]+'\\'+'Scripts\\activate'

# All Functions & Classes

class Venv():
    
    def venv(Name=None):
        try:
            NAME = commands["-v"]
            PATH = commands['-p']
            os.system(f"cd {PATH} & python -m venv {NAME}")
            print("[VENV] ==> Vertual Envirment was Created")
        except :
            print('[VENV] ==> Check Your Vertual Envirment')   
    def config():
        if sys.argv[1] == "-v":
            if sys.argv[2:] :
                try:
                    Name = str(sys.argv[2])
                    commands["-v"] = Name
                    print("[VENV CONFIG] ==> Replaced ")
                except:
                    print("[VENV CONFIG] ==> Try a String")
            else:
                print("[VENV CONFIG] ==> Enter a Name")


class Django():
    
    def start_project(Name=None, Apps=None):
        NAME = commands["-d"]    
        if NAME: 
            if Apps:
                APPs = Apps.split(" ")
                if len(APPs) > 1:
                    for i in len(APPs): 
                        os.system(f"{Env_Path} & pip install django &django-admin startproject  {NAME} . | manage.py start app {Apps[i]}")
                os.system(f"{Env_Path} & pip install django &django-admin startproject  {NAME} . | manage.py start app {Apps}")
            
            os.system(f"{Env_Path} & pip install django &django-admin startproject {NAME} .")

    def create_super_user(user=None, paswwd=None ,email=None):
        os.system(f"{Env_Path}| manage.py createsuperuser |root|root|root|root")
        print("[DJANGO]... \n username => root \n passowrd => root")
    
    def makemigartions_nd_migrate():
        try:
            os.system(f"{Env_Path}& manage.py makemigrations & manage.py migrate")
        except:
            try:
                os.system(f"{Env_Path}& manage.py makemigrations")
            except :
                print("[DJANGO] makemigrations error")

            try:
                os.system(f"{Env_Path} & manage.py migrate")
            except :
                print("[DJANGO] migrate error")

    def config():
        if sys.argv[1]=="-d":
            if sys.argv[2]:
                if sys.argv[3:]:
                    print("Please Fix Your Commands")
                else:
                    commands["-d"] = sys.argv[2]

# The System

if sys.argv[1]=="-all":
    Venv.venv()
    Django.start_project()
    Django.create_super_user()
    Django.makemigartions_nd_migrate()