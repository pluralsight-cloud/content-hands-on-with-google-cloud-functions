import functions_framework

@functions_framework.http
def greetings_http(request):
   """HTTP Cloud Function.
   Args:
       request (flask.Request): The request object.
       <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
   Returns:
       The response text, or any set of values that can be turned into a
       Response object using `make_response`
       <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
   """
   request_json = request.get_json(silent=True)
   request_args = request.args

   if request_json and 'name' in request_json:
       name = request_json['name']
   elif request_args and 'name' in request_args:
       name = request_args['name']
   else:
       name = 'My Friend'
   return '<html><head></head>\
        <body style="background-color:#060C59;"><div style="height:100%;background-repeat:no-repeat;background-position:center;\
        background-image:url(https://raw.githubusercontent.com/pluralsight-cloud/content-hands-on-with-google-cloud-functions/main/http-2nd-gen/hello-world.jpg);">\
        <h1 style="padding-top:100px;font-size:48px;color:white;text-align:center;">Greetings from Pluralsight, {}!</h1>\
        </div></body></html>'.format(name)
