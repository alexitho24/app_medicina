import reflex as rx
from ..components.mi_button import mi_button_p
def seccion_mobile()->rx.Component:
  return rx.mobile_and_tablet(
    rx.heading(
      "parkeo seguro",
      color="#eff9ff",
      size="8",
      align="center"
    ),
    rx.heading(
       "con ",
      rx.text.em("parkea seguro con parkealo",color="#92dafe"),
      color="#eff9ff",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("parkea seguro",color="#eff9ff",weight="bold"),"esta aplicacion esta diseñada con el fin de encontrar estacionamientos y evitas llas multas.",size="5",color="#eff9ff",text_align="center"),
    ),
    rx.vstack(
      rx.link(mi_button_p("user","Registrate"),href="https://forms.gle/YXXCDQHRZFGDaYWp9"),
      margin_top="4em",
      align="center"
    ),
    width="90vw",
  )