from flask import Flask, render_template
import os

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)

data_dir = '../'
seq_in_file = os.path.join(data_dir, 'seq.in')
seq_out_file = os.path.join(data_dir, 'seq.out')
labels_file = os.path.join(data_dir, 'labels')
tokens_file = os.path.join(data_dir, 'tokens.txt')

with open(seq_in_file, 'r') as f:
    seq_in = f.readlines()

with open(seq_out_file, 'r') as f:
    seq_out = f.readlines()

with open(labels_file, 'r') as f:
    labels = f.readlines()

with open(tokens_file, 'r') as f:
    tokens = f.readlines()

def define_data_dict():
    data_dict = []
    for i in range(len(seq_in)):
        data_dict.append({'sentence': seq_in[i], 'tokens': tokens[i].split(' ')
                        , 'tags': seq_out[i].split(' ')})
    return data_dict

@app.route('/')
def index():
    return render_template('index.html', data=define_data_dict())

if __name__ == '__main__':
    app.run(debug=True)