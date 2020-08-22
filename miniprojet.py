import pandas as pd
import _thread
import threading

# print("I. 1. Lire le fichier et le stocker dans un dataframe")
covid_data = pd.read_csv("owid-covid-data.csv",header=0)

print(" I. 2. affichage du schema")
print(covid_data)

# print(" I. 3. affichage du nombre d'enregistrements")
# print(covid_data.shape[0])

# print(" I. 4. affichage du nombre de pays differents")
# print(covid_data.groupby('location').nunique().shape[0])

# print(" I. 5. affichage du nombre de continents differents")
# print(covid_data.groupby('continent').nunique().shape[0])


# print(" II. 1. affichage du nombre de cas par pays")
# print(covid_data.groupby('location')['total_cases'].sum())


# print(" II. 2. affichage du plus grand nombre de nouveaux cas par pays")
# print(covid_data.groupby('location')['new_cases'].max())




#print(" II. 3. affichage nombre de cas par contininent avec des threads")
# def cas_au_31_juillet(continent):
#     print("thread for %s Starting" % (continent,))
#     print("\n")
#     print(covid_data[(covid_data['date'] == '2020-03-29') & (covid_data['continent'] == continent)].groupby('continent')['total_cases'].sum())
#     print("\n")


# tAsia = threading.Thread(target=cas_au_31_juillet, args=('Asia',))
# tAsia.start()

# tOceania = threading.Thread(target=cas_au_31_juillet, args=('Oceania',))
# tOceania.start()

# tEurope = threading.Thread(target=cas_au_31_juillet, args=('Europe',))
# tEurope.start()

# tAfrica = threading.Thread(target=cas_au_31_juillet, args=('Africa',))
# tAfrica.start()

# tNorthAmerica = threading.Thread(target=cas_au_31_juillet, args=('North America',))
# tNorthAmerica.start()

# tSouthAmerica = threading.Thread(target=cas_au_31_juillet, args=('South America',))
# tSouthAmerica.start()


# print(" II. 4. affichage de la date du plus grand nombre de nouveaux cas par pays")
# print(covid_data[covid_data.groupby(['location'])['new_cases'].transform(max) == covid_data['new_cases']][['date','location','new_cases']])

# print(" II. 5. affichage des 10 pays avec le plus grand ratio population/nombre au  31 juillet 2020")
# covid_data['ratioNombreCas'] = covid_data['total_cases']/covid_data['population']
# print(covid_data[(covid_data['date'] == '2020-07-31')].sort_values(by='ratioNombreCas', ascending=False).head(10))

# print(" II. 6. affichage des 10 pays les dix pays qui ont enregistré le plus grand ratio de morts (population/nombre total de morts au  31 juillet 2020)")
# covid_data['ratioMorts'] = covid_data['total_deaths']/covid_data['population']
# print(covid_data[(covid_data['date'] == '2020-07-31')].sort_values(by='ratioMorts', ascending=False).head(10))


# print(" II. 7. Pensez-vous que ce facteur (calculé au 6.) est lié au hospital_beds_per_thousand,ou au population_density? pourquoi?")

# print("III. 1. Dresser un tableau (dataframe) de 6 colonnes")
# new_columns = ['date', 'le nombre de nouveaux morts', 'le nombre de nouveaux cas à J-10',
#     'le nombre de nouveaux cas à J-15', 'le nombre de nouveaux cas à J-20', 'le nombre de nouveaux cas à J-25'
# ]

# df2 = covid_data[['date', 'new_deaths', covid_data[covid_data['date'] == '2020-07-20']['new_deaths'], 'new_deaths', 'new_deaths', 'new_deaths']].copy()

# # df2[new_columns] = covid_data[['date', 'new_deaths', 'new_deaths', 'new_deaths', 'new_deaths', 'new_deaths']]

# print(df2)

