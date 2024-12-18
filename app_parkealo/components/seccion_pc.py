import reflex as rx
from ..components.mi_button import mi_button_p
def seccion_pc()->rx.Component:
  return rx.desktop_only(
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
      rx.text(rx.text.em("parkeo seguro",color="#92dafe",weight="bold")," esta aplicacion esta diseñada con el fin de encontrar estacionamientos y evitas llas multas",size="5",color="#eff9ff",width="70vw",border_shadow="#FFFFFF"),
     
    ),
    rx.vstack(
      rx.link(mi_button_p("user","saber más"),href="https://app.jotform.com/243327787319669"),
      margin_top="4em",
      align="center"
    ),
    width="70vw",
  )