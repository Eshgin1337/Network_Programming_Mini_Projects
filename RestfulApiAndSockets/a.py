from flask import Flask, request, abort, make_response, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

a={}
b=[]
ac={}
bc=[]
dealsc={}
dealsp={}

HOST = '127.0.0.1'
PORT = 4444



class PC_add(Resource):
    def put(self):
        
        NAME=request.form['NAME']
        PRICE=int(request.form['PRICE'])
        DETAILS=request.form['DETAILS']


        a[NAME]=[len(b),PRICE,DETAILS]
        b.append(NAME)

        return {'ok':'200'}

class PC_delete(Resource):
    def put(self, NAME):
        
        NAME=request.form['NAME']

        b[a[NAME][0]]=''
        a[NAME]=[]

        return {'ok':'200'}

class CLIENT_add(Resource):
    def put(self):
        
        EMAIL=request.form['EMAIL']
        DETAILS=request.form['DETAILS']

        ac[EMAIL]=[len(bc),DETAILS,0]
        bc.append(EMAIL)

        return {'ok':'200'}

class CLIENT_delete(Resource):
    def put(self):
        
        EMAIL=request.form['EMAIL']

        bc[ac[EMAIL][0]]=''
        ac[EMAIL]=[]

        return {'ok':'200'}

class DEALS(Resource):
    def put(self):

        EMAIL=request.form['EMAIL']
        NAME=request.form['NAME']

        ac[EMAIL][2]+=a[NAME][1]
        try:
            dealsc[EMAIL].append(NAME)
            dealsp[NAME].append(EMAIL)
        except:
            dealsc[EMAIL]=[]
            dealsp[NAME]=[]
            dealsc[EMAIL].append(NAME)
            dealsp[NAME].append(EMAIL)

        return {'ok':'200'}

class SHOWCUSTOMERDEALS(Resource):
    def put(self):

        EMAIL=request.form['EMAIL']

        return {'ok':dealsc[EMAIL]}

class SHOWPCDEALS(Resource):
    def put(self):

        NAME=request.form['NAME']

        return {'ok':dealsp[NAME]}

class SHOWMAX(Resource):
    def get(self):

        maxx=-1
        q='a'
        for i in range(len(bc)):
            if ac[bc[i]][2]>maxx:
                maxx=ac[bc[i]][2]
                q=ac[bc[i]][1]

        return {'ok':q}

api.add_resource(PC_add, '/PC_add')
api.add_resource(PC_delete, '/PC_delete')
api.add_resource(CLIENT_add, '/CLIENT_add')
api.add_resource(CLIENT_delete, '/CLIENT_delete')
api.add_resource(DEALS, '/DEAL_add')
api.add_resource(SHOWCUSTOMERDEALS, '/SHOWCUSTOMERDEALS')
api.add_resource(SHOWPCDEALS, '/SHOWPCDEALS')
api.add_resource(SHOWMAX, '/SHOWMAX')

if __name__ == '__main__':
    app.run(debug=True)