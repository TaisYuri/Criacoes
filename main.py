from fastfood import Fastfood

menu = Fastfood()
menu.apresentar_menu()

print('\n\n--------------- PEDIDO ---------------')

while True:
    item = int(input('Escolha um item (Digite 9 para finalizar): '))
    if item == 9:
        if len(menu.pedido) > 0:
            print('Seleção de itens finalizada...\n')
            observacoes = (input('Informe as observações do pedido: '))
            menu.fecha_conta()
            print(f'{"Observações:"} {observacoes}')

            print('\n1 - Alterar pedido \n2 - Excluir item \n3 - Finalizar ')
            alteracao = int(input('Digite: '))
            if alteracao == 1:
                menu.altera_qtd()
                menu.fecha_conta()
            elif alteracao == 2:
                menu.exclui_item()
                menu.fecha_conta()

        break
    qtd = int(input('Escolha a quantidade: '))
    menu.fazer_pedido(item, qtd)



