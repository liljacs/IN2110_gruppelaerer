from sklearn.feature_extraction.text import CountVectorizer
from in2110.oblig1 import scatter_plot

# Eksempel for å vise hvordan vi kan visualisere dataene
# med scatter_plot

# Dataene er kunstige, men lagd for å være litt ulike.
# Hvis man ser på filene ser man at de bare er mange ord
# repetert i et tilfeldig antall ganger.


# Vi åpner filene.
# with...as er en måte å åpne filer på slik at vi ikke
# trenger å uroe oss for å glemme å lukke dem.

# I list comprehensionen lager vi ei liste av alle
# dokumentene. if x != "" er bare for å fjerne tomme
# elementer som kommer med fordi det ble lagt til et ekstra
# linjeskift da de ble lagt.

with open("snjo_ut.txt","r",encoding="utf-8") as data:
    snjo = [x for x in data.read().split("\n") if x != ""]

with open("davvi_ut.txt","r",encoding="utf-8") as data:
    davvi = [x for x in data.read().split("\n") if x != ""]

with open("nyheit_ut.txt","r",encoding="utf-8") as data:
    nyheit = [x for x in data.read().split("\n") if x != ""]

# Så skiller vi ut dataene og navna på klassene (labels):
data = snjo + davvi + nyheit
labels = ["snø" for x in snjo] + ["samisk" for x in davvi] + ["nyhet" for x in nyheit]

# Så initialiserer vi vektorizer-en.
vectorizer = CountVectorizer()

# Her bruker vi fit_transform på dataene våre.
X = vectorizer.fit_transform(data)

# Til slutt kan vi lage plottet vårt. X holder på vektor-
# representasjonene.

scatter_plot(X, labels)



