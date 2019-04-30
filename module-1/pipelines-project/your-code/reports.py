import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns

def report_compare(data, paisA, paisB):
    style.use('seaborn')
    report = data[['Area', 'Continente', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']][(data['Area'] == paisA) | (data['Area'] == paisB)].groupby(['Area']).sum()
    title = 'Comparación {} - {}'.format(paisA, paisB)
    chart = report.T.plot(kind = 'line', title = title, legend = True, figsize=(16,9))
    plt.figure()
    return chart

def report_pais(data, pais, item = 'Honey'):
    style.use('seaborn')
    report = data[['Item', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']][(data['Area'] == pais) & (data['Item'] == item)]
    report = report.set_index('Item')
    title = '{} ({})'.format(pais,item)
    chart = report.T.plot(kind = 'line', title = title, legend = True, figsize=(16,9))
    plt.figure()
    return chart

def produccion_continentes_total(data_total):
    style.use('seaborn')
    total_produccion = data_total.groupby(['Continente']).Total.sum()
    total_produccion.sort_values(ascending = False)
    total_bar = total_produccion.plot(kind = 'bar', rot = 0, title = "Producción por Continentes", legend = True, use_index=True, figsize=(16,9))
    plt.figure()
    return total_bar  

def paises_mayores_productores(data_total_pais):
    style.use('seaborn')
    total = data_total_pais.sort_values(ascending = False)[:5]
    total_bar = total.plot(kind = 'bar', rot = 0, title = "Mayores productores de alimentos para humanos", legend = True, use_index=True, figsize=(16,9))
    plt.figure()
    return total_bar