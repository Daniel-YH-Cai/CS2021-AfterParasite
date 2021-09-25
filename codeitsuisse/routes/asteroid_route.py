import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from codeitsuisse.routes.asteroid import asteroid
from codeitsuisse.routes.solve import solve_All

logger = logging.getLogger(__name__)




@app.route('/asteroid', methods=['POST'])
def asteroid_route():
    data=request.get_json()['test_cases']
    ans=[]
    for case in data:
        origin, score=asteroid(case)
        ans.append({"input":case,"score":int(score),"origin":int(origin)})
    return json.dumps(ans)

