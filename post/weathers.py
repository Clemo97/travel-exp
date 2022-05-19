
import requests
from flask import Flask, render_template, request

from app import db


class City(db.Model):
     __tablename__ = 'city'
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(50), nullable=False)

