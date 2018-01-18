#converte uma data qualquer em um dia da semana

import datetime
print datetime.datetime.strptime('01/11/2010', '%M/%d/%Y').strftime('%A')
