#!/bin/bash
pip install --upgrade pip
pip freeze > requirements.txt
pip install -r requirements.txt