from website import create_app
app = create_app()
if __name__ =='__main__':
    app.run(debug=True, port=80)
    #app.run(ssl_context=('cert.pem', 'key.pem'), port=443)
