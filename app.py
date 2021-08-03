from flask import Flask, jsonify, request

import json

app=Flask(_name_)
@app.route('/',methods=["GET"])
def main():
  default_file={
      "is_success": True,
      "user_id": "john_doe_17091999", 
      "odd": [1,3,5,7,9],
      "even": [0,2,4,6,8]
  }
  return jsonify(default_file)
@app.route('/bfhl', methods=["GET","POST"])
def new():
  data=request.get_json()
  if data==None:
    return("EXPECTING INPUT")
  number=data["numbers"]
  
  odd=[]
  even=[]
  final_dict={}
  userid="Sanaa_Siddiqui_04052000"
  status = True
  for i in number:
      if i.isnumeric():
          if int(i)%2==0:
              even.append(int(i))
          else:
              odd.append(int(i))
      else:
          status=False
          break
  if status:
      final_dict["is_success"]=status
      final_dict["user_id"]= userid
      final_dict["odd"] = odd
      final_dict["even"] = even
  else:
      final_dict["is_success"]=status
      final_dict["user_id"]= userid

  return jsonify(final)

if _name=="main_":
    app.run()