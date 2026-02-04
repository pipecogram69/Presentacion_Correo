class Equipo:
    def __init__(self, integrantes, github_url):
        self.integrantes = integrantes
        self.github_url = github_url

    def generar_mensaje(self):
        mensaje = "Integrantes del equipo:\n\n"
        for nombre in self.integrantes:
            mensaje += f"- {nombre}\n"

        mensaje += f"\nRepositorio GitHub:\n{self.github_url}"
        return mensaje
