import os
from flask import Flask, render_templates, requests, send_from_directory


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

