# Pow(d)er to the People

Voor het vak algoritmen en heuristieken zullen we gezamenlijk onze programmeervaardigheden in combinatie met AI-technieken inzetten om een onoplosbaar probleem op te lossen. De case die we proberen op te lossen is genaamd _Protein Pow(d)er_. Het doel van deze case is om eiwitten zo op te bouwen dat het eiwit zo stabiel mogelijk is. Een eiwit bestaat uit drie aminozuren: Polair (P), Hydrofoob (H), en Cysteine (C). Stabilitiet wordt bereikt door de bond tussen twee H's. twee C's. of een H met een C. Twee H's of een C-H nond zorgt voor een waarde van -1, twee C's voor een waarde van -5. Hoe lager de eindwaarde van het eiwit, hoe stabilier het eiwit is. Om de _string_ van aminozuren te vinden die een eiwit vinden met de hoogste stabiliteit, hebben we verschillende algoritmen geïmplementeerd. 
## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in Python 3.7. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip d.m.v. de volgende instructie:

```
pip install -r requirements.txt
```

Of via conda:

```
conda install --file requirements.txt
```

### Gebruik

Een voorbeeld kan gerund worden door het volgende aan te roepen: 

```
python main.py amino1 sa
```
Er zijn in totaal 9 amino textfiles die kunnen worden aangeroepen. Een voorbeeld boven is amino1, maar amino7 zou daarvoor ook in de plaats mogen. 

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor de verscheidende algoritmes
  - **/code/classes**: bevat de benodigde classes voor deze case
  - **/code/visualisation**: bevat de code voor visualisatie
- **/data**: bevat de verschillende databestanden met daarin de eiwitstrings die kunnen worden aangeroepen om een van de 9 voorbeelden te runnen 

### Algoritmes

De volgende algoritmes kunnen geimplenteerd worden om een proteinstring te vouwen:


- **random**
- **greedy**
- **depth first**
- **breadth first**
- **sa**: Simulated Annealing


## Auteurs
- Sarah Blok
- Suze Frikkee
- Marieke Mulder
