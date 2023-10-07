<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/chatbot.png" width="50px">
    <a style="color: blue; font-size: 20px; display: block; text-align: center;" href="https://gitlab.com/Willydmq/chatbot.git" target="_blank">Repositorio ChatBot Beekeeping</a>
</div>
<br />
<br />
<br />
<div>
  <div style="text-align: center; padding: 10px; display:flex flex-direction:column">
      <h1 style="font-size:25px; text-decoration-line: underline;">Version Escritorio 💻</h1>
      <div style="display:flex; flex-wrap: wrap; gap:5px; justify-content: center;">
      <img src="/images/v_escritorio.png" width="500px">
      </div>
      <h1 style="font-size:25px; text-decoration-line: underline;">Version Mobile 📱</h1>
      <div style="display:flex; flex-wrap: wrap; gap:5px; justify-content: center;">
      <img src="/images/v_mobile.png" width="200px" height="250px">    
  </div>
</div>

#1. Configuración del ambiente

Para empezar, deberás subir los archivos del proyecto a tu Google Drive, y desde allí, abrir el notebook **Chatbot_Inteligente_Alura_Sprint1**. En el primer paso necesitarás conectar tu Entorno de Google Colaboratory con tu Google Drive e instalar algunas bibliotecas necesarias para el proyecto.

Link:
<span
  data-path="https://caelum-online-public.s3.amazonaws.com/alura-latam-challenges/challenge-data-science-chatbox/Chatbot.zip">
<a>
<span>https://caelum-online-public.s3.amazonaws.com/alura-latam-challenges/challenge-data-science-chatbox/Chatbot.zip</span>
</a>
</span>

Para estar seguros de que tenemos todo listo y organizado en nuestro Ambiente de trabajo, compáralo con la siguiente imagen:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image.png">
</div>

El resultado debería ser las carpetas y sus respectivos archivos que tenemos en Google Drive, recuerda que la cuenta de gmail utilizada en Google Colab debe ser la misma a la cuenta usada en Google Drive, no te preocupes, esto es todo lo que debemos hacer en este paso.

#2. Importar Verbos

##Descripción

Utilizando la biblioteca `pickle` deberás importar cada uno de los siguientes archivos de verbos en las siguientes variables del proyecto:

```
`/verbos/lista_verbos.pickle` → lista_verbos

`/verbos/lista_verbos.pickle` → lista_verbos

`/verbos/verbos_irregulares.pickle` → verbos_irregulares
```

El resultado esperado es el siguiente:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image1.png">
</div>

##Resultado

```python
import pickle

# Importar el archivo de lista de verbos
with open("/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/Chatbot/verbos/lista_verbos.pickle", "rb") as f:
  lista_verbos = pickle.load(f)

# Importar el archivo de verbos irregulares
with open("/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/Chatbot/verbos/verbos_irregulares.pickle", "rb") as f:
  verbos_irregulares = pickle.load(f)

```

```python
print(lista_verbos)
```

    ['parar', 'recomendar', 'cancelar', 'fanatizar', 'amaran o amasen', 'exponer', 'obedecer', 'quejar', 'echar', 'legitimar', 'perjudicar', 'organizar', 'molar', 'objetar', 'considerar', 'golear', 'mover', 'acertar', 'reunir', 'regir', 'ilusionar', 'simpatizar', 'conjeturar', 'helar', 'quitar', 'amariamos', 'destacar', 'llegar', 'sincronizar', 'lesionar', 'seducir', 'asistir', 'conservar', 'acordar', 'salvar', 'relucir', 'graduar', 'forzar', 'dar', 'deplorar', 'batear', 'mofar', 'estropear', 'aplastar', 'wasapeo', 'gestionar', 'suprimir', 'gruñir', 'progresar', 'suscribir', 'noticiar', 'cavar', 'alejar', 'galopar', 'virar', 'medir', 'actualizar', 'humanizar', 'convivir', 'gratificar', 'digerir', 'tocar', 'zonificar', 'amariais', 'aterrizar', 'hojear', 'cometer', 'sufrir', 'reciclar', 'obturar', 'divertir', 'ondear', 'listar', 'determinar', 'alentar', 'sumar', 'reflexionar', 'ames', 'anotar', 'mitificar', 'escribir', 'ilustrar', 'obtener', 'subir', 'socorrer', 'desprender', 'agregar', 'gandulear', 'improvisar', 'traquetear', 'idealizar', 'pescar', 'despertarse', 'decorar', 'ceñir', 'asar', 'balbucear', 'noquear', 'amaremos', 'desconectar', 'tambalear', 'vengar', 'bolear', 'trabar', 'resplandecer', 'vagar', 'pasmar', 'susurrar', 'amamos', 'suceder', 'pelar', 'toser', 'preocupar', 'martillar', 'zarpar', 'repartir', 'costar', 'llenar', 'contradecir', 'trasplantar', 'embrujar', 'exonerar', 'wasapearia', 'fabular', 'alquilar', 'capturar', 'granular', 'instruir', 'roer', 'ufanarse', 'filtrar', 'pulsar', 'proporcionar', 'fijar', 'fallar', 'identificar', 'mermar', 'agradar', 'arder', 'desmerecer', 'arquear', 'desquitar', 'contar', 'pesar', 'rendir', 'exfoliar', 'gritar', 'hartar', 'pegar', 'irrumpir', 'resaltar', 'lagrimear', 'filosofar', 'perdonar', 'defender', 'zaherir', 'corromper', 'girar', 'titular', 'guadañar', 'evadir', 'traspasar', 'homenajear', 'dominar', 'variar', 'disminuir', 'wasapea', 'querellar', 'tiritar', 'excavar', 'opinar', 'comentar', 'prohibir', 'repasar', 'vislumbrar', 'alegrar', 'fotografiar', 'mosquear', 'hechizar', 'nadar', 'hastiar', 'recluyen', 'galvanizar', 'planificar', 'fisurar', 'fluctuar', 'comenzar', 'recrudecer', 'exagerar', 'colonizar', 'calcular', 'exterminar', 'desayunar', 'lamer', 'fluir', 'invadir', 'encantar', 'combinar', 'apagar', 'televisar', 'probar', 'aconsejar', 'necesitar', 'disparar', 'manejar', 'oxidar', 'devenir', 'ostentar', 'bucear', 'bautizar', 'moler', 'reir', 'crujir', 'shockear', 'nosotros', 'empezar', 'compensar', 'estatizar', 'alumbrar', 'formalizar', 'imaginar', 'construir', 'disuadir', 'iluminar', 'condimentar', 'estrenar', 'originar', 'abastecer', 'prolongar', 'usurar', 'inhalar', 'declinar', 'ensuciar', 'humillar', 'examinar', 'exteriorizar', 'amare', 'gobernar', 'tramar', 'oscilar', 'huir', 'esperar', 'infringir', 'predecir', 'wasapearian', 'alimentar', 'creer', 'niñear', 'zaparrastrar', 'quebrar', 'wasapeareis', 'almorzar', 'expresar', 'asentir', 'resolver', 'bailar', 'chocar', 'deprimir', 'obsequiar', 'sobrar', 'fluye', 'arañar', 'redimir', 'justiciar', 'acusar', 'robar', 'amaramos o amasemos', 'quemar', 'urdir', 'enamorarse', 'ocultar', 'salir', 'fantasear', 'ovacionar', 'apoyar', 'construyo', 'pedalear', 'galantear', 'lacrar', 'wasapearais o wasapeaseis', 'wasapeen', 'disentir', 'envejecer', 'radiar', 'asfixiar', 'bromear', 'amar', 'masacrar', 'representar', 'proclamar', 'alterar', 'incluyeran', 'inscribir', 'aligerar', 'querer', 'vapulear', 'traer', 'heredar', 'tararear', 'oscurecer', 'disminuyen', 'nutrir', 'oficializar', 'guiar', 'traducir', 'escoger', 'descarrilar', 'colorear', 'luchar', 'wasapeamos', 'ama', 'resarcir', 'convidar', 'liar', 'narrar', 'desconocer', 'ameis', 'protagonizar', 'refrescar', 'doblar', 'montar', 'ensayar', 'comer', 'obrar', 'fruncir', 'marinar', 'subrayar', 'replicar', 'teclear', 'auxiliar', 'litigar', 'sobrevivir', 'obstruir', 'vibrar', 'hablar', 'embestir', 'merendar', 'refutar', 'dirigir', 'hacinar', 'aspirar', 'propagar', 'sobreseer', 'educar', 'centrar', 'extender', 'redistribuya', 'plantar', 'aprobar', 'practicar', 'alarmar', 'bordar', 'instrumentar', 'universalizar', 'desteñir', 'glosar', 'magnificar', 'urgir', 'procurar', 'rebatir', 'quedar', 'razonar', 'macanear', 'renacer', 'repeler', 'fundir', 'rugir', 'subyacer', 'datar', 'incidir', 'frenar', 'negociar', 'definir', 'estallar', 'preexistir', 'turnar', 'caber', 'tranquilizar', 'disolver', 'localizar', 'varar', 'refaccionar', 'chupar', 'programar', 'zigzaguear', 'lookear', 'concluir', 'grisear', 'dividir', 'violentar', 'brincar', 'alborotar', 'dictar', 'casar', 'linchar', 'tricotar', 'temer', 'novelar', 'kickear', 'urbanizar', 'partir', 'mensurar', 'diferenciar', 'emancipar', 'wasapeasteis', 'aburrir', 'sacudir', 'confundir', 'añorar', 'constituyeran', 'ignorar', 'judicializar', 'solicitar', 'nasalizar', 'escuchar', 'desistir', 'esquiar', 'orar', 'cayo', 'bracear', 'herrumbrar', 'wasapean', 'destituyeron', 'trastornar', 'blindar', 'adquirir', 'distribuir', 'balancear', 'wasapeariais', 'instituyo', 'disimular', 'oxigenar', 'testimoniar', 'entusiasmar', 'desmentir', 'fragmentar', 'exhortar', 'felicitar', 'condicionar', 'vacunar', 'encontrar', 'mudar', 'mostrar', 'afilar', 'armar', 'concluyeron', 'mancillar', 'explotar', 'bajar', 'lacerar', 'chatear', 'diseñar', 'valuar', 'mecer', 'adorar', 'exigir', 'birlar', 'suplir', 'prevenir', 'registrar', 'terminar', 'jugar', 'aguardar', 'obviar', 'ellos', 'salar', 'higienizar', 'gatear', 'jerarquizar', 'presentar', 'yerran', 'hibernar', 'venir', 'clavar', 'olvidar', 'gimotear', 'asquear', 'roncar', 'wasapeariamos', 'resultar', 'vaciar', 'languidecer', 'intuyo', 'laquear', 'comprometer', 'enganchar', 'enquistar', 'entrar', 'nominar', 'impregnar', 'mutilar', 'fusilar', 'paralizar', 'tramitar', 'latir', 'vociferar', 'andar', 'arrojar', 'espirar', 'redactar', 'hornear', 'adornar', 'wasapeabas', 'ordenar', 'habilitar', 'prender', 'comerciar', 'transcribir', 'saciar', 'comunicar', 'maldecir', 'conectar', 'juntar', 'anexar', 'impresionar', 'conducir', 'cerrar', 'murmurar', 'firmar', 'merecer', 'neutralizar', 'consolidar', 'obnubilar', 'germinar', 'activar', 'comprar', 'wasapearias', 'reservar', 'sudar', 'atribuyo', 'nacionalizar', 'exhibir', 'yacer', 'contribuyan', 'impedir', 'familiarizar', 'intuir', 'exorcizar', 'obstaculizar', 'flotar', 'amaria', 'pasear', 'humedecer', 'barajar', 'dudar', 'celebrar', 'ayudar', 'adelantar', 'sepultar', 'jubilar', 'depositar', 'preservar', 'disfrazar', 'admitir', 'abatir', 'escalar', 'numerar', 'golpear', 'eliminar', 'llorisquear', 'estar', 'unir', 'sobresalir', 'exceptuar', 'amasteis', 'completar', 'expirar', 'glasear', 'lijar', 'obstruyen', 'expulsar', 'ofender', 'finalizar', 'restaurar', 'pisar', 'patinar', 'cepillar', 'lapidar', 'balar', 'crackear', 'huyeron', 'vaporizar', 'fastidiar', 'suponer', 'diluye', 'ocasionar', 'soler', 'implementar', 'parir', 'hemos wasapeado', 'llamar', 'estimar', 'reportar', 'satirizar', 'aproximar', 'leer', 'diluir', 'brindar', 'engordar', 'restablecer', 'retrasar', 'haya', 'enfriar', 'acariciar', 'vedar', 'lexicalizar', 'vos', 'equivocar', 'declarar', 'arrastrar', 'leñar', 'desafinar', 'garabatear', 'cambiar', 'yendo', 'deber', 'ofrecer', 'afinar', 'mendigar', 'confesar', 'gasificar', 'torcer', 'enchufar', 'incluir', 'retribuir', 'has wasapeado', 'sabotear', 'emitir', 'pillar', 'husmear', 'aportar', 'presumir', 'noblecer', 'privatizar', 'gravitar', 'rehusar', 'sobreexcitar', 'conseguir', 'recluir', 'explicitar', 'levar', 'tasar', 'reprochar', 'referir', 'usurpar', 'coincidir', 'rascar', 'maquillarse', 'distinguir', 'acabar', 'recordar', 'portar', 'presionar', 'aquejar', 'excitar', 'detener', 'amarian', 'garantizar', 'imprimir', 'atender', 'indisponer', 'destruir', 'aliñar', 'reclamar', 'volar', 'codificar', 'enamorar', 'desnudar', 'encender', 'menear', 'ventilar', 'puntualizar', 'pulir', 'sorprender', 'existir', 'tronar', 'maniatar', 'pinchar', 'abolir', 'ocluir', 'climatizar', 'fundar', 'inspirar', 'sonorizar', 'legar', 'migrar', 'notar', 'excretar', 'adjuntar', 'tatuar', 'elevar', 'fingir', 'solucionar', 'pronunciar', 'procesar', 'ulcerar', 'militarizar', 'amaran', 'dibujar', 'vestir', 'reconstruyeron', 'personalizar', 'revertir', 'retirar', 'concentrar', 'amenizar', 'editar', 'hilar', 'administrar', 'ejecutar', 'financiar', 'divorciar', 'borrar', 'vincular', 'sumergir', 'respetar', 'generar', 'afluyen', 'nortear', 'hermanar', 'competir', 'curtir', 'diferir', 'taladrar', 'favorecer', 'preguntar', 'calmar', 'malgastar', 'niquelar', 'pensar', 'malcriar', 'vayamos', 'sucumbir', 'detestar', 'retribuyan', 'complicar', 'reducir', 'aprovechar', 'integrar', 'zamarrear', 'rockear', 'depender', 'tintar', 'advertir', 'rozar', 'acotar', 'recuperar', 'ganar', 'culpar', 'liberar', 'recopilar', 'preferir', 'lucir', 'vacilar', 'ha wasapeado', 'optimizar', 'remplazar', 'saltar', 'lamentar', 'enojar', 'accionar', 'confiar', 'gotear', 'tallar', 'apostar', 'regalar', 'delinquir', 'ungir', 'enseñar', 'decidir', 'reaccionar', 'multiplicar', 'romper', 'untar', 'trotar', 'reflejar', 'enumerar', 'circular', 'wasapee', 'exiliar', 'honrar', 'suspirar', 'guillotinar', 'leyera', 'zorrear', 'encoger', 'avisar', 'calentar', 'asegurar', 'barnizar', 'hincar', 'abandonar', 'enhebrar', 'baldear', 'vivir', 'marear', 'fotocopiar', 'burbujear', 'relacionar', 'remitir', 'orquestar', 'pintar', 'plantear', 'fortalecer', 'concebir', 'situar', 'dimitir', 'matar', 'radicalizar', 'inferir', 'sostener', 'soportar', 'nacer', 'destruyo', 'perfeccionar', 'nominalizar', 'besar', 'destinar', 'exhalar', 'glorificar', 'ahorrar', 'criminalizar', 'empujar', 'conocer', 'conquistar', 'atar', 'movilizar', 'restar', 'coronar', 'sanar', 'acomodar', 'inhabilitar', 'trasladar', 'atribuir', 'estimular', 'tratar', 'fabricar', 'hipotecar', 'degustar', 'bifurcar', 'señalar', 'pretender', 'acostar', 'apreciar', 'contactar', 'lubricar', 'inaugurar', 'planear', 'grabar', 'fregar', 'llevar', 'aplicar', 'equiparar', 'gemir', 'stalkear', 'ultimar', 'acceder', 'descender', 'reproducir', 'mantener', 'funcionar', 'rodar', 'cantar', 'proyectar', 'coordinar', 'rejuvenecer', 'fomentar', 'entretener', 'absorber', 'interferir', 'conceder', 'volver', 'inspeccionar', 'molestar', 'pender', 'oler', 'escupir', 'influye', 'magullar', 'seguir', 'trabajar', 'abrazar', 'invitar', 'revelar', 'inclinar', 'osar', 'orientar', 'bostezar', 'realizar', 'ablandar', 'omitir', 'penetrar', 'sospechar', 'sobrescribir', 'negar', 'limar', 'entrenar', 'volcar', 'pelear', 'elegir', 'persuadir', 'ingresar', 'explorar', 'quintuplicar', 'admirar', 'granizar', 'cuidar', 'invocar', 'castellanizar', 'causar', 'estilizar', 'ingerir', 'equilibrar', 'discriminar', 'informar', 'beneficiar', 'augurar', 'eyectar', 'he wasapeado', 'liderar', 'alegrarse', 'frustrar', 'instruye', 'inventar', 'picar', 'enterar', 'pronosticar', 'recibir', 'zampar', 'exclamar', 'aprender', 'ella', 'laborar', 'recelar', 'menospreciar', 'reconquistar', 'vilipendiar', 'malhumorar', 'hallar', 'maquillar', 'saber', 'gravar', 'aflojar', 'tomar', 'excluir', 'operar', 'descubrir', 'extenuar', 'tensar', 'purificar', 'anular', 'ejercitar', 'tragar', 'concurrir', 'ultrajar', 'asociar', 'relatar', 'sumir', 'consultar', 'expender', 'madurar', 'despedir', 'nivelar', 'visitar', 'guisar', 'usufructuar', 'zanjar', 'vallar', 'vejar', 'enriquecer', 'zafar', 'estremecer', 'recorrer', 'broncear', 'obsesionar', 'oprimir', 'escapar', 'mejorar', 'otear', 'impartir', 'halagar', 'buscar', 'cultivar', 'saquear', 'donar', 'perfumar', 'eximir', 'remover', 'wasapeemos', 'acelerar', 'enfurecer', 'tardar', 'prometer', 'clarear', 'ocurrir', 'bombear', 'respirar', 'jactar', 'torturar', 'veranear', 'transportar', 'presentir', 'elaborar', 'indexar', 'ironizar', 'vetar', 'boicotear', 'meditar', 'estirar', 'negrear', 'descongelar', 'atacar', 'verter', 'soltar', 'wasapeaba', 'jadear', 'fertilizar', 'inmiscuyan', 'tolerar', 'iniciar', 'enfatizar', 'gesticular', 'vagabundear', 'regatear', 'devorar', 'cuchichear', 'zancadillear', 'sindicalizar', 'acreditar', 'tumbar', 'encuestar', 'excluyen', 'botar', 'instalar', 'apuntar', 'subdividir', 'alojar', 'tener', 'otorgar', 'rehuyo', 'apurar', 'freir', 'pregonar', 'vencer', 'complejizar', 'nevar', 'entrometer', 'herrar', 'malograr', 'wasapearan', 'suspender', 'acampar', 'hundir', 'prestar', 'ubicar', 'deletrear', 'responder', 'poseer', 'deponer', 'resfriarse', 'zalear', 'maravillar', 'optar', 'interponer', 'endurecer', 'fortificar', 'desatar', 'irradiar', 'wasapeare', 'reinar', 'excomulgar', 'vendar', 'cifrar', 'eludir', 'stockear', 'consumir', 'granjear', 'titilar', 'flaquear', 'requerir', 'yuxtaponer', 'tentar', 'aliviar', 'extraer', 'explayar', 'inundar', 'retorcer', 'sujetar', 'pulverizar', 'contextualizar', 'habitar', 'utilizar', 'rebobinar', 'holgazanear', 'wasapeeis', 'llover', 'abrochar', 'abusar', 'seleccionar', 'aguantar', 'wasapeara o wasapease', 'observar', 'ovular', 'gerenciar', 'repetir', 'amenazar', 'deteriorar', 'cesar', 'condenar', 'trazar', 'bramar', 'formar', 'almacenar', 'guerrear', 'destituir', 'lastimar', 'errar', 'violar', 'besuquear', 'mezclar', 'modelar', 'obligar', 'amen', 'importar', 'holgar', 'wasapeais', 'izar', 'jabonar', 'exasperar', 'disputar', 'dormir', 'agarrar', 'debatir', 'masajear', 'acompañar', 'wasapeas', 'chasquear', 'zambullir', 'encajar', 'denigrar', 'jalonar', 'juerguear', 'restituir', 'clasificar', 'afirmar', 'amaras o amases', 'remar', 'tirar', 'ligar', 'incumplir', 'moldear', 'decir', 'ajustar', 'madrugar', 'simbolizar', 'batir', 'traficar', 'empequeñecer', 'asesorar', 'wasapearan o wasapeasen', 'tender', 'escabullir', 'entrevistar', 'aquietar', 'aturdir', 'criticar', 'notificar', 'formular', 'marginar', 'quebrantar', 'intimidar', 'engrasar', 'proceder', 'zapar', 'flexibilizar', 'apartar', 'corresponder', 'elogiar', 'juguetear', 'lloviznar', 'judicar', 'atemorizar', 'reprender', 'ver', 'publicar', 'agotar', 'vosotros', 'mentir', 'inhibir', 'explicar', 'guiñar', 'abortar', 'transpirar', 'intervenir', 'sacrificar', 'marchar', 'ir', 'ladrar', 'traicionar', 'reconstituyo', 'animar', 'asomar', 'librar', 'zurcir', 'esquivar', 'lavar', 'renunciar', 'disculpar', 'grajear', 'emplear', 'simular', 'rellenar', 'enfermar', 'igualar', 'combatir', 'embellecer', 'injuriar', 'anunciar', 'amareis', 'desear', 'perder', 'someter', 'apelar', 'investigar', 'cuajar', 'desplazar', 'establecer', 'confluyan', 'embaucar', 'señalizar', 'orinar', 'arrestar', 'fallecer', 'hacer', 'interrumpir', 'voltear', 'complacer', 'sintonizar', 'amarais o amaseis', 'bañar', 'sonar', 'horadar', 'grillar', 'tejer', 'ustedes', 'imponer', 'caminar', 'macerar', 'expandir', 'zapatear', 'rechazar', 'herir', 'asustar', 'posar', 'encargar', 'aclarar', 'platicar', 'sextuplicar', 'venerar', 'relajar', 'encerrar', 'repercutir', 'viajar', 'embrollar', 'amais', 'entristecer', 'morir', 'callar', 'vitorear', 'galardonar', 'subsistir', 'devolver', 'divisar', 'acoger', 'hurgar', 'manipular', 'mediar', 'entorpecer', 'exceder', 'anhelar', 'trepar', 'humear', 'adaptar', 'cocinar', 'amara o amase', 'gambetear', 'uniformar', 'estornudar', 'abrir', 'introducir', 'atrever', 'licuar', 'festejar', 'odiar', 'agitar', 'percibir', 'analizar', 'satisfacer', 'hidratar', 'copiar', 'unisonar', 'acortar', 'triturar', 'interpretar', 'legalizar', 'valorar', 'dejar', 'gustar', 'hurtar', 'usar', 'intentar', 'brotar', 'bambolear', 'machucar', 'faltar', 'ellas', 'narcotizar', 'justificar', 'lograr', 'coleccionar', 'burlar', 'lindar', 'brillar', 'aislar', 'indicar', 'aplaudir', 'cosechar', 'sacar', 'falsificar', 'hackear', 'telefonear', 'asumir', 'marchitar', 'malherir', 'banalizar', 'extinguir', 'desaconsejar', 'comprender', 'proveer', 'manifestar', 'parpadear', 'trackear', 'derretir', 'deshacer', 'arreglar', 'peinar', 'emigrar', 'jactarse', 'carecer', 'saludar', 'balear', 'fracasar', 'reparar', 'saborear', 'colaborar', 'cansar', 'durar', 'menguar', 'protestar', 'influir', 'noviar', 'resistir', 'enredar', 'ensanchar', 'separar', 'tornear', 'afeitar', 'trajinar', 'boxear', 'habeis', 'adivinar', 'revolver', 'naufragar', 'batallar', 'oyeramos', 'bufar', 'flirtear', 'hospitalizar', 'ulular', 'demostrar', 'sugerir', 'mencionar', 'patear', 'normalizar', 'acosar', 'surtir', 'jaquear', 'profetizar', 'recurrir', 'nombrar', 'martirizar', 'esterilizar', 'cenar', 'fusionar', 'infundir', 'hostigar', 'prostituya', 'aumentar', 'amarias', 'fiar', 'fascinar', 'incrementar', 'desarrollar', 'extrañar', 'rodear', 'distraer', 'hipnotizar', 'cooperar', 'constatar', 'regresar', 'convencer', 'ceder', 'hilvanar', 'temperar', 'compartir', 'añadir', 'confirmar', 'reponer', 'envolver', 'sintetizar', 'atrasar', 'olfatear', 'desvestir', 'vigilar', 'hamacar', 'malentender', 'contestar', 'esclarecer', 'llamear', 'compilar', 'mojar', 'facilitar', 'estacionar', 'resumir', 'pedir', 'atenuar', 'renovar', 'oponer', 'envidiar', 'inmigrar', 'reconocer', 'expiar', 'bastar', 'descomponer', 'sustituir', 'ocupar', 'licenciar', 'afectar', 'recitar', 'zaracear', 'maniobrar', 'readmitir', 'inmiscuir', 'nacarar', 'zunchar', 'motivar', 'invertir', 'asesinar', 'difundir', 'participar', 'juzgar', 'cautivar', 'aceptar', 'convertir', 'preparar', 'horrorizar', 'nublar', 'equivaler', 'llorar', 'visualizar', 'impulsar', 'exportar', 'importunar', 'zumbar', 'inquietar', 'esclavizar', 'cubrir', 'retener', 'entrañar', 'irrigar', 'privar', 'excusar', 'objetivar', 'evitar', 'cazar', 'proponer', 'enloquecer', 'hinchar', 'incorporar', 'beber', 'naturalizar', 'acostumbrar', 'lanzar', 'incurrir', 'luxar', 'exaltar', 'rasquetear', 'fumar', 'conversar', 'interesar', 'curar', 'wasapearemos', 'valer', 'ame', 'bonificar', 'wasapearon', 'levantar', 'limpiar', 'vender', 'restringir', 'revisar', 'amas', 'candar', 'decepcionar', 'manotear', 'wasapees', 'medicar', 'florecer', 'liquidar', 'acoplar', 'hospedar', 'soñar', 'esconder', 'tostar', 'oir', 'inyectar', 'vomitar', 'persistir', 'hachar', 'verificar', 'transferir', 'controlar', 'graznar', 'piar', 'provocar', 'mirar', 'enfadar', 'recoger', 'trinar', 'votar', 'indagar', 'gastar', 'configurar', 'triunfar', 'sonreir', 'haber', 'amaron', 'descansar', 'rehacer', 'jinetear', 'malversar', 'opacar', 'habituar', 'poner', 'gestar', 'zarandear', 'victimizar', 'superar', 'babear', 'aterrar', 'ellas wasapeaban', 'justipreciar', 'lidiar', 'figurar', 'amaste', 'estudiar', 'gozar', 'poder', 'resbalar', 'intercambiar', 'citar', 'exprimir', 'facturar', 'ejercer', 'forrar', 'permitir', 'noctambular', 'intoxicar', 'capitular', 'contemplar', 'tapar', 'contratar', 'rezar', 'flamear', 'comparar', 'wasapearamos o wasapeasemos', 'comprimir', 'doler', 'servir', 'vaticinar', 'alunizar', 'bombardear', 'amaras', 'temblar', 'caldear', 'meter', 'proteger', 'describir', 'enviar', 'laminar', 'derribar', 'basar', 'exculpar', 'templar', 'sentir', 'congelar', 'correr', 'consistir', 'concientizar', 'asombrar', 'transmitir', 'ofertar', 'filmar', 'nuclear', 'rogar', 'wasapearas o wasapeases', 'charlar', 'legislar', 'relamer', 'retroceder', 'levitar', 'suplicar', 'empeñar', 'amara', 'crear', 'frotar', 'maquinar', 'cumplir', 'cortar', 'comportar', 'deducir', 'planchar', 'matricular', 'flexionar', 'caramelizar', 'modular', 'abonar', 'disfrutar', 'fraccionar', 'adoptar', 'afrontar', 'hisopar', 'detectar', 'polucionar', 'ladear', 'esquilar', 'borbotear', 'jurar', 'desviar', 'amo', 'exacerbar', 'insertar', 'guardar', 'nebulizar', 'experimentar', 'yerguen', 'soplar', 'han wasapeado', 'aman', 'hervir', 'cruzar', 'abordar', 'desquiciar', 'sustraer', 'idolatrar', 'ser', 'discutir', 'acudir', 'amemos', 'distribuyo', 'emprender', 'ojear', 'imitar', 'transformar', 'demoler', 'morder', 'musicalizar', 'sentar', 'navegar', 'interceder', 'dañar', 'coquetear', 'ningunear', 'expatriar', 'anticipar', 'barrer', 'engañar', 'guarecer', 'estresar', 'incomodar', 'homogeneizar', 'empobrecer', 'tropezar', 'validar', 'limitar', 'coser', 'wasapeabamos', 'argumentar', 'trocear', 'consentir', 'wasapeabais', 'censurar', 'zozobrar', 'refrigerar', 'disponer', 'jalar', 'wasapearas', 'enfervorizar', 'atrapar', 'entender', 'machacar', 'wasapeaste', 'heder', 'evolucionar', 'pasar', 'centralizar', 'hociquear', 'blanquear', 'parafrasear', 'homologar', 'sustituyeran', 'insistir', 'zoncear', 'zurrar', 'tripular', 'regular', 'tartamudear', 'apestar', 'refinar', 'manchar', 'mamar', 'vulnerar', 'bloquear', 'significar', 'insultar', 'cobrar', 'corregir', 'nausear', 'pagar', 'extorsionar', 'transcurrir', 'secar', 'unificar', 'wasapeaban', 'velar', 'contaminar', 'independizar']

```python
print(verbos_irregulares)
```

    {'soy': 'ser', 'estuviste': 'estar', 'fuiste': 'ir', 'tuviste': 'tener', 'hiciste': 'hacer', 'dijiste': 'decir', 'dimar': 'decir', 'pudiste': 'poder', 'supiste': 'saber', 'pusiste': 'poner', 'viste': 'ver', 'diste': 'dar', 'damar': 'dar', 'viniste': 'venir', 'haya': 'haber', 'cupiste': 'caber', 'valiste': 'valer', 'quisiste': 'querer', 'llegaste': 'llegar', 'contaste': 'contar', 'cuesta': 'costar', 'duraste': 'durar', 'eres': 'ser', 'estas': 'estar', 'vas': 'ir', 'vaya': 'ir', 'tienes': 'tener', 'haces': 'hacer', 'dices': 'decir', 'dime': 'decir', 'puedes': 'poder', 'sabes': 'saber', 'pones': 'poner', 'ves': 'ver', 'das': 'dar', 'dame': 'dar', 'vienes': 'venir', 'has': 'haber', 'cabes': 'caber', 'vales': 'valer', 'quieres': 'querer', 'llegares': 'llegar', 'cuentas': 'contar', 'cuestan': 'costar', 'duro': 'durar', 'seras': 'ser', 'estaras': 'estar', 'iras': 'ir', 'tendras': 'tener', 'haras': 'hacer', 'diras': 'decir', 'digame': 'decir', 'podras': 'poder', 'sabras': 'saber', 'pondras': 'poner', 'veras': 'ver', 'daras': 'dar', 'vendras': 'venir', 'habras': 'haber', 'cabras': 'caber', 'valdras': 'valer', 'querras': 'querer', 'llegaras': 'llegar', 'contaras': 'contar', 'costo': 'costar', 'duraras': 'durar', 'eras': 'ser', 'estabas': 'estar', 'ibas': 'ir', 'tenias': 'tener', 'hacias': 'hacer', 'decias': 'decir', 'dimir': 'decir', 'podias': 'poder', 'sabias': 'saber', 'ponias': 'poner', 'veias': 'ver', 'dabas': 'dar', 'venias': 'venir', 'habias': 'haber', 'cabias': 'caber', 'valias': 'valer', 'querias': 'querer', 'llegarias': 'llegar', 'contabas': 'contar', 'costaria': 'costar', 'durabas': 'durar', 'es': 'ser', 'dimo': 'decir', 'darme': 'dar', 'hubiste': 'haber', 'cuentame': 'contar', 'costarian': 'costar', 'serias': 'ser', 'estarias': 'estar', 'irias': 'ir', 'tendrias': 'tener', 'harias': 'hacer', 'dirias': 'decir', 'dimiria': 'decir', 'podrias': 'poder', 'sabrias': 'saber', 'pondrias': 'poner', 'verias': 'ver', 'darias': 'dar', 'vendrias': 'venir', 'habrias': 'haber', 'cabrias': 'caber', 'valdrias': 'valer', 'querrias': 'querer', 'llegarrias': 'llegar', 'podria': 'poder', 'contarias': 'contar', 'cuestas': 'costar', 'durarias': 'durar'}

#3. Tratamiento de datos

##Raíz de los verbos

**Raíz de los verbos**

- ¿Sabias que la biblioteca `jellyfish.jaro_winkler` nos devuelve el radio de similaridad entre dos textos? Con valores entre 0 y 1, cuanto más cerca de 1, más parecido serán ambos textos, mira este ejemplo:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image2.png">
</div>

- Usando este ejemplo, crea una función `raiz` que reciba una palabra y la compare con todas las palabras de la `lista_verbos` utilizando `jaro_winkler`, y que devuelva la palabra de `lista_verbos` con mayor similaridad a la palabra ingresada.
- **Observación**: Si la palabra encontrada, con mayor similaridad, no supera el radio de `0.93` entonces deberá regresar la palabra original.
- El objetivo de esta función es encontrar la raíz del verbo ingresado.

```python
!pip install jellyfish
```

    Requirement already satisfied: jellyfish in /usr/local/lib/python3.10/dist-packages (1.0.1)

```python
!pip install --upgrade jellyfish
```

    Requirement already satisfied: jellyfish in /usr/local/lib/python3.10/dist-packages (1.0.1)

```python
import jellyfish

jellyfish.jaro_winkler_similarity("volando", "volar")
```

    0.8742857142857143

```python
import jellyfish

def raiz(palabra):

  max_sim = 0
  raiz_candidata = ""

  for verbo in lista_verbos:
    sim = jellyfish.jaro_winkler_similarity(palabra, verbo)

    if sim > max_sim:
      max_sim = sim
      raiz_candidata = verbo

  if max_sim >= 0.93:
    return raiz_candidata
  else:
    return palabra
```

##Tratamiento de texto

**Tratamiento de texto**

- Crea una función `tratamiento_texto` que reciba una frase de texto y devuelva la misma frase pero sin acentuaciones, todo en minúscula y sin espacios en blanco adicionales.
- Como en el siguiente ejemplo:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image3.png">
</div>

- El objetivo de esta función es equilibrar los textos

```python
import re

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
    frase_tratada = re.sub(rf'\b{nombre}\b', nombre.capitalize(), frase_tratada, flags=re.IGNORECASE)

  return frase_tratada
```

##Terminación de palabras

**Terminación de palabras**

- Crea una función `reemplazar_terminacion` que reciba una palabra e identifique si la misma termina en alguna de las siguientes palabras: “es”, “me”, “as”, “te”, “ste”, si coincide, entonces que substituya esa terminación por la letra “r”.
- Como en el siguiente ejemplo:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image4.png">
</div>

- El objetivo de esta función es aproximar el verbo a su raíz.

```python
terminaciones = ['es', 'me', 'as', 'ste', 'te']
excluir = ['me', 'se','ser','estar','estas']
ends = ('rte', 'a')

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
```

```python
reemplazar_terminacion("hola")
```

    'hola'

```python
tratamiento_texto("Yo Alejandro Estoy Maria?")
```

    'yo Alejandro estoy Maria'

```python
raiz("soy")
```

    'soy'

##Normalización de textos

**Normalización de textos**

- Existe otra función en esta sección llamada `normalizar(texto)`, no te preocupes, no deberás modificar nada aqui, pero eso no significa que no deba explicártela, verás, esta función se aprovecha de todas las funciones que has creado anteriormente para regresar una frase a su raíz original, a esto se le conoce como normalizar textos, que es fundamental para el aprendizaje de máquinas, además de aprovechar tus funciones, también utiliza la biblioteca `spacy` para identificar el tipo de palabra que compone una frase y así decidir cuales debe mantener y cuales palabras deberá eliminar por no ser importantes.
- Mira cómo funciona esta biblioteca:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image5.png">
</div>

- ¿Te diste cuenta? Los atributos `pos_` y `lemma_` nos indican el tipo y raíz de una palabra, por esto usamos mucho estos 2 atributos y tus funciones dentro de la función `normalizar()`

**Apoyo**

Puedes encontrar más información de la biblioteca `spacy` en su página oficial: [Linguistic Features - spaCy Usage Documentation](https://spacy.io/usage/linguistic-features)

```python
!python -m spacy download es_core_news_sm
```

    2023-09-27 20:02:15.001096: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
    To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
    2023-09-27 20:02:17.490256: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
    Collecting es-core-news-sm==3.6.0
      Downloading https://github.com/explosion/spacy-models/releases/download/es_core_news_sm-3.6.0/es_core_news_sm-3.6.0-py3-none-any.whl (12.9 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m12.9/12.9 MB[0m [31m9.9 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: spacy<3.7.0,>=3.6.0 in /usr/local/lib/python3.10/dist-packages (from es-core-news-sm==3.6.0) (3.6.1)
    Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (3.0.12)
    Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (1.0.4)
    Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (1.0.9)
    Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (2.0.7)
    Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (3.0.8)
    Requirement already satisfied: thinc<8.2.0,>=8.1.8 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (8.1.12)
    Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (1.1.2)
    Requirement already satisfied: srsly<3.0.0,>=2.4.3 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (2.4.7)
    Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (2.0.9)
    Requirement already satisfied: typer<0.10.0,>=0.3.0 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (0.9.0)
    Requirement already satisfied: pathy>=0.10.0 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (0.10.2)
    Requirement already satisfied: smart-open<7.0.0,>=5.2.1 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (6.4.0)
    Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (4.66.1)
    Requirement already satisfied: numpy>=1.15.0 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (1.23.5)
    Requirement already satisfied: requests<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (2.31.0)
    Requirement already satisfied: pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (1.10.12)
    Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (3.1.2)
    Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (67.7.2)
    Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (23.1)
    Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /usr/local/lib/python3.10/dist-packages (from spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (3.3.0)
    Requirement already satisfied: typing-extensions>=4.2.0 in /usr/local/lib/python3.10/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (4.5.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (3.2.0)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (2.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (2023.7.22)
    Requirement already satisfied: blis<0.8.0,>=0.7.8 in /usr/local/lib/python3.10/dist-packages (from thinc<8.2.0,>=8.1.8->spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (0.7.10)
    Requirement already satisfied: confection<1.0.0,>=0.0.1 in /usr/local/lib/python3.10/dist-packages (from thinc<8.2.0,>=8.1.8->spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (0.1.2)
    Requirement already satisfied: click<9.0.0,>=7.1.1 in /usr/local/lib/python3.10/dist-packages (from typer<0.10.0,>=0.3.0->spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (8.1.7)
    Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->spacy<3.7.0,>=3.6.0->es-core-news-sm==3.6.0) (2.1.3)
    [38;5;2m✔ Download and installation successful[0m
    You can now load the package via spacy.load('es_core_news_sm')

```python
import spacy
nlp = spacy.load("es_core_news_sm")
import es_core_news_sm
nlp = es_core_news_sm.load()

# def normalizar_prueba(frase):
#   palabras = frase.split()

#   for palabra in palabras:
#     raiz_palabra = raiz(palabra)
#     texto_tratado = tratamiento_texto(raiz_palabra)
#     reemplazo_palabra = reemplazar_terminacion(texto_tratado)

#     doc = nlp(reemplazo_palabra)

#     for token in doc:
#       print(f"{palabra} - {token.pos_} - {token.lemma_}")

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
```

```python
frase = 'Yo soy Alejandro y me gusta el deporte'
normalizar(frase)
```

    ['yo', 'ser', 'Alejandro', 'y', 'yo', 'gustar', 'el', 'deporte']

```python
# def normalizar(texto):
#   tokens=[]
#   doc = nlp(texto)
#   for t in doc:
#     lemma=verbos_irregulares.get(t.text, t.lemma_.split()[0])
#     lemma=re.sub(r'[^^\w\s+\-*/?¡¿!]', '', lemma)
#     if t.pos_ in ('VERB','PROPN','PRON','NOUN','AUX','SCONJ','ADJ','ADV','NUM') or lemma in lista_verbos:
#       if t.pos_=='VERB':
#         lemma = reemplazar_terminacion(lemma)
#         tokens.append(raiz(tratamiento_texto(lemma)))
#       else:
#         tokens.append(tratamiento_texto(lemma))

#   tokens = list(dict.fromkeys(tokens))
#   tokens = list(filter(None, tokens))
#   return tokens
```

```python
normalizar('hola como estas mi hermano?')
```

    ['holgar', 'como', 'estar', 'hermano']

#4. Cargar bases de documentos

##Descripción

En esta sección, vamos a construir nuestro dataframe `df_dialogo` con los 16 archivos de conversaciones que tenemos en nuestro proyecto, para esto tu misión será importar, para cada uno de los archivos de texto, la pregunta, la respuesta y el tipo en 3 listas diferentes:

pregunta → `lista_dialogos`

respuesta → `lista_dialogos_respuesta`

tipo → `lista_tipo_dialogo`

**Observaciones:**

La pregunta deberá tener un tratamiento antes de adicionarla a la lista:

```
pregunta = re.sub(r"[^\w\s+\-*/]", '', pregunta)
pregunta = tratamiento_texto(pregunta)
lista_dialogos.append(pregunta)
```

Deberás excluir la extension `'.txt'` del tipo antes de adicionarla a la lista:

```
lista_tipo_dialogo.append(tipo.replace('.txt', ''))
```

¿Y donde encontramos la pregunta, la respuesta y el tipo dentro de los archivos?. En este ejemplo te muestro como identificarlos:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image6.png">
</div>

El objetivo de esta sección es crear las listas que servirán de base para construir el dataframe `df_dialogo`, que a su vez, será utilizado tanto para la búsqueda de la mejor respuesta, así como también, será usado como base para el entrenamiento de los modelos de Machine Learning.

¿Y cómo quedará nuestro dataframe final? Aquí te muestro:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image7.png">
</div>

##Resultado

```python
import os

ruta = '/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/Chatbot/dialogos'

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
```

```python
import pandas as pd

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

df_dialogo.sample(5)

```

  <div id="df-f99f4229-faae-4bdd-b424-4c9149b9f496" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dialogo</th>
      <th>respuesta</th>
      <th>tipo</th>
      <th>interseccion</th>
      <th>jaro_winkler</th>
      <th>probabilidad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>225</th>
      <td>que haces</td>
      <td>Estoy trabajando en mi computadora. Estoy escr...</td>
      <td>Funcion</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>86</th>
      <td>cuenta es la informacion que manejas</td>
      <td>Aprendo con mi experiencia conversando con otr...</td>
      <td>Aprendizaje</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>533</th>
      <td>hola profe</td>
      <td>Hola, ¿en qué puedo ayudarte?</td>
      <td>Saludos</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>735</th>
      <td>la ciencia es hermosa verdad</td>
      <td>¡La Ciencia de datos es maravillosa!</td>
      <td>Otros</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1051</th>
      <td>tienes web</td>
      <td>Sí, este es el link: https://www.youtube.com/@...</td>
      <td>Contacto</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-f99f4229-faae-4bdd-b424-4c9149b9f496')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-f99f4229-faae-4bdd-b424-4c9149b9f496 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-f99f4229-faae-4bdd-b424-4c9149b9f496');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>

  </div>

<div id="df-87c380a1-72e4-4270-a0b8-2e2fc3711b21">
  <button class="colab-df-quickchart" onclick="quickchart('df-87c380a1-72e4-4270-a0b8-2e2fc3711b21')"
            title="Suggest charts."
            style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
width="24px">
<g>
<path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
</g>
</svg>
</button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

  <script>
    async function quickchart(key) {
      const quickchartButtonEl =
        document.querySelector('#' + key + ' button');
      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
      quickchartButtonEl.classList.add('colab-df-spinner');
      try {
        const charts = await google.colab.kernel.invokeFunction(
            'suggestCharts', [key], {});
      } catch (error) {
        console.error('Error during call to suggestCharts:', error);
      }
      quickchartButtonEl.classList.remove('colab-df-spinner');
      quickchartButtonEl.classList.add('colab-df-quickchart-complete');
    }
    (() => {
      let quickchartButtonEl =
        document.querySelector('#df-87c380a1-72e4-4270-a0b8-2e2fc3711b21 button');
      quickchartButtonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';
    })();
  </script>
</div>
    </div>
  </div>

#5. Buscar respuesta del Chatbot

##Comparación de Textos

En esta sección crearemos 2 técnicas para buscar la mejor respuesta del chatbot, la 1ra usando comparación de textos y la 2da usando un modelo de Machine Learning, veamos cómo implementar cada una de ellas:

**Comparación de Textos**

Nuestra función `dialogo()` está casi completa, sin embargo, necesito de tu ayuda para comparar los textos:

- Esta función recibe la pregunta del usuario, le realiza una limpieza, y luego recorre todo el dataframe `df_dialogo` para comparar la pregunta del usuario con la pregunta de los diálogos, si encuentra alguna pregunta que se parezca en más de un 93% entonces devuelve la respuesta correspondiente sino devuelve en blanco.
- Tu misión en esta sección será crear 3 tipos de comparación de texto, entre la pregunta del usuario y la pregunta del diálogo (columna `dialogo`), y devolver el porcentaje de similaridad (entre 0 y 1) de esta comparación, este número será guardado en las columnas `'interseccion', 'similarity', 'jaro_winkler'` de nuestro dataframe, correspondiendo al método usado en la comparación:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image8.png">
</div>

- ¿Cómo debo crear estos 3 métodos? Aquí te muestro el paso a paso:

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image9.png">
</div>

- El objetivo de esta función `dialogo()` es devolver la respuesta del chatbot basado en comparación de textos.

```python
import jellyfish
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# def interseccion(texto1, texto2):
#   palabras1 = set(texto1.split())
#   palabras2 = set(texto2.split())

#   interseccion = palabras1 & palabras2
#   return len(interseccion) / len(palabras1)

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
  return jellyfish.jaro_winkler_similarity(texto1, texto2)
```

```python
jaro_winkler("hola como estas mi hermano?","hermano")
```

    0.49982363315696654

```python
#Función para verificar si el usuário inició un diálogo
def dialogo(user_response):
  user_response = tratamiento_texto(user_response) #Tratando el texto
  user_response = re.sub(r"[^\w\s+\-*/?¡¿!]", '', user_response) #Elimina signos de puntuación
  df = df_dialogo.copy()
  for idx,row in df.iterrows():
    df.at[idx, 'interseccion'] = interseccion(user_response, row['dialogo'])
    df.at[idx, 'similarity'] = similarity(user_response, row['dialogo'])
    df.at[idx, 'jaro_winkler'] = jaro_winkler(user_response, row['dialogo'])
    df.at[idx,'probabilidad'] = max(df.at[idx,'interseccion'],df.at[idx,'similarity'],df.at[idx,'jaro_winkler'])
  df.sort_values(by=['probabilidad','jaro_winkler'], inplace=True, ascending=False)
  probabilidad = df['probabilidad'].head(1).values[0]
  if probabilidad >= 0.92:
    print('Respuesta encontrada por el método de comparación de textos - Probabilidad: ', probabilidad)
    respuesta = df['respuesta'].head(1).values[0]
  else:
    respuesta = ''
    # print(probabilidad)
  return respuesta
```

```python
dialogo("hola como estas mi hermano?")
```

    Respuesta encontrada por el método de comparación de textos - Probabilidad:  0.9279352226720647





    'Estoy bien, gracias por preguntar. ¿Y tú?'

##Machine Learning

**Machine Learning**

Utilizar comparación de textos para encontrar la respuesta es bastante útil, pero utilizar un modelo entrenado de Machine Learning es mucho mejor, veamos como podemos entrenar el nuestro:

Entre los mejores modelos para clasificación de texto, esto es, recibe una frase de entrada y devuelve el tipo de esta frase, tenemos los siguientes:

- Naive Bayes (Básico)
- Random Forest (Intermedio)
- Transformers (Avanzado)

Escoge alguno de estos 3 modelos y entrénalo con `df_dialogo`, te recomiendo el modelo Transformers. ¿Quieres una ayuda para entrenar estos modelos? Claro que sí, puedes abrir el notebook **Clasificación de texto** y usarlo como guía para entrenar tu modelo, luego guarda tu modelo en tu Google Drive para que puedas usarlo cuando quieras.

Una vez que tengas tu modelo entrenado dentro del folder `/modelo` de tu Google Drive, deberás importarlo a tu notebook.

Por último, en la función `clasificacion_modelo()` deberás usar tu modelo entrenado para predecir la frase ingresada por el usuario, una vez identificado el `tipo` de la frase, el algoritmo buscará la pregunta más parecida de este tipo en nuestro `df_dialogo` y devolverá su respectiva respuesta, en caso el `tipo` sea diferente de ‘Otros’ y su similaridad mayor a 0.5, sino devolverá en blanco.

```python
from sklearn.preprocessing import LabelEncoder

#Normalizando las frases
label_encoder = LabelEncoder()
df_dialogo['palabras'] = df_dialogo['dialogo'].apply(lambda x: ' '.join(normalizar(x)))
df_dialogo['tipo_num'] = label_encoder.fit_transform(df_dialogo['tipo'])
df_dialogo = df_dialogo[df_dialogo.palabras.values!='']
df_dialogo
```

  <div id="df-69a0540d-9c85-4b1e-be5a-f0c9e21e92dd" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dialogo</th>
      <th>respuesta</th>
      <th>tipo</th>
      <th>interseccion</th>
      <th>jaro_winkler</th>
      <th>probabilidad</th>
      <th>palabras</th>
      <th>tipo_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bueno te elogio a ti</td>
      <td>¡Muchas gracias! Me alegro mucho de oír eso.</td>
      <td>Agradecimiento</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>bueno tu elogiar</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>de acuerdo</td>
      <td>¡Gracias!</td>
      <td>Agradecimiento</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>acuerdo</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>entiendo</td>
      <td>¡Perfecto! ¡Me alegra que hayas entendido!</td>
      <td>Agradecimiento</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>entender</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>estoy de acuerdo</td>
      <td>¡Gracias!</td>
      <td>Agradecimiento</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>estar acuerdo</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>igualmente</td>
      <td>¡Igualmente!</td>
      <td>Agradecimiento</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>igualmente</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1146</th>
      <td>bueno me voy a dormir buenas noches</td>
      <td>Buenas noches 😊 Deseo que descanses bien.</td>
      <td>Despedida</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>bueno yo ir dormir buena noche</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1147</th>
      <td>bueno ps ya paz y amor</td>
      <td>¡Hasta luego! Haz el amor y no la guerra!</td>
      <td>Despedida</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>bueno ya paz amor</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1148</th>
      <td>vale</td>
      <td>¡Hasta la vista!</td>
      <td>Despedida</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>valer</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1149</th>
      <td>buena noche</td>
      <td>¡Buenas noches!</td>
      <td>Despedida</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>buen noche</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1150</th>
      <td>ok saludos</td>
      <td>¡Saludos también!</td>
      <td>Despedida</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>ok saludo</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>1149 rows × 8 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-69a0540d-9c85-4b1e-be5a-f0c9e21e92dd')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-69a0540d-9c85-4b1e-be5a-f0c9e21e92dd button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-69a0540d-9c85-4b1e-be5a-f0c9e21e92dd');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>

  </div>

<div id="df-fb1285fb-a0dc-415c-9e73-1f032485ebc6">
  <button class="colab-df-quickchart" onclick="quickchart('df-fb1285fb-a0dc-415c-9e73-1f032485ebc6')"
            title="Suggest charts."
            style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
width="24px">
<g>
<path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
</g>
</svg>
</button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

  <script>
    async function quickchart(key) {
      const quickchartButtonEl =
        document.querySelector('#' + key + ' button');
      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
      quickchartButtonEl.classList.add('colab-df-spinner');
      try {
        const charts = await google.colab.kernel.invokeFunction(
            'suggestCharts', [key], {});
      } catch (error) {
        console.error('Error during call to suggestCharts:', error);
      }
      quickchartButtonEl.classList.remove('colab-df-spinner');
      quickchartButtonEl.classList.add('colab-df-quickchart-complete');
    }
    (() => {
      let quickchartButtonEl =
        document.querySelector('#df-fb1285fb-a0dc-415c-9e73-1f032485ebc6 button');
      quickchartButtonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';
    })();
  </script>
</div>
    </div>
  </div>

```python
# Imprimir diccionario
relacion_diccionario = {}

# Iterar sobre las filas del DataFrame
for tipo, tipo_num in zip(df_dialogo['tipo'], df_dialogo['tipo_num']):
    relacion_diccionario[tipo_num] = tipo

# Imprimir el diccionario
print(relacion_diccionario)
```

    {0: 'Agradecimiento', 1: 'Aprendizaje', 5: 'Edad', 6: 'ElProfeAlejo', 7: 'Error', 8: 'Funcion', 9: 'Identidad', 10: 'Nombre', 11: 'Origen', 13: 'Saludos', 14: 'Sentimiento', 15: 'Usuario', 12: 'Otros', 2: 'Contacto', 3: 'Continuacion', 4: 'Despedida'}

###Entrenando con Naive Bayes

```python
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Separar los datos en características (X) y etiquetas (y)
X = df_dialogo['palabras']
y = df_dialogo['tipo_num']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorizar los datos de texto
vectorizer = CountVectorizer()
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Entrenar el clasificador de Naive Bayes
modelo_NB = MultinomialNB()
modelo_NB.fit(X_train_vect, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = modelo_NB.predict(X_test_vect)

# Calcular el accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)
```

    Precisión: 0.7086956521739131

```python
# Guardar el vectorizador y el modelo en un archivo
with open('/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/modelo_naive_bayes.pickle', 'wb') as archivo:
    pickle.dump((vectorizer, modelo_NB), archivo)

# Cargar el vectorizador y el modelo desde el archivo
with open('/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/modelo_naive_bayes.pickle', 'rb') as archivo:
    vectorizer, modelo_NB = pickle.load(archivo)
```

```python
# Calcular la precisión por clase
unique_classes = df_dialogo['tipo_num'].unique()
for cls in unique_classes:
    cls_indices = y_test == cls
    cls_accuracy = accuracy_score(y_test[cls_indices], y_pred[cls_indices])
    print("Accuracy para la clase", df_dialogo[df_dialogo.tipo_num == cls]['tipo'].unique()[0], ":", cls_accuracy)
```

    Accuracy para la clase Agradecimiento : 0.42857142857142855
    Accuracy para la clase Aprendizaje : 0.4444444444444444
    Accuracy para la clase Edad : 0.3333333333333333
    Accuracy para la clase ElProfeAlejo : 1.0
    Accuracy para la clase Error : 0.0
    Accuracy para la clase Funcion : 0.35714285714285715
    Accuracy para la clase Identidad : 0.43478260869565216
    Accuracy para la clase Nombre : 0.3333333333333333
    Accuracy para la clase Origen : 0.42857142857142855
    Accuracy para la clase Saludos : 0.875
    Accuracy para la clase Sentimiento : 0.5714285714285714
    Accuracy para la clase Usuario : 0.5714285714285714
    Accuracy para la clase Otros : 0.9571428571428572
    Accuracy para la clase Contacto : 0.0
    Accuracy para la clase Continuacion : 0.8333333333333334
    Accuracy para la clase Despedida : 1.0

```python
# Procesando la nueva frase
frase = ' '.join(normalizar('como haces para aprender tan rapido?'))
nueva_frase_vect = vectorizer.transform([frase])

# Realizar la predicción
prediccion = modelo_NB.predict(nueva_frase_vect)

diccionario = {14: 'Sentimiento', 13: 'Saludos', 10: 'Nombre', 9: 'Identidad', 6: 'ElProfeAlejo', 1: 'Aprendizaje', 8: 'Funcion', 15: 'Usuario', 11: 'Origen', 5: 'Edad', 0: 'Agradecimiento', 3: 'Continuacion', 2: 'Contacto', 4: 'Despedida', 12: 'Otros', 7: 'Error'}
llave_buscada = prediccion[0]
clase_encontrada = diccionario[llave_buscada]

print("La frase", frase, "se clasifica como: ", clase_encontrada)
```

    La frase como hacer aprender tanto rapido se clasifica como:  Otros

###Entrenando con Random Forest

```python
from sklearn.ensemble import RandomForestClassifier

# Separar los datos en características (X) y etiquetas (y)
X = df_dialogo['palabras']
y = df_dialogo['tipo_num']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorizar los datos de texto
vectorizer = CountVectorizer()
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Entrenar el clasificador Random Forest
Modelo_RF = RandomForestClassifier()
Modelo_RF.fit(X_train_vect, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = Modelo_RF.predict(X_test_vect)

# Calcular el accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)
```

    Precisión: 0.7695652173913043

```python
# Guardar el vectorizador y el modelo en un archivo
with open('/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/modelo_random_forest.pickle', 'wb') as archivo:
    pickle.dump((vectorizer, Modelo_RF), archivo)

# Cargar el vectorizador y el modelo desde el archivo
with open('/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/modelo_random_forest.pickle', 'rb') as archivo:
    vectorizer, Modelo_RF = pickle.load(archivo)
```

```python
# Calcular la precisión por clase
unique_classes = df_dialogo['tipo_num'].unique()
for cls in unique_classes:
    cls_indices = y_test == cls
    cls_accuracy = accuracy_score(y_test[cls_indices], y_pred[cls_indices])
    print("Accuracy para la clase", df_dialogo[df_dialogo.tipo_num == cls]['tipo'].unique()[0], ":", cls_accuracy)
```

    Accuracy para la clase Agradecimiento : 0.6428571428571429
    Accuracy para la clase Aprendizaje : 0.6666666666666666
    Accuracy para la clase Edad : 0.3333333333333333
    Accuracy para la clase ElProfeAlejo : 1.0
    Accuracy para la clase Error : 1.0
    Accuracy para la clase Funcion : 0.6428571428571429
    Accuracy para la clase Identidad : 0.782608695652174
    Accuracy para la clase Nombre : 0.6666666666666666
    Accuracy para la clase Origen : 0.7142857142857143
    Accuracy para la clase Saludos : 0.9
    Accuracy para la clase Sentimiento : 1.0
    Accuracy para la clase Usuario : 0.2857142857142857
    Accuracy para la clase Otros : 0.8142857142857143
    Accuracy para la clase Contacto : 1.0
    Accuracy para la clase Continuacion : 0.8333333333333334
    Accuracy para la clase Despedida : 0.6666666666666666

```python
# Procesando la nueva frase
frase = ' '.join(normalizar('como haces para aprender tan rapido?'))
nueva_frase_vect = vectorizer.transform([frase])

# Realizar la predicción
prediccion = Modelo_RF.predict(nueva_frase_vect)

diccionario = {14: 'Sentimiento', 13: 'Saludos', 10: 'Nombre', 9: 'Identidad', 6: 'ElProfeAlejo', 1: 'Aprendizaje', 8: 'Funcion', 15: 'Usuario', 11: 'Origen', 5: 'Edad', 0: 'Agradecimiento', 3: 'Continuacion', 2: 'Contacto', 4: 'Despedida', 12: 'Otros', 7: 'Error'}
llave_buscada = prediccion[0]
clase_encontrada = diccionario[llave_buscada]

print("La frase", frase, "se clasifica como: ", clase_encontrada)
```

    La frase como hacer aprender tanto rapido se clasifica como:  Otros

###Entrenando con Transformers

```python
!pip install transformers
```

    Collecting transformers
      Downloading transformers-4.33.3-py3-none-any.whl (7.6 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m7.6/7.6 MB[0m [31m17.6 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from transformers) (3.12.2)
    Collecting huggingface-hub<1.0,>=0.15.1 (from transformers)
      Downloading huggingface_hub-0.17.3-py3-none-any.whl (295 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m295.0/295.0 kB[0m [31m29.2 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (1.23.5)
    Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from transformers) (23.1)
    Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (6.0.1)
    Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (2023.6.3)
    Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from transformers) (2.31.0)
    Collecting tokenizers!=0.11.3,<0.14,>=0.11.1 (from transformers)
      Downloading tokenizers-0.13.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (7.8 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m7.8/7.8 MB[0m [31m38.2 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting safetensors>=0.3.1 (from transformers)
      Downloading safetensors-0.3.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.3/1.3 MB[0m [31m44.7 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.10/dist-packages (from transformers) (4.66.1)
    Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.15.1->transformers) (2023.6.0)
    Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.15.1->transformers) (4.5.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (3.2.0)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (2.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (2023.7.22)
    Installing collected packages: tokenizers, safetensors, huggingface-hub, transformers
    Successfully installed huggingface-hub-0.17.3 safetensors-0.3.3 tokenizers-0.13.3 transformers-4.33.3

```python
from transformers import BertForSequenceClassification
from transformers import BertTokenizer
import torch

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
df_train, df_test = train_test_split(df_dialogo, test_size=0.2, random_state=42)

# Cargar el modelo preentrenado de BERT para clasificación en español
model_name = 'dccuchile/bert-base-spanish-wwm-uncased'
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=df_dialogo['tipo_num'].nunique())
tokenizer = BertTokenizer.from_pretrained(model_name)

# Tokenizar y codificar las frases de entrenamiento
train_inputs = tokenizer.batch_encode_plus(
    df_train['palabras'].tolist(),
    max_length=128,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)

# Tokenizar y codificar las frases de prueba
test_inputs = tokenizer.batch_encode_plus(
    df_test['palabras'].tolist(),
    max_length=128,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)

# Preparar los datos de entrenamiento y prueba
train_data = torch.utils.data.TensorDataset(train_inputs['input_ids'], train_inputs['attention_mask'], torch.tensor(df_train['tipo_num'].tolist()))
test_data = torch.utils.data.TensorDataset(test_inputs['input_ids'], test_inputs['attention_mask'], torch.tensor(df_test['tipo_num'].tolist()))

# Definir el optimizador y la función de pérdida
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
loss_fn = torch.nn.CrossEntropyLoss()

# Entrenamiento del modelo
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
model.train()

train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=16, shuffle=True)

for epoch in range(5):  # Número de épocas de entrenamiento
    total_loss = 0

    for batch in train_dataloader:
        input_ids, attention_mask, labels = tuple(t.to(device) for t in batch)

        optimizer.zero_grad()

        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss

        total_loss += loss.item()

        loss.backward()
        optimizer.step()

    print("Epoch:", epoch + 1, "Loss:", total_loss)

# Evaluación del modelo
model.eval()
test_dataloader = torch.utils.data.DataLoader(test_data, batch_size=32, shuffle=False)

with torch.no_grad():
    predictions = []
    true_labels = []

    for batch in test_dataloader:
        input_ids, attention_mask, labels = tuple(t.to(device) for t in batch)

        outputs = model(input_ids, attention_mask=attention_mask)

        _, predicted_labels = torch.max(outputs.logits, dim=1)

        predictions.extend(predicted_labels.tolist())
        true_labels.extend(labels.tolist())

accuracy = accuracy_score(true_labels, predictions)
print("Precisión:", accuracy)
```

    Downloading (…)lve/main/config.json:   0%|          | 0.00/650 [00:00<?, ?B/s]



    Downloading pytorch_model.bin:   0%|          | 0.00/440M [00:00<?, ?B/s]


    Some weights of BertForSequenceClassification were not initialized from the model checkpoint at dccuchile/bert-base-spanish-wwm-uncased and are newly initialized: ['bert.pooler.dense.bias', 'bert.pooler.dense.weight', 'classifier.weight', 'classifier.bias']
    You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.



    Downloading (…)solve/main/vocab.txt:   0%|          | 0.00/248k [00:00<?, ?B/s]



    Downloading (…)cial_tokens_map.json:   0%|          | 0.00/134 [00:00<?, ?B/s]



    Downloading (…)okenizer_config.json:   0%|          | 0.00/310 [00:00<?, ?B/s]


    Epoch: 1 Loss: 139.7565631866455
    Epoch: 2 Loss: 113.9612363576889
    Epoch: 3 Loss: 87.10076087713242
    Epoch: 4 Loss: 63.10559403896332
    Epoch: 5 Loss: 44.37783741950989
    Precisión: 0.8043478260869565

```python
# Guardar el modelo entrenado
ruta_modelo = '/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/transformers'
model.save_pretrained(ruta_modelo)
tokenizer.save_pretrained(ruta_modelo)
```

    ('/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/transformers/tokenizer_config.json',
     '/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/transformers/special_tokens_map.json',
     '/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/transformers/vocab.txt',
     '/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/transformers/added_tokens.json')

```python
#Cargar el modelo entrenado
ruta_modelo = '/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/transformers'
Modelo_TF = BertForSequenceClassification.from_pretrained(ruta_modelo)
tokenizer_TF = BertTokenizer.from_pretrained(ruta_modelo)
```

```python
# Calcular la precisión por clase
unique_classes = df_dialogo['tipo_num'].unique()

for class_label in unique_classes:
    # Filtrar los datos por clase
    class_data = df_dialogo[df_dialogo['tipo_num'] == class_label]

    # Preparar los datos de la clase para evaluar
    tokens = tokenizer_TF.batch_encode_plus(
        class_data['palabras'].tolist(),
        truncation=True,
        padding=True,
        return_tensors='pt'
    )

    inputs = tokens['input_ids']
    attention_mask = tokens['attention_mask']
    labels = class_data['tipo_num'].tolist()

    # Pasar los datos de la clase por el modelo
    with torch.no_grad():
        outputs = Modelo_TF(inputs, attention_mask=attention_mask)

    predicted_labels = outputs.logits.argmax(dim=1).tolist()

    # Calcular la precisión para la clase
    accuracy = accuracy_score(labels, predicted_labels)
    print(f"Precisión por clase {df_dialogo[df_dialogo.tipo_num == class_label]['tipo'].unique()[0]}: {accuracy}")
```

    Precisión por clase Agradecimiento: 0.9242424242424242
    Precisión por clase Aprendizaje: 0.8837209302325582
    Precisión por clase Edad: 0.5806451612903226
    Precisión por clase ElProfeAlejo: 0.9259259259259259
    Precisión por clase Error: 1.0
    Precisión por clase Funcion: 0.9041095890410958
    Precisión por clase Identidad: 0.9506172839506173
    Precisión por clase Nombre: 0.9166666666666666
    Precisión por clase Origen: 0.86
    Precisión por clase Saludos: 0.9725274725274725
    Precisión por clase Sentimiento: 0.9577464788732394
    Precisión por clase Usuario: 0.7567567567567568
    Precisión por clase Otros: 0.9567901234567902
    Precisión por clase Contacto: 0.896551724137931
    Precisión por clase Continuacion: 0.8064516129032258
    Precisión por clase Despedida: 0.8928571428571429

```python
# Procesar nueva frase
frase = ' '.join(normalizar('hola como estas mi hermano?'))

# Tokenizar la frase de entrada
tokens = tokenizer_TF.encode_plus(
    frase,
    add_special_tokens=True,
    max_length=128,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)

# Obtener los input_ids y attention_mask
input_ids = tokens['input_ids']
attention_mask = tokens['attention_mask']

# Realizar la predicción
with torch.no_grad():
    outputs = Modelo_TF(input_ids, attention_mask)

# Obtener las etiquetas predichas
etiquetas_predichas = torch.argmax(outputs.logits, dim=1)

# Decodificar las etiquetas predichas
etiquetas_decodificadas = etiquetas_predichas.tolist()

diccionario = {14: 'Sentimiento', 13: 'Saludos', 10: 'Nombre', 9: 'Identidad', 6: 'ElProfeAlejo', 1: 'Aprendizaje', 8: 'Funcion', 15: 'Usuario', 11: 'Origen', 5: 'Edad', 0: 'Agradecimiento', 3: 'Continuacion', 2: 'Contacto', 4: 'Despedida', 12: 'Otros', 7: 'Error'}
llave_buscada = etiquetas_decodificadas[0]
clase_encontrada = diccionario[llave_buscada]
print("La frase", frase, "se clasifica como: ", clase_encontrada)
```

    La frase holgar como estar hermano se clasifica como:  Saludos

##Buscar respuesta del Chatbot

Respuesta final del Chatbot

Wow, creamos 2 formas diferentes de buscar la respuesta para nuestro Chatbot, ¿que tal si juntamos todas en una única función?

En la función `respuesta_chatbot(pregunta)` nuestro algoritmo buscará primero la respuesta por comparación de textos y sino la encuentra la buscará por el modelo entrenado de Machine Learning, ya está todo listo, veamos en el próximo paso como ejecutar nuestro Chatbot.

```python
#Cargar tu modelo entrenado aqui(recuerda siempre cargar el modelo y el vectorizer o tokenizer usado en el entrenamiento del modelo):
ruta_modelo = '/content/drive/MyDrive/BootCamp/CHALLENGE/Spring_4/modelo/transformers'
Modelo_TF = BertForSequenceClassification.from_pretrained(ruta_modelo)
tokenizer_TF = BertTokenizer.from_pretrained(ruta_modelo)
```

```python
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

  diccionario = {14: 'Sentimiento', 13: 'Saludos', 10: 'Nombre', 9: 'Identidad', 6: 'ElProfeAlejo', 1: 'Aprendizaje', 8: 'Funcion', 15: 'Usuario', 11: 'Origen', 5: 'Edad', 0: 'Agradecimiento', 3: 'Continuacion', 2: 'Contacto', 4: 'Despedida', 12: 'Otros', 7: 'Error'}
  llave_buscada = etiquetas_decodificadas[0]
  clase_encontrada = diccionario[llave_buscada]

  return clase_encontrada

```

```python
clase_encontrada("hola como estas mi hermano?")
```

    'Despedida'

```python
#Función para dialogar utilizando el modelo
def clasificacion_modelo(pregunta):

  clase_encontrada1 = clase_encontrada(pregunta)

  # print(clase_encontrada1)

  #Buscar respuesta más parecida en la clase encontrada
  df = df_dialogo[df_dialogo['tipo'] == clase_encontrada1]
  df.reset_index(inplace=True)
  vectorizer = TfidfVectorizer()
  dialogos_num = vectorizer.fit_transform(df['dialogo'])
  pregunta_num = vectorizer.transform([tratamiento_texto(pregunta)])
  similarity_scores = cosine_similarity(dialogos_num, pregunta_num)
  indice_pregunta_proxima = similarity_scores.argmax()

  # print(max(similarity_scores))

  if max(similarity_scores)>0.5 and clase_encontrada1 not in ['Otros']:
    print('Respuesta encontrada por el modelo Transformers - tipo:',clase_encontrada1)
    respuesta = df['respuesta'][indice_pregunta_proxima]
  else:
    respuesta = ''
  return respuesta
```

```python
clasificacion_modelo("hola como estas mi hermano?")
```

    Despedida
    [0.]





    ''

```python
def respuesta_chatbot(pregunta):
  respuesta_modelo = clasificacion_modelo(pregunta)
  if respuesta_modelo != '':
    return respuesta_modelo

  respuesta_df_dialogo = dialogo(pregunta)

  if respuesta_df_dialogo != '':
    return respuesta_df_dialogo
  else:
    return 'Respuesta no encontrada'

```

#6. Ejecutar Chatbot

En este último paso sólo tenemos que relajarnos y dialogar con nuestro Chatbot, hazle preguntas que estén en los documentos de diálogo, varia un poco tus preguntas, pregunta cosas que el Chatbot no haya visto durante su entrenamiento, pruébalo y observa como nos responde, estamos creando una Inteligencia Artificial, pongamos a prueba esa inteligencia 😊

<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/images/image10.png">
</div>

```python
pregunta='CoMO ESTAS'
respuesta = respuesta_chatbot(pregunta)
print(respuesta)
```

    Respuesta encontrada por el modelo Transformers - tipo: Saludos
    Estoy bien, gracias por preguntar.

```python
pregunta='hola como estas mi hermano?'
respuesta = respuesta_chatbot(pregunta)
print(respuesta)
```

    Respuesta encontrada por el método de comparación de textos - Probabilidad:  0.9279352226720647
    Estoy bien, gracias por preguntar. ¿Y tú?
