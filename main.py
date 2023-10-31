from fastapi import FastAPI #class
app=FastAPI() #class instance
#api accepts incoming request sent by client in this case web browser


# def index(): #we need to associate this function with specific URL Request 
#     return "Hello World !"


#we add a decorator on top of function and make use of app instance 
#we want this app instance to handle get request from the client
#it means when user hits '/' then this function should be executed
@app.get('/') 
def index(): #we need to associate this function with specific URL Request 
    return "Hello World !"

#reload automatically restarts server when making changes to code


@app.get('/new')
def new():
    return "This is a new page"

@app.get("/fruits")
def fruits():
    return  {"Fruits list":{"Mango","Apple"}}