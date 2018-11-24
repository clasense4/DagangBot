# Simple Telegram Bot

## Introduction

Simple telegram bot using orator as database manager. This bot will simulate how ecommerce works by using telegram bot.


## Requirements

- Python 3.6
- Python pip
- Python Virtualenv
- Mysql
- [Linux Server](https://www.digitalocean.com/?refcode=6b1c3b315e1e)

## Installation

```
virtualenv -p `which python3` env
source env/bin/activate
pip3 install -r requirements.txt
```

## Configuration

1. Edit `orator.yml` as needed
2. Copy `telegram.yml.example` to `telegram.yml` and add your bot token

## Run

`python bot.py`