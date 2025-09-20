from flask import Flask, render_template

app = Flask(__name__)

@app.get("/hw1")
def display_hw1():
    return render_template("hw1.html", title="공공자전거 재배치 최적화 시스템 기획안")

if __name__ == "__main__":
    app.run(debug=True) #기본: http://127.0.01:5000, http://127.0.0.1:5000/hw1