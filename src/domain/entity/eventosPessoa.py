from src.domain.schema.dadosUltimaCompraSchema import DadosUltimaCompra


class EventosPessoa():

    def __init__(self,
                 cpf,
                 ultimaConsulta,
                 movimentacaoFinanceira,
                 dadosUltimaCompra
    ):

        self.cpf = cpf
        self.ultimaConsulta = ultimaConsulta
        self.movimentacaoFinanceira = movimentacaoFinanceira
        self.dadosUltimaCompra = DadosUltimaCompra(valor=dadosUltimaCompra.valor,
                                                   local=dadosUltimaCompra.local,
                                                   data=dadosUltimaCompra.data)


        # pessoaCreate = EventosPessoa(
        #     cpf=pessoa.cpf,
        #     ultimaConsulta= "01/01/2000",
        #     movimentacaoFinanceira= 0.00,
        #     dadosUltimaCompra= dict(
        #         valor=0.00,
        #         local="Desconhecido",
        #         data="01/01/2000"
        #     )
        # ).__dict__