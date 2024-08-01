#getcounty/numeOras - sa returneze judetul din care provine

from judete import *
from flask import Flask,request

app=Flask(__name__)

@app.route('/getCounty/<numeOras>')
def getCounty(numeOras):
    for judet in romaniaFaraDiacr:
        if numeOras in romaniaFaraDiacr[judet] or numeOras==judet:
            return judet
    return 'Not found',404

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

