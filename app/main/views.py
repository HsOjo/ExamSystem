from flask import Flask, render_template, request
from . import main


@main.route('/')
@main.route('/index')
def index():
    return render_template('main/index.html')