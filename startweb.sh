#!/bin/bash
gunicorn -c guniConf.ini web:app
