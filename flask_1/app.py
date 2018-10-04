from flask import Flask, jsonify, request, Response
import json
app = Flask(__name__)
print(__name__)

mfunds = [
    {
        'fund_house': 'Aditya Birla',
        'fund_name': 'Aditya Birla Tax Saver 96',
        'nav': 143.78,
        'fund_id': 101
    },
    {
        'fund_house': 'Canara Robecco',
        'fund_name': 'Canara Robecco Emerging Equities',
        'nav': 85.29,
        'fund_id': 102
    }
]


# GET /mfunds
@app.route('/mfunds')
def get_mfunds():
    return jsonify({'mfunds': mfunds})


def validMfFund(mfObject):
    if ("fund_house" in mfObject and "fund_name" in mfObject and "nav" in mfObject and "fund_id" in mfObject):
        return True
    else:
        return False


@app.route('/mfunds', methods=['POST'])
def add_fund():
    print ('Here')
    # return jsonify(request.get_json())
    request_data = request.get_json()
    print(request_data)
    if (validMfFund(request_data)):
        new_fund = {
            "fund_house": request_data['fund_house'],
            "fund_name": request_data['fund_name'],
            "nav": request_data['nav'],
            "fund_id": request_data['fund_id']
        }
        mfunds.insert(0, new_fund)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/mfunds/" + str(new_fund["fund_id"])
        return response
    else:
        invalidFundObjectErrorMsg = {
            "error": "Invalid Fund object passed in request",
            "helpString": "Expected Data string"
        }
        response = Response(json.dumps(invalidFundObjectErrorMsg), 401, mimetype='application/json')


@app.route('/mfunds/<int:fund_id>')
def get_fund_nav(fund_id):
    return_value = {}
    for fund in mfunds:
        print(fund)
        if fund['fund_id'] == fund_id:
            print('YES')
            return_value = {
                'fund_name': fund['fund_name'],
                'nav': fund['nav'],
                'fund_id': fund['fund_id']
            }
            return jsonify(return_value)


app.run(port=5000)
