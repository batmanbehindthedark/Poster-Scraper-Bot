from dotenv import load_dotenv
from os import environ, path as ospath
from subprocess import run as r
load_dotenv("config.env", override=True)
repo = environ.get("UPSTREAM_REPO")
branch = environ.get("UPSTREAM_BRANCH", "main")
if not repo:
    exit(1)
if ospath.exists("echo-bot"):
    r("rm -rf echo-bot", shell=True)
cmd = f"git clone -b {branch} {repo} echo-bot"
res = r(cmd, shell=True)
if res.returncode != 0:
    exit(1)
