from numpy import split
import tweepy as tw
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

# loop an string and remain only letters and spaces


def clean_text(text):
        text = text.lower()
        text = ''.join(
            [char for char in text if char in ' abcdefghijklmnopqrstuvwxyz'])
        return text


clean = clean_text('''
                VÍVA 🇵🇦
                ·
                Jan 26
                COMO  # EVALUO LAS #VACUNACIONES DEL COVID POR EL GOBIERNO DE
                Y EL
                LOS CIVILISTA PIDIERON INVASION SE ACABO LA DICTADURA DE NORIEGA. MURIERON PANAMEÑO Y LLEGO LA DEMOCRACIA 2 - LLEGO LA VACUNACION SE REDUJO LOS MUERTOS COMPARE 2021 DE ENERO 2022 DE ENERO
                🏫 Ayuntamiento de Torrejoncillo y Valdencín
                @ AytoTorre
                ·
                Dec 1, 2021
                💉 VACUNACIONES COVID-19 Y GRIPE EN TORREJONCILLO

                🗓️ Viernes 3 de diciembre 2021

                # Torrejoncillo.
                ✍🏼 Debes apuntarte en el Centro de Salud. Solo para vecinos y vecinas de

                👵🏻 Mayores de 70 años que se vacunara antes del día 6 de junio de 2021.

                # NoLoTiresPorLaBorda #Vacunaciones
                Foro Económico Mundial
                @ wef_es
                ·
                Jul 18, 2020
                # vacunaciones durante pandemia de COVID-19
                ONU advierte de peligrosa caída de las
                https: // buff.ly/32m8v04
                ABDELKADER MIMON
                @ arifimimon
                ·
                Apr 20, 2021
                # Melilla siga siendo aún la región española con peores datos #COVID , y q sigamos estando a la cola en #vacunaciones.
                Desolador seguir viendo q a pesar de las sonadas críticas
                # Ceuta con menor cupo d personas a vacunar , y con mejores datos #COVID19 nos adelantan #VacunasCOVID19


                ADERID
                @ ADERID1
                ·
                Jan 11, 2021
                VACUNACIÓN
                ➡️ En estos días, el personal de ADERID está recibiendo la vacuna contra COVID-19.

                ⚠️ Si tenes alguna duda o inquietud, consultá con tu médico.

                # VACUNACONTRACOVID19 #vacunaciones #COVID19 #Covid_19 #vacunacioncovid
                # aderid #generalvillegas #inclusion #Empatia
                ANTONIO ROD
                @ antonioguez60
                ·
                Feb 2, 2021
                Una fuerte  # tormenta de nieve que azota el noreste de Estados Unidos podría ser una de las mayores de la historia en golpear #Nueva York, que decretó el estado de #emergencia y suspendió las #vacunaciones contra el covid-19. /
                Colegio Enfermería Valladolid
                @ EnfValladolid
                ·
                Jun 1, 2021
                # QueNoseTePase #Covid_19
                # Vacunaciones en Valladolid: 👉 https://saludcastillayleon.es/.../lugares.../valladolid
                Consulta el Calendario de
                Consejo de Enfermería de Castilla y León
                @ Consejo_Enf_CyL
                ·
                Jun 15, 2021
                # QueNoseTePase
                Consulta el Calendario de  # Vacunaciones Covid-19 en Castilla y León: 👉 https://saludcastillayleon.es/es/covid-19-poblacion/vacunacion-covid/lugares-vacunacion
                JSE León
                @ JSE_Leon
                ·
                Jul 16, 2021
                # leonesp #Vacunaciones #Covid
                “León vacuna la próxima semana a los nacidos entre 1988 y 1990”
                astorgadigital.com
                León vacuna la próxima semana a los nacidos entre 1988 y 1990
                La vacunación se llevará a cabo los días 19, 20 y 21 de julio
                Treintayseis
                @ treintayseis_36
                ·
                Dec 21, 2021
                # 4 #LoMásVistoDelDía Vacuna Covid: El Sergas comienza a citar a los gallegos de 40 a 49 años para la tercera dosis #Sergas #Vacunaciones #Covid-19 #VacunaCoronavirus
                elespanol.com
                Vacuna Covid: El Sergas comienza a citar a los gallegos de 40 a 49 años para la tercera dosis
                Los ciudadanos en esa franja de edad recibirán un SMS con el día, la hora y el lugar al que podrán acudir para recibir la dosis de refuerzo
                Anna Quero
                @ AnnaQueroN
                ·
                Jan 21
                Abierta  # investigación criminal por las #vacunaciones contra la #Covid en Inglaterra: la policía busca testimonios de afectados - Diario16
                diario16.com
                Abierta investigación criminal por las vacunaciones contra la Covid en Inglaterra: la policía busca...
                Los datos que se están reportando de posibles efectos adversos y fallecidos que podrían tener como causa la inoculación de las inyecciones contra la covid
                El Día de Córdoba
                @ eldiacordoba
                ·
                Dec 13, 2021
                # Andalucía ya pueden pedir cita para que reciban la primera dosis contra la #covid: las #vacunaciones serán por la tarde
                💉  Los padres de niños de entre 9 y 11 años de
                eldiadecordoba.es
                Andalucía permite ya pedir cita para la vacunación de niños de hasta 9 años
                La primera remesa de 260.000 vacunas Pfizer da para vacunar hasta los nueve años antes de Navidad Andalucía administra 178.000 vacunas en la última semana, 153.000 de ellas para terceras dosis
                Treintayseis
                @ treintayseis_36
                ·
                Jul 3, 2021 ''')


def open_file(path: str) -> str:
    content = ""
    with open(path, "r") as f:
        content = f.readlines()
    return " ".join(content)

wordcloud = WordCloud(
    background_color="white", min_font_size=5
).generate(clean)

# print(all_words)
# plot the WordCloud image
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.savefig('Graphics/p10_TextAnalysis.png')
plt.close()


# def wordcloud():


# # {
# #   "serviceId": "b06c3cd1-d95d-4a1f-a215-0b19bfc38891",
# #   "input": {
# #     "username": "garyvee",
# #     "background_color": "#1DA1F2",
# #     "shape": "Twitter"
# #   }
# # }
