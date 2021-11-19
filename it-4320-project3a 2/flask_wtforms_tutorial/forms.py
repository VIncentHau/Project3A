"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from datetime import date
from wtforms.fields.html5 import DateField
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length



class StockForm(FlaskForm):
    """Generate Your Graph."""
    
    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    #using the alphavantage api ---if doesn't work, use a json or a csv file--

    stockList_file = '/project/flask_wtforms_tutorial/nasdaqlisted.txt'
    #

    stockList= open(stockList_file)


    

    # print processed tabular data (if exists any)
    count = 0
    stock_choices = []
    for data in stockList:
        count +=1
        if count > 1:
            savedData = data.split("|")
            stock_choices.append(tuple((savedData[0], savedData[0])))


        

    symbol = SelectField("Choose Stock Symbol",[DataRequired()],
        choices=stock_choices,
    )

    chart_type = SelectField("Select Chart Type",[DataRequired()],
        choices=[
            ("1", "1. Bar"),
            ("2", "2. Line"),
        ],
    )

    time_series = SelectField("Select Time Series",[DataRequired()],
        choices=[
            ("1", "1. Intraday"),
            ("2", "2. Daily"),
            ("3", "3. Weekly"),
            ("4", "4. Monthly"),
        ],
    )

    start_date = DateField("Enter Start Date")
    end_date = DateField("Enter End Date")
    submit = SubmitField("Submit")
