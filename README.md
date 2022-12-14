<p align="center">
  <img src="./resources/extras/logo.readmeALPHA.jpg" alt="Alpha Logo">
</p>
<h1 align="center">
  <b>ALPHA - UserBot</b>
</h1>

<b>A stable pluggable Telegram userbot based on Telethon.</b>

[![](https://img.shields.io/badge/ALPHA-v0.1-blue)](#)
[![Stars](https://img.shields.io/github/stars/Light-Sensei/AlphaUB?style=flat-square&color=yellow)](https://github.com/Light-Sensei/AlphaUB/stargazers)
[![Forks](https://img.shields.io/github/forks/Light-Sensei/AlphaUB?style=flat-square&color=orange)](https://github.com/Light-Sensei/AlphaUB/fork)
[![Size](https://img.shields.io/github/repo-size/Light-Sensei/AlphaUB?style=flat-square&color=green)](https://github.com/Light-Sensei/AlphaUB/)   
[![Python](https://img.shields.io/badge/Python-v3.10.3-blue)](https://www.python.org/)
[![CodeFactor](https://www.codefactor.io/repository/github/Light-Sensei/AlphaUB/badge/main)](https://www.codefactor.io/repository/github/Light-Sensei/AlphaUB/overview/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Light-Sensei/AlphaUB/graphs/commit-activity)
[![Docker Pulls](https://img.shields.io/docker/pulls/theLight-Sensei/AlphaUB?style=flat-square)](https://img.shields.io/docker/pulls/theLight-Sensei/AlphaUB?style=flat-square)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/Light-Sensei/AlphaUB)
[![Contributors](https://img.shields.io/github/contributors/Light-Sensei/AlphaUB?style=flat-square&color=green)](https://github.com/Light-Sensei/AlphaUB/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/Light-Sensei/AlphaUB/blob/main/LICENSE)   
[![Sparkline](https://stars.medv.io/Light-Sensei/AlphaUB.svg)](https://stars.medv.io/Light-Sensei/AlphaUB)
----

# Deploy
- [Heroku](#deploy-to-heroku)
- [Okteto](#deploy-to-okteto)
- [Local Machine](#deploy-locally)

# Documentation 
[![Documentation](https://img.shields.io/badge/Documentation-ALPHA-blue)](http://ALPHA.tech/)

# Tutorial 

- Tutorial to get Redis URL and password - [here.](./resources/extras/redistut.md)
---

## Deploy to Heroku
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://deploy.Light-Sensei/AlphaUB.tech)

## Deploy to Okteto
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/Light-Sensei/AlphaUB)

## Deploy Locally
- [Traditional Method](#local-deploy---traditional-method)
- [Easy Method](#local-deploy---easy-method)
- [ALPHA CLI](#ALPHA-cli)

### Local Deploy - Easy Method
- Linux - `wget -O locals.py https://git.io/JY9UM && python3 locals.py`
- Windows - `cd desktop ; wget https://git.io/JY9UM -o locals.py ; python locals.py`
- Termux - `wget -O install-termux https://tiny.ALPHA.tech/termux && bash install-termux`

### Local Deploy - Traditional Method
- Get your [Necessary Variables](#Necessary-Variables)
- Clone the repository:    
`git clone https://github.com/Light-Sensei/AlphaUB.git`
- Go to the cloned folder:    
`cd ALPHA`
- Create a virtual env:      
`virtualenv -p /usr/bin/python3 venv`
`. ./venv/bin/activate`
- Install the requirements:      
`pip(3) install -U -r re*/st*/optional-requirements.txt`
`pip(3) install -U -r requirements.txt`
- Generate your `SESSION`:
  - For Linux users:
    `bash sessiongen`
     or
    `wget -O session.py https://git.io/JY9JI && python3 session.py`
  - For Termux users:
    `wget -O session.py https://git.io/JY9JI && python session.py`
  - For Windows Users:
    `cd desktop ; wget https://git.io/JY9JI -o ALPHA.py ; python ALPHA.py`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/Light-Sensei/AlphaUB/blob/main/.env.sample).
(You can either edit and rename the file or make a new file named `.env`.)
- Run the bot:
  - Linux Users:
   `bash startup`
  - Windows Users:
    `python(3) -m AlphaOP`
<details>
<summary><h3>[OUTDATED] ALPHA CLI</h3></summary>

[ALPHA CLI](https://github.com/BLUE-DEVIL1134/ALPHACli) is a command-line interface for deploying ALPHA.   

- **Installing** -    
Run the following code on a terminal, with curl installed.   
`ver=$(curl https://raw.githubusercontent.com/BLUE-DEVIL1134/ALPHACli/main/version.txt) && curl -L -o ALPHA https://github.com/BLUE-DEVIL1134/ALPHACli/releases/download/$ver/ALPHA.exe`
OR
Go to [ALPHACli](https://github.com/BLUE-DEVIL1134/ALPHACli) and install the version release from the Github Releases. Add the executable to your system path as specified in the [Readme](https://github.com/BLUE-DEVIL1134/ALPHACli#how-to-use-ALPHAcli-).   

- **Documentation** -
Take a look at the [`docs`](https://blue-devil1134.github.io/ALPHACli/) for more detailed information.
</details>

---
## Necessary Variables
- `SESSION` - SessionString for your accounts login session. Get it from [here](#Session-String)

One of the following database:
- For **Redis** (tutorial [here](./resources/extras/redistut.md))
  - `REDIS_URI` - Redis endpoint URL, from [redislabs](http://redislabs.com/).
  - `REDIS_PASSWORD` - Redis endpoint Password, from [redislabs](http://redislabs.com/).
- For **MONGODB**
  - `MONGO_URI` - Get it from [mongodb](https://mongodb.com/atlas).
- For **SQLDB**
  - `DATABASE_URL`- Get it from [elephantsql](https://elephantsql.com).

## Session String
Different ways to get your `SESSION`:
* [![Run on Repl.it](https://replit.com/badge/github/Light-Sensei/AlphaUB)](https://replit.com/@Light-Sensei/AlphaUBStringSession)
* Linux : `wget -O session.py https://git.io/JY9JI && python3 session.py`
* PowerShell : `cd desktop ; wget https://git.io/JY9JI ; python ALPHA.py`
* Termux : `wget -O session.py https://git.io/JY9JI && python session.py`
* TelegramBot : [@SessionGeneratorBot](https://t.me/SessionGeneratorBot)

---

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
ALPHA is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

---

# Credits
* [Light](https://github/Light-Sensei)
* [Yui](https://github/yuisakura)

> Made with ???? by [Quinx Network](https://t.me/Quinx_Network).    
