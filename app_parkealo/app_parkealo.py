import reflex as rx
from .components.navbar import navbar
from .components.seccion import seccion
def index()->rx.components:
  return rx.vstack(
    navbar(),
    seccion(),
    width="100%",
        background="url('https://images.unsplash.com/photo-1712397943847-e104395a1a8b?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')",
        background_size="cover",
        background_position="center",
    height="100vh",
    align="center",
  )
app=rx.App()
app.add_page(index)
