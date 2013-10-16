import web

if 1:
	web.config.smtp_server = 'smtp.gmail.com'
	web.config.smtp_port = 587
	web.config.smtp_username = 'ruvido@gmail.com'
	web.config.smtp_password = 'S0le.Mi0'
	web.config.smtp_starttls = True
	
	
urls = (
  '/hello', 'Index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    #def GET(self):
    #    return render.hello_form()

    def POST(self):
        form = web.input(nome="Nobody", email="Hello")
        greeting = "%s, %s" % (form.nome, form.email)
    	web.sendmail('5pani2pesci <info@5p2p.it>', '', greeting, 'message',bcc='ruvido@gmail.com')
        return greeting

if __name__ == "__main__":
    app.run()




