from flask import render_template, flash, Blueprint, request, current_app
from flask_login import login_required

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/')
@login_required
def index():
    pass
