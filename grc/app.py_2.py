import os
import pandas as pd 
import numpy as numpy

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2

engine = create_engine('postgres+psycopg2://postgres:postgres@localhost:5432/NHL Stats')
app = Flask(__name__)


