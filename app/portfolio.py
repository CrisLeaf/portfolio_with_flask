from flask import (
	Blueprint, render_template, request, redirect, url_for, current_app
)


bp = Blueprint("portfolio", __name__, url_prefix="/")

@bp.route("/", methods=["GET"])
def index():
	return render_template("portfolio/index.html")

# @bp.route("/mail", methods=["GET", "POST"])
# def mail():
# 	name = request.form.get("name")
# 	email = request.form.get("email")
# 	message = request.form.get("message")
#
# 	if request.method == "POST":
# 		send_mail(name, email, message)
#
# 		return render_template("portfolio/sent_mail.html")
#
# 	return redirect(url_for("portfolio.index"))
#
# def send_mail(name, email, message):
# 	mi_email = "cristobal_javier@hotmail.com"
# 	sg = sendgrid.SendGridAPIClient(api_key=current_app.config["SENDGRID_KEY"])
#
# 	from_email = Email(mi_email)
# 	to_email = To(mi_email, substitutions={
# 		"-name-": name,
# 		"-email-": email,
# 		"-message-": message
# 	})
#
# 	html_content = """
# 		<p>Hola Cris, tienes un nuevo contacto desde la web:</p>
# 		<p>Nombre: -name-</p>
# 		<p>Mail: -email-</p>
# 		<p>Mensaje: -message-</p>
# 	"""
#
# 	mail = Mail(mi_email, to_email, "Nuevo contacto desde la web", html_content=html_content)
# 	response = sg.client.mail.send.post(request_body=mail.get())
# 	print(response.status_code)
# 	print(response.body)
# 	print(response.headers)

@bp.route("/mail", methods=["GET"])
def mail():
	return render_template("portfolio/sent_mail.html")
