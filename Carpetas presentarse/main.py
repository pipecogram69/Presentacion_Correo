from services.email_service import EmailService
from domain.equipo import Equipo
from utils.validator import validar_email

DESTINATARIO = "eburiticam@ucentral.edu.co"

def main():
    if not validar_email(DESTINATARIO):
        print("Correo destino inválido")
        return

    integrantes = [
        "Felipe Cortes",
        "Erik buritica ",
        
    ]

    github_url = "https://github.com/pipecogram69/Presentacion_Correo"


    equipo = Equipo(integrantes, github_url)
    mensaje = equipo.generar_mensaje()

    servicio = EmailService()
    enviado = servicio.enviar(
        DESTINATARIO,
        "Entrega Proyecto – Envío de Correo",
        mensaje
    )

    if enviado:
        print("Correo enviado correctamente ✅")
    else:
        print("No se pudo enviar el correo ❌")

if __name__ == "__main__":
    main()
