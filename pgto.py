valor_total = float(input("Digite o valor da compra: R$"))

opcao_pgto = ''

while opcao_pgto != 'B' and opcao_pgto != 'DE' and opcao_pgto != 'C' and opcao_pgto != 'DI' and opcao_pgto != 'PIX':

    opcao_pgto = input('''Escolha a forma de pagamento: 
(B) - Boleto 
(DE) - Débito 
(C) - Crédito
(DI) - Dinheiro
(PIX) - PIX
Digite a opção desejada: ''').upper()

    if opcao_pgto !='B' and opcao_pgto != 'DE' and opcao_pgto != 'C' and opcao_pgto != 'DI' and opcao_pgto != 'PIX':
        print('Opção inválida! Digite novamente.')

mostra = True

valor_pagar = 0
#Boleto = 15% e Dinheiro = 15%
if opcao_pgto == 'B' or opcao_pgto == 'DI':
    valor_pagar = valor_total * 0.85
elif opcao_pgto == 'DE' or opcao_pgto == 'PIX':
    valor_pagar = valor_total * 0.90
else:

    mostrar = False

    parcelar = input("Deseja parcelar: (S) Sim / (N) Não: ").lower()

    if parcelar == 'n':
        print(f'Valor a pagar R${valor_total}')

    else:
        n_parcela = int(input('Digite a quantidade de parcelas: ')) 
        valor_parcela = round(valor_total / n_parcela, 2 )

        print(f'Valor da parcela R$ {valor_parcela}  - Número de parcelas {n_parcela} - Valor total R$ {valor_total}')

if mostra: 
    print(f'Valor a pagar R${valor_pagar}')