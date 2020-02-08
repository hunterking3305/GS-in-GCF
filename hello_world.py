def hello_world(request):
    request_json = request.get_json()
    
    print("---------------")
    print(type(request_json["age"]))
    print("---------------")
    return "Hi, " + request_json["name"] + ", age is " + str(request_json["age"])