import web

web.config.smtp_server = 'smtp.gmail.com'
web.config.smtp_port = 587
web.config.smtp_username = 'ruvido@gmail.com'
web.config.smtp_password = 'S0le.Mi0'
web.config.smtp_starttls = True

web.sendmail('5pani2pesci <info@5p2p.it>', '', 'subject', 'message',bcc='ruvido@gmail.com')


