import flet as ft

def main(page: ft.Page):
  page.title = "Formulário de Contato"

  def apertou_enviar(evento):
    page.add(ft.Text("Formulário Enviado!", size=15, color="green"))
    nome.value = ""
    email.value = ""
    mensagem.value = ""
    page.update()

  txt1 = ft.Text(value="Formulário de Contato", size=30, weight="bold")
  nome = ft.TextField(label="NOME", width=700, hint_text="Digite seu nome...", bgcolor="#001969", color="#ffffff")
  email = ft.TextField(label="EMAIL", width=700, hint_text="Digite seu email...", bgcolor="#001969", color="#ffffff")
  bnt = ft.ElevatedButton("ENVIAR", on_click=apertou_enviar, bgcolor="#ffffff", color="#001969")
  txt2 = ft.Text(value="Sua Mensagem", size=20, weight="bold")
  mensagem = ft.TextField(label="SUA MENSAGEM", width=700, hint_text="Digite sua mensagem...", bgcolor="#001969", color="#ffffff")


  page.add(txt1, nome, email, txt2, mensagem, bnt)

ft.app(target=main)
