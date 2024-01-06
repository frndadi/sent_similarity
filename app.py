# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from flask import Flask, request,jsonify
from utils import run_common_steps
from model_file import embed_vec, cosine_sim

app = Flask(__name__)



@app.route('/')
def helloWorld():
    return "Welcome to AI-World..!!" 


# @app.route('/score',  methods=['GET', 'POST'])
# def sent_similrity():
        
#     args = request.get_json( )
#     print(args)

#     try:
#         text1=args.get("text1")
#         text2=args.get("text2")
        
#         text_data = pd.DataFrame({'text1':[text1],
#                                   'text2':[text2]})

#         filtrd_df = run_common_steps(text_data)
#         if len(filtrd_df) ==1:
#             sent1 = filtrd_df['text1'][0]
#             sent2 = filtrd_df['text2'][0]

#             embedings = embed_vec(sent1, sent2)
#             score = cosine_sim(embedings)[0]
#             rslt = {"similarity score": str(score) }

#     except:
#         rslt = {"similarity score": 0.0 }
#     return jsonify(rslt)


if __name__ == "__main__":
    app.run()



