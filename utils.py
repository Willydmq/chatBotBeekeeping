import csv
import os
import pickle
import re

import docx2txt
import es_core_news_sm
import jellyfish
import nltk
import pandas as pd
import PyPDF2
import spacy
import torch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
from transformers import BertForSequenceClassification, BertTokenizer

nltk.download("wordnet")
nltk.download("punkt")
nlp = spacy.load("es_core_news_sm")
nlp = es_core_news_sm.load()

terminaciones = ["es", "me", "as", "ste", "te"]
excluir = ["me", "se", "ser", "estar", "estas"]
ends = ("rte", "a")


def models():
    global lista_verbos
    global ruta
    global ruta_modelo
    global verbos_irregulares
    global txt_folder_path

    lista_verbos = pickle.load(open("./data/verbos/lista_verbos.pickle", "rb"))

    verbos_irregulares = pickle.load(
        open("./data/verbos/verbos_irregulares.pickle", "rb")
    )

    ruta = "./data/dialogos"

    ruta_modelo = "./models"

    txt_folder_path = "./data/documentos"

    return lista_verbos, ruta, ruta_modelo, verbos_irregulares, txt_folder_path


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
    frase_tratada = re.sub(r"[^\w\s+\-*/?¡¿!]", "", frase_tratada)
    frase_tratada = re.sub(r"\s+", " ", frase_tratada)
    frase_tratada = frase_tratada.replace("á", "a")
    frase_tratada = frase_tratada.replace("é", "e")
    frase_tratada = frase_tratada.replace("í", "i")
    frase_tratada = frase_tratada.replace("ó", "o")
    frase_tratada = frase_tratada.replace("ú", "u")

    # Estandarización de nombres propios
    nombres_propios = ["alejandro", "maria", "juan", "luis"]

    for nombre in nombres_propios:
        frase_tratada = re.sub(
            rf"\b{nombre}\b", nombre.capitalize(), frase_tratada, flags=re.IGNORECASE
        )

    return frase_tratada


def reemplazar_terminacion(palabra):
    if palabra in excluir:
        return palabra

    if len(palabra) < 2:
        return palabra

    if palabra.endswith("rte"):
        return palabra
    if palabra.endswith("a"):
        return palabra

    for t in terminaciones:
        if palabra.endswith(t):
            if not palabra.endswith("aeiouáéíóúü"):
                return palabra[: -len(t)] + "r"

    return palabra


# ------------- TOKENS --------------#


def revisar_tokens(texto, tokens):
    texto = tratamiento_texto(texto)
    if len(tokens) == 0:
        if any(name in texto for name in ["cientifico de datos", "data scientist"]):
            tokens.append("datascientist")
        if any(
            name in texto
            for name in ["elprofealejo", "el profe alejo", "profe alejo", "profealejo"]
        ):
            tokens.append("elprofealejo")
        if any(name in texto for name in ["ciencia de datos", "data science"]):
            tokens.append("datascience")
        if any(name in texto for name in ["apicultura", "apicola"]):
            tokens.append("beekeeping")
    else:
        elementos_a_eliminar = ["cual", "que", "quien", "cuanto", "cuando", "como"]
        if "hablame" in texto and "hablar" in tokens:
            elementos_a_eliminar.append("hablar")
        elif "cuentame" in texto and "contar" in tokens:
            elementos_a_eliminar.append("contar")
        elif "hago" in texto and "hacer" in tokens:
            elementos_a_eliminar.append("hacer")
        elif "entiendes" in texto and "entender" in tokens:
            elementos_a_eliminar.append("entender")
        elif "sabes" in texto and "saber" in tokens:
            elementos_a_eliminar.append("saber")
        tokens = [token for token in tokens if token not in elementos_a_eliminar]
    return tokens


# def normalizar(frase):
#     lemmas = []
#     palabras = frase.split()

#     for palabra in palabras:
#         raiz_palabra = raiz(palabra)
#         texto_tratado = tratamiento_texto(raiz_palabra)
#         reemplazo_palabra = reemplazar_terminacion(texto_tratado)

#         doc = nlp(reemplazo_palabra)

#         for token in doc:
#             lemmas.append(token.lemma_)

#     return lemmas


def normalizar(texto):
    tokens = []
    tokens = revisar_tokens(texto, tokens)
    doc = nlp(texto)
    for t in doc:
        # Obtener el lemma
        lemma = verbos_irregulares.get(t.text, t.lemma_)

        # Verificar si lemma es una cadena no vacía
        if lemma and isinstance(lemma, str):
            lemma = re.sub(r"[^\w\s+\-*/]", "", lemma)

            if (
                t.pos_
                in (
                    "VERB",
                    "PROPN",
                    "PRON",
                    "NOUN",
                    "AUX",
                    "SCONJ",
                    "ADJ",
                    "ADV",
                    "NUM",
                )
                or lemma in lista_verbos
            ):
                if t.pos_ == "VERB":
                    lemma = reemplazar_terminacion(lemma)
                    tokens.append(raiz(tratamiento_texto(lemma)))
                else:
                    tokens.append(tratamiento_texto(lemma))

    # Aplicar el lematizador
    tokens = [nltk.WordNetLemmatizer().lemmatize(palabra) for palabra in tokens]

    tokens = list(dict.fromkeys(tokens))
    tokens = list(filter(None, tokens))
    tokens = revisar_tokens(texto, tokens)
    tokens_str = str(tokens)
    return tokens_str


# ------------- CARGAR DATA --------------#


lista_dialogos = []
lista_dialogos_respuesta = []
lista_tipo_dialogo = []

for archivo in os.listdir(ruta):
    if archivo.endswith(".txt"):
        tipo = archivo.split(".")[0]

        with open(os.path.join(ruta, archivo)) as f:
            lineas = f.readlines()

            for i in range(0, len(lineas), 2):
                pregunta = lineas[i].strip()
                pregunta = re.sub(r"[^\w\s+\-*/]", "", pregunta)
                pregunta = tratamiento_texto(pregunta)
                lista_dialogos.append(pregunta)

                respuesta = lineas[i + 1].strip()
                lista_dialogos_respuesta.append(respuesta)

                lista_tipo_dialogo.append(tipo)


datos = {
    "dialogo": lista_dialogos,
    "respuesta": lista_dialogos_respuesta,
    "tipo": lista_tipo_dialogo,
    "interseccion": pd.Series([0] * len(lista_dialogos), dtype=float),
    "jaro_winkler": pd.Series([0] * len(lista_dialogos), dtype=float),
    "probabilidad": pd.Series([0] * len(lista_dialogos), dtype=float),
}

df_dialogo = pd.DataFrame(datos)

df_dialogo = df_dialogo.drop_duplicates(keep="first")
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

    user_response = re.sub(r"[^\w\s+\-*/?¡¿!]", "", user_response)
    df = df_dialogo.copy()
    for idx, row in df.iterrows():
        df.at[idx, "interseccion"] = interseccion(user_response, row["dialogo"])
        df.at[idx, "similarity"] = similarity(user_response, row["dialogo"])
        df.at[idx, "jaro_winkler"] = jaro_winkler(user_response, row["dialogo"])
        df.at[idx, "probabilidad"] = max(
            df.at[idx, "interseccion"],
            df.at[idx, "similarity"],
            df.at[idx, "jaro_winkler"],
        )
    df.sort_values(by=["probabilidad", "jaro_winkler"], inplace=True, ascending=False)
    probabilidad = df["probabilidad"].head(1).values[0]
    if probabilidad >= 0.92:
        print(
            "Respuesta encontrada por el método de comparación de textos - Probabilidad: ",
            probabilidad,
        )
        respuesta = df["respuesta"].head(1).values[0]
    else:
        respuesta = ""

    return respuesta


# ------------- NORMALIZANDO LAS FRASES --------------#


label_encoder = LabelEncoder()
df_dialogo["palabras"] = df_dialogo["dialogo"].apply(lambda x: " ".join(normalizar(x)))
df_dialogo["tipo_num"] = label_encoder.fit_transform(df_dialogo["tipo"])
df_dialogo = df_dialogo[df_dialogo.palabras.values != ""]

# Imprimir diccionario
relacion_diccionario = {}

# Iterar sobre las filas del DataFrame
for tipo, tipo_num in zip(df_dialogo["tipo"], df_dialogo["tipo_num"]):
    relacion_diccionario[tipo_num] = tipo


# ------------- MACHINE LEARNING --------------#

Modelo_TF = BertForSequenceClassification.from_pretrained(ruta_modelo)
tokenizer_TF = BertTokenizer.from_pretrained(ruta_modelo)


def clase_encontrada(frase):
    palabra = " ".join(normalizar(frase))

    # Realizar la predicción con el modelo
    tokens = tokenizer_TF.encode_plus(
        frase,
        add_special_tokens=True,
        max_length=128,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )

    input_ids = tokens["input_ids"]
    attention_mask = tokens["attention_mask"]

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
    df = df_dialogo[df_dialogo["tipo"] == clase_encontrada1]
    df.reset_index(inplace=True)
    vectorizer = TfidfVectorizer()
    dialogos_num = vectorizer.fit_transform(df["dialogo"])
    pregunta_num = vectorizer.transform([tratamiento_texto(pregunta)])
    similarity_scores = cosine_similarity(dialogos_num, pregunta_num)
    indice_pregunta_proxima = similarity_scores.argmax()

    if max(similarity_scores) > 0.5 and clase_encontrada1 not in ["Otros"]:
        print(
            "Respuesta encontrada por el modelo Transformers - tipo:", clase_encontrada1
        )
        respuesta = df["respuesta"][indice_pregunta_proxima]
    else:
        respuesta = ""
    return respuesta


# ------------- RESPUESTA DOCUMENTO --------------#


# Importando bases csv
lista_documentos = [x for x in os.listdir(txt_folder_path) if x.endswith(".csv")]
documento_csv = ""
for i in range(len(lista_documentos)):
    with open(
        txt_folder_path + "/" + lista_documentos[i], "r", encoding="utf-8"
    ) as csv_txt:
        csv_text = csv.reader(csv_txt)
        for fila in csv_text:
            if fila[-1] != "frase":
                documento_csv += fila[-1]


# DOCX
lista_documentos = [x for x in os.listdir(txt_folder_path) if x.endswith(".docx")]
documento_docx = ""
for i in range(len(lista_documentos)):
    texto = docx2txt.process(txt_folder_path + "/" + lista_documentos[i])

    documento_docx += texto.replace("*", "\n\n*") + "\n"


# TXT
lista_documentos = [x for x in os.listdir(txt_folder_path) if x.endswith(".txt")]
documento_txt = ""
for i in range(len(lista_documentos)):
    with open(
        txt_folder_path + "/" + lista_documentos[i], "r", encoding="utf-8"
    ) as txt:
        txt_new = txt.read()
        for i in txt_new:
            documento_txt += i


# Lista de documentos PDF
lista_documentos = [x for x in os.listdir(txt_folder_path) if x.endswith(".pdf")]

documento_pdf = ""

for documento in lista_documentos:
    with open(os.path.join(txt_folder_path, documento), "rb") as f:
        reader = PyPDF2.PdfReader(f)

        for page in reader.pages:
            documento_pdf += page.extract_text()


documento = documento_csv + documento_txt + documento_docx + documento_pdf
lista_frases = nltk.sent_tokenize(documento, "spanish")
lista_frases_normalizadas = [" ".join(normalizar(x)) for x in lista_frases]


# Función para devolver la respuesta de los documentos
def respuesta_documento(pregunta):
    pregunta = normalizar(pregunta)

    def contar_coincidencias(frase):
        return sum(1 for elemento in pregunta if elemento in frase)

    diccionario = {
        valor: posicion for posicion, valor in enumerate(lista_frases_normalizadas)
    }
    lista = sorted(list(diccionario.keys()), key=contar_coincidencias, reverse=True)[
        :100
    ]
    # Hasta aqui ya tengo mi lista con las 6 respuestas con mayor coincidencia de tokens
    # Convierte la pregunta en frase
    lista.append("".join(pregunta))

    TfidfVec = TfidfVectorizer(tokenizer=normalizar)
    tfidf = TfidfVec.fit_transform(lista)

    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = round(flat[-2], 2)
    if req_tfidf >= 0.22:
        print(
            "Respuesta encontrada por el método TfidfVectorizer - Probabilidad:",
            req_tfidf,
        )
        respuesta = lista_frases[diccionario[lista[idx]]]
    else:
        respuesta = ""
    return respuesta


# ------------- BUSCAR RESPUESTA --------------#


def procesar_pregunta(pregunta):
    # código de clasificación y búsqueda de respuesta
    respuesta_df_dialogo = dialogo(pregunta)
    if respuesta_df_dialogo != "":
        return respuesta_df_dialogo

    respuesta_modelo = clasificacion_modelo(pregunta)
    if respuesta_modelo != "":
        return respuesta_modelo

    respuesta_document = respuesta_documento(pregunta)
    if respuesta != "":
        return respuesta_document

    else:
        return "Respuesta no encontrada"
