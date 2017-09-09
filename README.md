# Minority-Report

## Grupo
Rute Souza de Abreu
Yuri Thomas Pinheiro Nunes

## Objetivos

Os objetivos do projeto são analisar os dados de ocorrências policiais e extrair informações que possam ajudar a predizer e responder de maneira eficiente. As ocorrencias foram registradas no banco de dados da policia do condado de Montgomery no estado de Maryland, Estados Unidos. Os dados são referentes aos últimos seis meses do ano de 2013. Os dados que podem ferir a privacidade de algum individuo foram removidos e informações como endereço foram arrendondados para um raio de 100 casas.

Para realizar os objetivos as ocorrências serão categorizadas pelo código de chamada utilizado na comunição via rádio. Serão realizados análises relacionadas a localização e tempo. Para análise de tempo será criado um perfil de ocorrências relacionado ao horário do dias e outro perfil de ocorrências relacionado aos dias da semana. Para localização foram criados perfis por cidade e por distrito policial.

##Divisão dos notebooks

Foram criados 3 notebooks e um script python. O script python faz algumas alterações no dataset original; são elas: a categorização dos crimes de acordo com o regimento policial do condado, a criação da coluna categoria informando a categoria a qual o crime pertence e a conversão das datas das ocorrências para o tipo DateTime. Este script é importado nos demais notebooks. O primeiro notebook é uma Descrição do dataset (Dataset description), contendo a descrição e a explicação de todas as colunas, bem como as respostas as questões iniciais levantadas pela atividade. O segundo notebook (Time Analysis) faz uma análise temporal das ocorrências, as análises contidas neste notebook são: horária, semanal, por período do dia (dia e noite) e a análise do intervalo entre as ocorrências da mesma categoria. O terceiro notebook (Location Analysis) compreende as análises relacionadas a localidade, nele são calculados os índices de crimes por cidade e por distrito policial, são também levantados os 10 principais tipos de ocorrência em cada localidade. 

## Conclusões

No perfil semanal foi possível perceber questões de sazonalidade como o maior número de ocorrências de roubo e ocorrências relacionadas a drogas durante a semana. Em contraste, existe um maior número de ocorrências de suicidio nos fins de semana. Essas informações podem ajudar no planejamento para garantir um maior nível de patrulhamento durante a semana e manejar funcionários para auxílio psicológico em caso de pessoas com maior tendência para cometer suicidio.

No perfil horário pode-se notar um claramente que as ocorrências relacionadas a drogas ocorrerem no período noturno enquanto os roubos durante o dia.

Em relação as análises que relacionam os crimes com as localidades, isto é, crimes por cidade e crimes por distrito policial, pudemos perceber que o crime de 'Lacerny', que diz respeito a roubo/furto, foi o crime com maior porcentagem de ocorrência em 20 das 32 cidades e em 6 dos 8 distritos.



## Requisitos

- NumPy
- Pandas
- Matploblib
