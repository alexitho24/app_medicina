import reflex as rx
from ..components.mi_button import mi_button_p
def seccion_pc()->rx.Component:
  return rx.desktop_only(
    rx.heading(
      "Tecnología al servicio de tu salud",
      color="#eff9ff",
      size="8",
      align="center"
    ),
    rx.heading(
      "con ",
      rx.text.em("Doc al rescate",color="#00addd"),
      color="#cdf9ff",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("Doc al rescate",color="#0189b9",weight="bold")," La aplicación de medicina es una solución integral diseñada para mejorar la eficiencia y la calidad de la atención médica. Ofrece una amplia gama de herramientas y funcionalidades que permiten a los profesionales de la salud acceder, gestionar y analizar información médica de manera más efectiva. La aplicación se caracteriza por su enfoque en la facilidad de uso, la seguridad de los datos y la integración con sistemas médicos existentes.",size="5",color="#eff9ff",width="70vw"),
      rx.box(
        rx.image(src="/img_seccion.png",alt="Imagen de app"),
        width="30vw"
      ),
      align="center"
    ),
    rx.vstack(
      rx.link(mi_button_p("user","Inicia Sesion"),href="/login"),
      margin_top="4em",
      align="center"
    ),
    width="70vw",
  )