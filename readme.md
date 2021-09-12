# Technical Screener

A powerful tool for investors to identify new trading opportunities and potentially profitable investments. 

## Contents

1. [Description](#description)
1. [Project structure](#project-structure)
1. [Getting started](#getting-started)
1. [Built with](#built-with)
1. [Acknowledgments](#acknowledgments)

## Description

TODO


## Project structure

```
/
  ├── env                 python virtual environment*
  ├── techscreener/       entry point to django project
      ├── techscreener/   default django app
      ├── main/           django app for main functionalities
      ├── user/           django app for user authentication
      ├── static/         static files used in frontend
      ├── templates/      HTML code for frontend
      ├── manage.py       admin script for the project
  ├── .gitignore          script to ignore files in commits
  ├── readme.md           project readme!
  └── requirements.txt    python packages used
```

## Getting started

### Prerequisites
- Python3, virtualenv, pip
- Postgresql 13
- A web browser

A step by step series of instructions that tell you how to get a development env running.

1. **Postgres DB Setup**: Head to `/techscreener/techscreener/settings.py` line 83 to view configurations needed for postgres
2. **Virtualenv setup**: I had named the virtualenv as 'env' in this project. Run `pip install -r requirements.txt` in the project's root folder to install all required packages. Once installed, run the virtualenv byy typing `source env/bin/activate` from the root directory.
3. cd into `techscreener/` and run:
```bash
    python manage.py makemigrations
```
followed by 
```bash
    python manage.py migrate
```
4. Now to run the application at any time, just use `python manage.py runserver` and the application will be live at [127.0.0.1:8000](http://127.0.0.1:8000)


## Built with

- Backend: Django
- Database: Postgres SQL
- Frontend: HTML, CSS, JS

## Acknowledgments

- Credits to all authors of the various packages used throughout the project.
- BoostrapDash for Kapella Dashboard theme.
