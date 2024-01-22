from flask import Flask, redirect, url_for, request, render_template, send_from_directory
import flask
from core import pic
from core.orca import Orca

app = Flask(__name__)
PHandle = pic.PicHandler()
qe = Orca

@app.route("/api/v3", methods=['GET', 'POST'])
def apiv3():
    if request.method=='POST':
        if request.args['type']=='img':
            data = request.files['file']
            output = {"input_text":PHandle.getText(data),"max_questions":10}
            short_qs = qe.gen_single(output['input_text'])
            data = {"text":output,"short_qs":short_qs}
            return short_qs
        elif request.args['type'] == 'text':
            data = request.json
            output = {"input_text":data['text'],"max_questions":10}
            short_qs = qe.gen_single(output)
            data = {"text":output,"short_qs":short_qs}
            return short_qs
    else:
        return "This is a POST only end point!"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, use_reloader=False)