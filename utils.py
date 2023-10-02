import os
import pickle
import re

import es_core_news_sm
import jellyfish
import pandas as pd
import spacy
import torch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
from transformers import BertForSequenceClassification, BertTokenizer

nlp = spacy.load("es_core_news_sm")
nlp = es_core_news_sm.load()

terminaciones = ['es', 'me', 'as', 'ste', 'te']
excluir = ['me', 'se', 'ser', 'estar', 'estas']
ends = ('rte', 'a')


def models():

    global lista_verbos
    global ruta
    global ruta_modelo

    lista_verbos = pickle.load(open(
        "./data/verbos/lista_verbos.pickle", "rb"))

    ruta = "./data/dialogos"

    ruta_modelo = "./models"

    return lista_verbos, ruta, ruta_modelo


models()

# ------------- TRATAMIENTO DE DATOS--------------#


def raiz(palabra):

    max_sim = 0
    raiz_candidata = ""

    for verbo in lista_verbos:
        sim = jellyfish.jaro_winkler(palabra, verbo)

        if sim > max_sim:
            max_sim = sim
            raiz_candidata = verbo

    if max_sim >= 0.93:
        return raiz_candidata
    else:
        return palabra


def tratamiento_texto(frase):

    frase_tratada = frase.lower()

    # Limpieza y normalización
    frase_tratada = re.sub(r'[^\w\s+\-*/?¡¿!]', '', frase_tratada)
    frase_tratada = re.sub(r'\s+', ' ', frase_tratada)
    frase_tratada = frase_tratada.replace("á", "a")
    frase_tratada = frase_tratada.replace("é", "e")
    frase_tratada = frase_tratada.replace("í", "i")
    frase_tratada = frase_tratada.replace("ó", "o")
    frase_tratada = frase_tratada.replace("ú", "u")

    # Estandarización de nombres propios
    nombres_propios = ['alejandro', 'maria', 'juan', 'luis']

    for nombre in nombres_propios:
        frase_tratada = re.sub(
            rf'\b{nombre}\b', nombre.capitalize(), frase_tratada, flags=re.IGNORECASE)

    return frase_tratada


def reemplazar_terminacion(palabra):

    if palabra in excluir:
        return palabra

    if len(palabra) < 2:
        return palabra

    if palabra.endswith('rte'):
        return palabra
    if palabra.endswith('a'):
        return palabra

    for t in terminaciones:
        if palabra.endswith(t):
            if not palabra.endswith(u'aeiouáéíóúü'):
                return palabra[:-len(t)] + 'r'

    return palabra


def normalizar(frase):
    lemmas = []
    palabras = frase.split()

    for palabra in palabras:
        raiz_palabra = raiz(palabra)
        texto_tratado = tratamiento_texto(raiz_palabra)
        reemplazo_palabra = reemplazar_terminacion(texto_tratado)

        doc = nlp(reemplazo_palabra)

        for token in doc:
            lemmas.append(token.lemma_)

    return lemmas

# ------------- CARGAR DATA --------------#


lista_dialogos = []
lista_dialogos_respuesta = []
lista_tipo_dialogo = []

for archivo in os.listdir(ruta):

    if archivo.endswith('.txt'):

        tipo = archivo.split('.')[0]

        with open(os.path.join(ruta, archivo)) as f:
            lineas = f.readlines()

            for i in range(0, len(lineas), 2):

                pregunta = lineas[i].strip()
                pregunta = re.sub(r"[^\w\s+\-*/]", '', pregunta)
                pregunta = tratamiento_texto(pregunta)
                lista_dialogos.append(pregunta)

                respuesta = lineas[i+1].strip()
                lista_dialogos_respuesta.append(respuesta)

                lista_tipo_dialogo.append(tipo)


datos = {'dialogo': lista_dialogos,
         'respuesta': lista_dialogos_respuesta,
         'tipo': lista_tipo_dialogo,
         'interseccion': pd.Series([0] * len(lista_dialogos), dtype=float),
         'jaro_winkler': pd.Series([0] * len(lista_dialogos), dtype=float),
         'probabilidad': pd.Series([0] * len(lista_dialogos), dtype=float)
         }

df_dialogo = pd.DataFrame(datos)

df_dialogo = df_dialogo.drop_duplicates(keep='first')
df_dialogo.reset_index(drop=True, inplace=True)


# ------------- COMPARACION DE TEXTOS --------------#


def interseccion(texto1, texto2):
    palabras1 = set(texto1.split())
    palabras2 = set(texto2.split())

    if len(palabras1) == 0:
        return 0
    else:
        interseccion = palabras1 & palabras2
        return len(interseccion) / len(palabras1)


def similarity(texto1, texto2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([texto1, texto2])
    return cosine_similarity(vectors)[0][1]


def jaro_winkler(texto1, texto2):
    return jellyfish.jaro_winkler(texto1, texto2)


def dialogo(user_response):
    user_response = tratamiento_texto(user_response)

    user_response = re.sub(r"[^\w\s+\-*/?¡¿!]", '', user_response)
    df = df_dialogo.copy()
    for idx, row in df.iterrows():
        df.at[idx, 'interseccion'] = interseccion(
            user_response, row['dialogo'])
        df.at[idx, 'similarity'] = similarity(user_response, row['dialogo'])
        df.at[idx, 'jaro_winkler'] = jaro_winkler(
            user_response, row['dialogo'])
        df.at[idx, 'probabilidad'] = max(
            df.at[idx, 'interseccion'], df.at[idx, 'similarity'], df.at[idx, 'jaro_winkler'])
    df.sort_values(by=['probabilidad', 'jaro_winkler'],
                   inplace=True, ascending=False)
    probabilidad = df['probabilidad'].head(1).values[0]
    if probabilidad >= 0.92:
        print('Respuesta encontrada por el método de comparación de textos - Probabilidad: ', probabilidad)
        respuesta = df['respuesta'].head(1).values[0]
    else:
        respuesta = ''

    return respuesta

# ------------- NORMALIZANDO LAS FRASES --------------#


label_encoder = LabelEncoder()
df_dialogo['palabras'] = df_dialogo['dialogo'].apply(
    lambda x: ' '.join(normalizar(x)))
df_dialogo['tipo_num'] = label_encoder.fit_transform(df_dialogo['tipo'])
df_dialogo = df_dialogo[df_dialogo.palabras.values != '']

# Imprimir diccionario
relacion_diccionario = {}

# Iterar sobre las filas del DataFrame
for tipo, tipo_num in zip(df_dialogo['tipo'], df_dialogo['tipo_num']):
    relacion_diccionario[tipo_num] = tipo


# ------------- MACHINE LEARNING --------------#

Modelo_TF = BertForSequenceClassification.from_pretrained(ruta_modelo)
tokenizer_TF = BertTokenizer.from_pretrained(ruta_modelo)


def clase_encontrada(frase):
    palabra = ' '.join(normalizar(frase))

    # Realizar la predicción con el modelo
    tokens = tokenizer_TF.encode_plus(
        frase,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    input_ids = tokens['input_ids']
    attention_mask = tokens['attention_mask']

    with torch.no_grad():
        outputs = Modelo_TF(input_ids, attention_mask)

    etiquetas_predichas = torch.argmax(outputs.logits, dim=1)
    etiquetas_decodificadas = etiquetas_predichas.tolist()

    llave_buscada = etiquetas_decodificadas[0]
    clase_encontrada = relacion_diccionario[llave_buscada]

    return clase_encontrada


def clasificacion_modelo(pregunta):

    clase_encontrada1 = clase_encontrada(pregunta)

    # Buscar respuesta más parecida en la clase encontrada
    df = df_dialogo[df_dialogo['tipo'] == clase_encontrada1]
    df.reset_index(inplace=True)
    vectorizer = TfidfVectorizer()
    dialogos_num = vectorizer.fit_transform(df['dialogo'])
    pregunta_num = vectorizer.transform([tratamiento_texto(pregunta)])
    similarity_scores = cosine_similarity(dialogos_num, pregunta_num)
    indice_pregunta_proxima = similarity_scores.argmax()

    if max(similarity_scores) > 0.5 and clase_encontrada1 not in ['Otros']:
        print('Respuesta encontrada por el modelo Transformers - tipo:',
              clase_encontrada1)
        respuesta = df['respuesta'][indice_pregunta_proxima]
    else:
        respuesta = ''
    return respuesta


# ------------- BUSCAR RESPUESTA --------------#

def procesar_pregunta(pregunta):
    # código de clasificación y búsqueda de respuesta
    respuesta_modelo = clasificacion_modelo(pregunta)

    if respuesta_modelo != '':
        return respuesta_modelo

    respuesta_df_dialogo = dialogo(pregunta)

    if respuesta_df_dialogo != '':
        return respuesta_df_dialogo
    else:
        return 'Respuesta no encontrada'
