<h1 align="center">
    EENOVATORS BILLING DASHBOARD
</h1>

<h3 align=center style="font-weight: 1000;">
    Empowering accurate energy insights, usage tracking, and cost computation
</h3>


![Last Commit](https://img.shields.io/github/last-commit/KiseraTimon/eenovators)
![Jinja](https://img.shields.io/badge/jinja-Templates-yellowgreen)
![Languages](https://img.shields.io/github/languages/count/KiseraTimon/eenovators)

---

<h3 align=center style="font-weight: 1000">
🚀 Built with the tools and technologies
</h3>

<h1 align=center>

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python)
![Flask](https://img.shields.io/badge/-Flask-black?logo=flask)
![HTML](https://img.shields.io/badge/-HTML5-E34F26?logo=html5)
![CSS](https://img.shields.io/badge/-CSS3-1572B6?logo=css3)
![JavaScript](https://img.shields.io/badge/-JavaScript-yellow?logo=javascript)
![XML](https://img.shields.io/badge/-XML-0060aa?logo=xml)
![Jinja](https://img.shields.io/badge/-Jinja2-brown?logo=jinja)
![MySQL](https://img.shields.io/badge/-MySQL-grey?logo=mysql)
</h1>

---

## 📚 Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Future Possible Enhancements](#future-possible-enhancements)
- [Acknowledgements](#acknowledgements)

---

## Introduction

This is a Flask-based energy billing dashboard that integrates with the **eGauge API** to retrieve real-time and historical electricity usage data from a registered smart meter.

It features:

- Live register readings and deltas
- Cost calculation using user-defined tariffs
- Auto-updated consumption/generation stats
- Exportable reports via browser printing or PDF
- Clean separation of staff roles and dashboard routing

---

## Prerequisites

To run this project, you'll need:

- Python 3.10+
- pip
- Valid eGauge account and credentials
- Access to a live eGauge meter with public API
- MySQL Package (Workbench/Server etc.)

---

## Getting Started

1. Cloning Repository

    In a directory of your choice, clone this repository using the commands below

    ```bash
    git clone https://github.com/KiseraTimon/eenovators.git
    ```

2. Project setup:

    With the project cloned into your directory, the following steps will ensure you have a stable and running application

    - *Virtual Environment*

    First, create a virtual environment within the cloned project. If you are prompted to change the environment, click yes

    ```bash
    python -m venv .venv
    ```

    Next, activate the environment. You should see the name of your environment enclosed in parenthesis after this step

    ```bash
    .venv/scripts/activate
    ```

    - *Installing dependencies*

    With the virtual environment running, you can now install the dependencies used in this project

    ```bash
    pip install -r dependencies.txt
    ```

3. Configuring app files

    The application is still not ready to run, and a few changes MUST be made to the code. The following guidelines will conduct you through the necessary steps to both preview and run the app.

    - *Secret Key*

    By default, this particular app expects a `env.py` file.

    To setup your secret key manually, reference the [**assets**](#assets) section of this document, and locate the `env_example.py` file.

    Copy the contents of the file into a new `env.py` file within `website/config/env.py`

    - *Database Configuration*

    A MySQL database is used to store user data and newsletter information.

    This application expects a `connector.py` file that handles database connection.

    First, however, create a new MySQL database using the script provided in `website/database/eenovators.sql`. Then, reference the [**assets**](#assets) section of this document, and locate the `connector_example.py` file.

    Copy the contents of the file into a new `connector.py` file within `website/database/connector.py` and populate accordingly

    ```t
    host = ''           #Typically 'localhost'
    user = ''           # Typically 'root'
    password = ''       # Your MySQL password
    database = ''       # Your created database's name
    ```

4. Starting Server

    With the app configuration process complete, you can now run the develoment server using the commands below in your root app directory

    ```bash
    python main.py
    ```

## Project Structure

By the end of the setup, your project directories should look like this:

```t
├──.venv/
├──/logs/
├── website/                        # Flask Blueprint views & logic
│   ├── config                      # Configuration & Constants File
│   │   ├── __init__.py
│   │   ├── env_example.py
│   │   └── env.py
│   ├── database                    # Database Setup Files
│   │   ├── __init__.py
│   │   ├── connector_example.py
│   │   ├── connector.py
│   │   └── innovate.sql
│   ├── static                      # UI Assets
│   │   ├── css
│   │   ├── fonts
│   │   ├── images
│   │   └── js
│   ├── templates                   # UI Pages
│   │   ├── auth
│   │   ├── dashboard
│   │   ├── home
│   │   └──other
│   ├── __init__.py                 # App Initialization File
│   ├── auth.py                     # Authentication Backend
│   ├── dashboard.py                # Dashboard Backend
│   ├── processes.py                # Process Logics
│   └── views.py                    # UI Page Rendering
├── .gitignore                      # Git Commit Exclusions
├── dependencies.txt                # List of Dependencies
├── Task Details.pdf                # Task Details File
├── README.md                       # Documentation
└── utils.py                        # Custom Logging Helper
```

## Usage

1. User Accounts

    A user account is required to navigate access-controlled pages, like the dashboard.

    With the application running, use the sign up button to navigate to the registration page, where you can create a new account.

    The account will reflect on your MySQL Workbench. With the command below, you can access the list of all users in the system

    ```bash
    SELECT * FROM eenovators.users;
    ```

    Role access is still not automated in the system, hence, you'll need to manually change the user role of your registered user. You can use the command below

    ```bash
    UPDATE `[database]`.`[table]` SET `[field]` = 'staff' WHERE (`[attribute]` = '[key]');
    ```

    Change the values in square brackets accordingly

2. API Configuration

    - eGauge Keys
    You'll need access to an **eGauge** online meter with valid credentials.

    With valid credentials, modify **BASE_URL**, **EGAUGE_USER** and **EGAUGE_PASS** in `website/config/env.py` as below:

    ```t
    BASE_URI='https://DEV.egaug.es/'    # Replace DEV with eGauge Meter e.g egauge12345
    EGAUGE_USER=''                      # eGauge Username
    EGAUGE_PASS=''                      # eGauge Password
    ```

    - *Connection Management*

    Navigate to `.venv/Lib/site-packages/egauge/examples/test_common.py`

    In this file, replace:

    ```t
    meter_dev = os.getenv("EGDEV", "http://egauge-dut")
    meter_user = os.getenv("EGUSR", "dmo")
    meter_password = os.getenv("EGPWD", "secret password")
    ```

    with:

    ```t
    from website.config import env

    meter_dev = env.BASE_URI
    meter_user = env.EGAUGE_USER
    meter_password = env.EGAUGE_PASS
    ```

    The API linking your data to this application is now complete

3. Dashboard

    If the above steps are all followed correctly, access management is a non-issue and the API should work correctly. You can check either `logs/sys_logs/api.txt` or `logs/err_logs/dashboard/api` for communication regarding API configuration

    - *Restart Server*

    Kill the current server using `Ctrl + C` and restart with the command below

    ```bash
    python main.py
    ```

    With the server up and running again, you can logout of existing sessions and re-authenticate. This will help with updating your role on session data.

    You can now access the dashboard using the **dash** button on your navbar.

    The dashboard consists of a set of tables with energy statistics popuated by your API. It also features a tariff calculator that calculates cost real-time. There is a **download report** button to print/download the report in PDF format.

## Future Possible Enhancements

- Support for multiple meters and historical trend visualization
- Persistent storage of calculated invoices (database)
- Export to custom PDF (WeasyPrint with server-side logic)
- Admin controls to manage user roles and rates
- Real-time websocket updates

## Acknowledgements

[eGauge Systems](https://www.egauge.net/)

[eenovators](https://eenovators.com/)

## Assets

<details>
<summary><strong>env_example.py</strong></summary>

```bash
from egauge import webapi

from utils import errhandler, message, syshandler

# Application Settings
FLASK_ENV=''
SECRET_KEY=''

# Egauge Settings
BASE_URI='https://DEV.egaug.es/' #Replace DEV with eGauge meter
EGAUGE_USER=''
EGAUGE_PASS=''

# Parser
dev = webapi.device.Device(BASE_URI, webapi.JWTAuth(EGAUGE_USER, EGAUGE_PASS))

# Testing API Connection
try:
    METER = dev.get('/config/net/hostname')

    # Validating API Connection
    if METER != (None or ""):
        syshandler(f"API connection {METER} established", "api")
        message("[API]... Success")
    else:
        raise ValueError("Invalid response")

except Exception as e:
    errhandler(e, "api")
    syshandler("API connection failed", "api")
    message("[API]... Fail")


```

<details>
<summary><strong>eenovators.sql</strong></summary>

```bash
CREATE DATABASE eenovators;

USE eenovators;

CREATE TABLE
    users (
        userID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        fname VARCHAR(100) NOT NULL,
        lname VARCHAR(100) NOT NULL,
        uname VARCHAR(100) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        phone INT NOT NULL,
        password VARCHAR(255) NOT NULL,
        role VARCHAR(100) NOT NULL,
        dateUpd TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE
    newsletters (
        emailID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(100) NOT NULL UNIQUE,
        user VARCHAR(10) NOT NULL
    );

```
