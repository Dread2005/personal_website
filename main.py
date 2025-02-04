from sqlite3 import connect

from flask import Flask, render_template, url_for, request
import smtplib
import os

app = Flask(__name__)

gapp_pswrd = 'yflw jeuh ryxp vvpq'
my_email = 'tshifhiwachedzafordjr@gmail.com'

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        msg = {
            'Name': request.form['name'],
            'Email': request.form['email'],
            'Msg': request.form['message']
        }

        print(msg)
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=gapp_pswrd)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject: A message from a may be employee \n\n"
                                    f"{msg['Name']}\n"
                                    f"{msg['Email']}\n"
                                    f"{msg['Msg']}")
        return render_template('website.html', methods=['POST'])
    else:
        return render_template('website.html', methods=['POST'])


if __name__ == '__main__':
     app.run(debug=True)