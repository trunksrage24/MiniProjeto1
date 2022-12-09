# MiniProjeto1

#trabalho realizado por: 
    Vitor Daniel, nº a22204782 
    João Carvalho, nº a22204909

1º commit - implementaçao de um esqueleto e ideia base.
2º commit - dar valor de venda a cada item (ideia geral) e contar receitas e recursos; decidir valores iniciais de recursos, receitas e dinheiro.
3º commit - implementaçao de funcao de compra de recursos e craft de items (incompleto)
4º commit - adicionado o sistema de monetizaçao a funçao de crafting e criaçao da funçao de venda de items
5º commit - criaçao de sistema de npcs com personalidades para comprar items
6º commit - "still finishing npc function; still need to apply to main code: removing resource spent on crafting, 
            adding and/or removing money, updating lists of items (and their amounts) and recipes"
7º commit - completou se funcao de comprar recursos, funcao comprar receitas esta quase concluida (missing a couple ifs)

4 recursos - iron, gold, leather e wood

starting amounts:
    money - 7000
    wood - 5
    leather - 5
    iron - 5
    gold - 0

22 receitas totais

Relatório:
    
    Embora cada um tenha ficado responsável por fazer cada funçao e/ou classes, ambos ajudamos mutuamente tanto na parte de programar como em correções (de erros no codigo, missing coments, má legibilidade devido a falta de identações, etc).

    João :
        fez Função do "BuyResourceRecipes",
        fez função do "CraftingItems",
        fez função de "VerifyWin",
        fez função de "verifyrecipes",
        fez inventarios(variaveis nas classes),
        fez variaveis globais nas classes e correspondente uso nas funções(exceto função "SellingItems"),
        fez dicionarios,
        fez comentarios das funções e dicionários(exceto selling items e classes),
        fez parte final do relatório.
    
    Vitor:
        fez esqueleto inicial(classes sem variaveis),
        fez função "SellingItems",
        fez função de "levelup",
        fez class todas(class de npc toda),
        fez dicionário com receitas como esboço num ficheiro á parte,
        fez organização de código (idents e coments),
        fez parte de arranjo de interatividade com o jogador(prints),
        fez relatório.

Arquitetura da solução:
        A class "Item" é pai da class Swords(pai de SwordIni,SwordInter,SwordAdva),Armors(pai de HelmetIni,HelmetInter,HelmetAdva,ChestplatelIni,ChestplateInter,ChestplateAdva,LegginsIni,LegginsInter,LegginsAdva,ShoesIni,ShoesInter,ShoesAdva),Shields(pai de ShieldIni,ShieldInter,ShieldAdva) e Bows(BowIni,BowInter,BowAdva), cada um dos filhos destas 4 classes variaveis que servem para guardar o valor dos recursos que são necessarios para os fazer podem ser "wood","leather","iron" e "gold", todos têm tambem "SuccessRating" que depende da qualidade do item e por final "qt" que é usada para guardar a quantidade de items daquela class criados(ex:jogador criou 1 Sword inicial->Sword.qt=1).

Referências:
        Usado "Import ramdom" para fazer multiplos geradores de numeros, na função "CraftItems" e "BuyResourceRecipes" e "SellingItems".
        Exemplos de W3schools para uso de dicionario, classes e random.
