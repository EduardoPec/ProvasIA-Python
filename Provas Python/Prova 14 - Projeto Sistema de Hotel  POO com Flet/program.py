import datetime

class Cliente:
    def __init__(self, nome, telefone, email, id_unico):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id_unico = id_unico

class Quarto:
    def __init__(self, num_quarto, tipo_quarto, preco_diaria, status_disp):
        self.num_quarto = num_quarto
        self.tipo_quarto = tipo_quarto
        self.preco_diaria = preco_diaria
        self.status_disp = status_disp

    def modelo_quarto(self):
        if self.tipo_quarto == 1:
            return "Simples (1 pessoa)"
        elif self.tipo_quarto == 2:
            return "Duplo (2 pessoas)"
        elif self.tipo_quarto == 3:
            return "Suíte (4 pessoas)"
        else:
            return "Tipo de quarto desconhecido"

    def preco_quarto(self):
        return self.preco_diaria

class Reserva:
    def __init__(self, dono_reserva, quarto_reservado, checkin, checkout, status_reserva):
        self.dono_reserva = dono_reserva
        self.quarto_reservado = quarto_reservado
        self.checkin = checkin
        self.checkout = checkout
        self.status_reserva = status_reserva

class GerenciadorReservas:
    def __init__(self, clientes, quartos):
        self.clientes = clientes
        self.quartos = quartos
        self.reservas = []

    def verificacao(self, status_disp):
        return status_disp

    def criar_reserva(self, cliente, quarto, checkin, checkout):
        if self.verificacao(quarto.status_disp):
            reserva = Reserva(cliente, quarto, checkin, checkout, "Confirmada")
            self.reservas.append(reserva)
            quarto.status_disp = False
            return f"{cliente.nome}, seu quarto {quarto.num_quarto} ({quarto.modelo_quarto()}) foi reservado com sucesso! Preço da diária: R${quarto.preco_quarto()}"
        else:
            return f"O quarto {quarto.num_quarto} ({quarto.modelo_quarto()}) está indisponível."

    def listar_reservas(self):
        return sorted(self.reservas, key=lambda r: datetime.datetime.strptime(r.checkin, "%d-%m-%Y"))

    def cancelar_reserva(self, reserva):
        reserva.status_reserva = "Cancelada"
        reserva.quarto_reservado.status_disp = True
        return f"A reserva de {reserva.dono_reserva.nome} no quarto {reserva.quarto_reservado.num_quarto} foi cancelada com sucesso."
