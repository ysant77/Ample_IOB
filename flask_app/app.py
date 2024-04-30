from flask import Flask, render_template
import os

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)

data_dir = '../'
seq_in_file = os.path.join(data_dir, 'seq.in')
seq_out_file = os.path.join(data_dir, 'seq.out')
labels_file = os.path.join(data_dir, 'labels')
tokens_file = os.path.join(data_dir, 'tokens.txt')

def define_data_dict():
    data_dict = []
    with open(seq_in_file, 'r') as f_in, open(seq_out_file, 'r') as f_out, open(labels_file, 'r') as f_labels:
        for seq_in, seq_out, label in zip(f_in.readlines(), f_out.readlines(), f_labels.readlines()):
            data_dict.append({
                'intent': label.strip(),  # Assuming intent labels are stored per line
                'sentence': seq_in.strip(),
                'tokens': seq_in.strip().split(),
                'tags': seq_out.strip().split()
            })
    return data_dict

@app.route('/')
def index():
    return render_template('index.html', data=define_data_dict())

if __name__ == '__main__':
    app.run(debug=True, port=5000)