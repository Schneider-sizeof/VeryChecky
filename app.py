from flask import Flask, render_template, request
import dns.resolver

app = Flask(__name__)

def verify_email_domain(email):
    try:
        domain = email.split('@')[1]
        records = dns.resolver.resolve(domain, 'MX')
        return True if records else False
    except Exception as e:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        is_valid = verify_email_domain(email)
        return render_template("index.html", email=email, is_valid=is_valid)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
