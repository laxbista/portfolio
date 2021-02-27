from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')  # Decorator
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # Decorator
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv',newline ='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)  # Writes to database.txt
            write_to_csv(data)  # writes to database.csv
            return redirect('thankyou.html')
        except:
            return 'Did not save to Database'
    else:
        return 'Something went wrong'


if __name__ == '__main__':
    app.run(debug=True)
