import datetime
import flet as ft
from program import Cliente, Quarto, Reserva, GerenciadorReservas

def main(page: ft.Page):
    cliente1 = Cliente("João", "123456789", "joao@email.com", "C001")
    cliente2 = Cliente("Maria", "987654321", "maria@email.com", "C002")
    quarto1 = Quarto(101, 1, 70, True)
    quarto2 = Quarto(102, 2, 120, True)
    quarto3 = Quarto(103, 3, 200, True)
    gerenciador = GerenciadorReservas([cliente1, cliente2], [quarto1, quarto2, quarto3])

    reserva_selecionada = None
    modo_edicao = False

    cliente_dropdown = ft.Dropdown(label="Selecione o Cliente", width=400, border_color=ft.Colors.WHITE)
    quarto_dropdown = ft.Dropdown(label="Selecione o Quarto", width=400, border_color=ft.Colors.WHITE)
    checkin_input = ft.TextField(label="Data de Check-in (dd-mm-aaaa)", width=400, border_color=ft.Colors.WHITE)
    checkout_input = ft.TextField(label="Data de Check-out (dd-mm-aaaa)", width=400, border_color=ft.Colors.WHITE)
    status_dropdown = ft.Dropdown(label="Status", options=[ft.dropdown.Option("Confirmada"), ft.dropdown.Option("Cancelada")], width=400, border_color=ft.Colors.WHITE)
    resultado_texto = ft.Text(value="", color=ft.Colors.BLUE)

    reservas_listview = ft.ListView(expand=1, spacing=5, height=250)
    editar_button = ft.ElevatedButton("Salvar Edição", disabled=True, bgcolor=ft.Colors.ORANGE, color=ft.Colors.WHITE)

    formulario_column = ft.Column([
        ft.Row([cliente_dropdown], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([quarto_dropdown], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([checkin_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([checkout_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton("Reservar", on_click=lambda e: reservar_quarto(e), bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE), editar_button], alignment=ft.MainAxisAlignment.CENTER),
    ], spacing=10)

    def preencher_dropdowns():
        cliente_dropdown.options = [ft.dropdown.Option(cliente.nome) for cliente in gerenciador.clientes]
        quarto_dropdown.options = [ft.dropdown.Option(f"Quarto {quarto.num_quarto} - {quarto.modelo_quarto()}") for quarto in gerenciador.quartos]
        page.update()

    def update_reservas_listview():
        reservas_listview.controls = []
        for reserva in gerenciador.listar_reservas():
            try:
                checkin_date = datetime.datetime.strptime(reserva.checkin, "%d-%m-%Y")
                checkout_date = datetime.datetime.strptime(reserva.checkout, "%d-%m-%Y")
                num_dias = (checkout_date - checkin_date).days
            except Exception:
                num_dias = 1
            if num_dias < 1:
                num_dias = 1
            total = reserva.quarto_reservado.preco_diaria * num_dias
            noites_texto = f"{num_dias} noite" if num_dias == 1 else f"{num_dias} noites"
            status_icone = "✅" if reserva.status_reserva == "Confirmada" else "❌"
            status_cor = ft.Colors.GREEN if reserva.status_reserva == "Confirmada" else ft.Colors.RED

            reservas_listview.controls.append(
                ft.ListTile(
                    title=ft.Text(
                        f"{status_icone} {reserva.dono_reserva.nome} - Quarto {reserva.quarto_reservado.num_quarto} | Check-in: {reserva.checkin} "
                        f"| Check-out: {reserva.checkout} | Diária: R${reserva.quarto_reservado.preco_diaria:.2f} | Total ({noites_texto}): R${total:.2f}",
                        color=status_cor, size=14
                    ),
                    leading=ft.IconButton(ft.icons.EDIT, icon_color=ft.Colors.ORANGE, on_click=lambda e, r=reserva: iniciar_edicao(r)),
                    trailing=ft.IconButton(ft.icons.DELETE, icon_color=ft.Colors.RED, on_click=lambda e, r=reserva: cancelar_reserva_func(r)),
                )
            )
        page.update()

    def reservar_quarto(e):
        if not cliente_dropdown.value or not quarto_dropdown.value or not checkin_input.value or not checkout_input.value:
            resultado_texto.value = "Por favor, preencha todos os campos corretamente."
            resultado_texto.color = ft.Colors.RED
            page.update()
            return

        try:
            datetime.datetime.strptime(checkin_input.value, "%d-%m-%Y")
            datetime.datetime.strptime(checkout_input.value, "%d-%m-%Y")
        except ValueError:
            resultado_texto.value = "As datas devem estar no formato dd-mm-aaaa."
            resultado_texto.color = ft.Colors.RED
            page.update()
            return

        cliente = next(c for c in gerenciador.clientes if c.nome == cliente_dropdown.value)
        quarto_num = int(quarto_dropdown.value.split(" ")[1])
        quarto = next(q for q in gerenciador.quartos if q.num_quarto == quarto_num)

        mensagem = gerenciador.criar_reserva(cliente, quarto, checkin_input.value, checkout_input.value)
        resultado_texto.value = mensagem
        resultado_texto.color = ft.Colors.GREEN

        limpar_formulario()
        update_reservas_listview()
        page.update()

    def iniciar_edicao(reserva):
        nonlocal reserva_selecionada, modo_edicao
        reserva_selecionada = reserva
        modo_edicao = True
        cliente_dropdown.value = reserva.dono_reserva.nome
        quarto_dropdown.value = f"Quarto {reserva.quarto_reservado.num_quarto} - {reserva.quarto_reservado.modelo_quarto()}"
        checkin_input.value = reserva.checkin
        checkout_input.value = reserva.checkout
        status_dropdown.value = reserva.status_reserva

        if status_dropdown not in formulario_column.controls:
            formulario_column.controls.insert(4, ft.Row([status_dropdown], alignment=ft.MainAxisAlignment.CENTER))

        editar_button.disabled = False
        resultado_texto.value = f"Editando reserva de {reserva.dono_reserva.nome}"
        resultado_texto.color = ft.Colors.ORANGE
        page.update()

    def salvar_edicao(e):
        nonlocal reserva_selecionada, modo_edicao
        if reserva_selecionada:
            reserva_selecionada.dono_reserva = next(c for c in gerenciador.clientes if c.nome == cliente_dropdown.value)
            reserva_selecionada.quarto_reservado = next(q for q in gerenciador.quartos if f"Quarto {q.num_quarto}" in quarto_dropdown.value)
            reserva_selecionada.checkin = checkin_input.value
            reserva_selecionada.checkout = checkout_input.value
            reserva_selecionada.status_reserva = status_dropdown.value
            resultado_texto.value = "Reserva atualizada com sucesso!"
            resultado_texto.color = ft.Colors.GREEN
            limpar_formulario()
            update_reservas_listview()
            modo_edicao = False
            editar_button.disabled = True

            if status_dropdown in formulario_column.controls:
                formulario_column.controls.remove(ft.Row([status_dropdown], alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    def cancelar_reserva_func(reserva):
        mensagem = gerenciador.cancelar_reserva(reserva)
        gerenciador.reservas.remove(reserva)
        resultado_texto.value = mensagem
        resultado_texto.color = ft.Colors.ORANGE
        update_reservas_listview()
        page.update()

    def limpar_formulario():
        cliente_dropdown.value = None
        quarto_dropdown.value = None
        checkin_input.value = ""
        checkout_input.value = ""
        status_dropdown.value = None

        for control in formulario_column.controls:
            if isinstance(control, ft.Row) and status_dropdown in control.controls:
                formulario_column.controls.remove(control)
                break

    editar_button.on_click = salvar_edicao

    page.add(
        ft.Column(
            [
                ft.Text("Gerenciamento de Reservas", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                ft.Card(content=ft.Container(content=formulario_column, padding=20), elevation=4),
                ft.Card(content=ft.Container(content=ft.Column([
                    ft.Text("Reservas Atuais", size=20, weight=ft.FontWeight.BOLD),
                    reservas_listview,
                ], spacing=10), padding=20), elevation=4),
                resultado_texto,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    preencher_dropdowns()
    update_reservas_listview()

ft.app(target=main)
