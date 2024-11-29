from myapp import app       #imports app object from myapp module


if __name__=='__main__':    #runs when file is executed directly
    app.run(debug=True)     #starts web server and listens for HTTP request