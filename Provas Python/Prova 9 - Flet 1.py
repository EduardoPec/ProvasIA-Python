import flet as ft

def main (page: ft.Page):
    page.title = "Lista de Tarefas"
    page.bgcolor = ft.colors.BLUE

    tarefa_nova = ft.TextField(label="Nova Tarefa")
    lista_tarefas = ft.ListView(expand=True, controls=[])

    def adicionar_tarefa(e):
        lista_tarefas.controls.append(
            ft.Text(tarefa_nova.value)
        )
        tarefa_nova.value = ""
        page.update()
    
    botao = ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa)

    layout = ft.Column(
        controls=[
            ft.Text("Lista de Tarefas", size=30, weight="bold", color="black"),
            tarefa_nova,
            botao,
            lista_tarefas,
            ft.Text("Suas Tarefas", size=30, weight="bold", color="black"),
            ft.Container(
                content=lista_tarefas,
                border=ft.border.all(1, "black"),
                border_radius=ft.border_radius.all(5),
                padding=10,
                expand=True,
            ),
        ]
    )

    page.add(layout)

ft.app(target=main)