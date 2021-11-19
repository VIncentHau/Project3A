from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import StockForm
from .charts import *
import time


@app.route("/", methods=['GET', 'POST'])
@app.route("/stocks", methods=['GET', 'POST'])
def stocks():
    
    form = StockForm()
    if request.method == 'POST':
        if form.validate_on_submit():
           
            symbol = request.form['symbol']
            chart_type = request.form['chart_type']
            time_series = request.form['time_series']
            start_date = convert_date(request.form['start_date'])
            end_date = convert_date(request.form['end_date'])

            if end_date <= start_date:
               
                err = "ERROR: End date cannot be earlier than Start date."
                chart = None
            else:
               
                err = None
                 
                chart = getData(symbol, time_series, chart_type, start_date, end_date)

            return render_template("stock.html", form=form, template="form-template", err = err, chart = chart)
    
    return render_template("stock.html", form=form, template="form-template")