from wrangle import Serie

# Importando dados das features e target
print("Importando Variáveis...")

feature = Serie()

igpm = feature.get_BCB(189)
credito_pib = feature.get_BCB(20622)
div_liq = feature.get_BCB(4536)
pib = feature.get_pib("http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=521274780&module=M")
find11 = feature.get_yahoo("FIND11.SA", '2000-01-01')

igpm.columns = ["IGP"]
credito_pib.columns = ["CRED/PIB"]
div_liq.columns = ["DIV_LIQ"]

# Unindo dataframes
print("Consolidando Base de Dados...")

df = feature.merge([igpm, credito_pib, div_liq, pib, find11])

# Tratamento dos Dados
print("Tratando dados...")



print("Processo finalizado")

