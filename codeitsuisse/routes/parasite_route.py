import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.routes.solve import solve_All

logger = logging.getLogger(__name__)




@app.route('/parasite', methods=['POST'])
def parasite_route():
    data=request.get_json()
    ans=[]
    for room in data:
        ans.append(solve_All(room))
    return json.dumps(ans)

