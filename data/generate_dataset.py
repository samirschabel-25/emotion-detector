import pandas as pd
import random

data = {
    "Freude": [
        "Ich freue mich riesig auf den Urlaub",
        "Heute ist ein fantastischer Tag",
        "Ich bin sehr glücklich",
        "Das macht mich unglaublich froh",
        "Endlich habe ich mein Ziel erreicht",
        "Ich bin stolz auf meine Leistung",
        "Die Nachricht hat mich begeistert",
        "Ich könnte vor Freude springen",
        "Heute läuft alles perfekt",
        "Das ist die beste Nachricht des Jahres",
        "Ich genieße diesen Moment",
        "Mein Projekt war erfolgreich",
        "Ich habe die Prüfung bestanden",
        "Das erfüllt mich mit Freude",
        "Ich fühle mich großartig",
        "Heute bin ich voller Energie",
        "Ich habe endlich eine Lösung gefunden",
        "Das macht mich zufrieden",
        "Ich bin erleichtert und glücklich",
        "Mein Team hat gewonnen"
    ],
    "Wut": [
        "Das ist absolut unfair",
        "Ich bin stinksauer",
        "Das regt mich unglaublich auf",
        "Ich könnte ausrasten",
        "Das macht mich wütend",
        "So etwas akzeptiere ich nicht",
        "Ich bin richtig verärgert",
        "Das geht gar nicht",
        "Ich habe die Nase voll",
        "Warum passiert so etwas immer wieder",
        "Ich bin enttäuscht und wütend",
        "Das ist eine Frechheit",
        "Ich hasse solche Situationen",
        "Das macht mich aggressiv",
        "Ich bin außer mir vor Wut",
        "Das bringt mich auf die Palme",
        "So ein Unsinn",
        "Ich ärgere mich darüber",
        "Das ist unerträglich",
        "Ich bin frustriert"
    ],
    "Angst": [
        "Ich habe Angst vor morgen",
        "Das macht mir Sorgen",
        "Ich bin nervös wegen der Prüfung",
        "Mir ist ganz mulmig",
        "Ich fürchte mich vor dem Ergebnis",
        "Ich habe ein ungutes Gefühl",
        "Das verunsichert mich",
        "Ich bin angespannt",
        "Ich mache mir große Sorgen",
        "Was passiert wenn etwas schiefgeht",
        "Ich habe Angst zu versagen",
        "Ich fühle mich unsicher",
        "Das bereitet mir Kopfzerbrechen",
        "Ich bin beunruhigt",
        "Ich weiß nicht was passieren wird",
        "Ich habe Zweifel",
        "Das macht mich nervös",
        "Ich fühle mich bedroht",
        "Ich bin ängstlich",
        "Ich habe Angst vor der Zukunft"
    ],
    "Traurigkeit": [
        "Ich fühle mich allein",
        "Das macht mich traurig",
        "Mir geht es heute schlecht",
        "Ich vermisse meine Freunde",
        "Heute bin ich niedergeschlagen",
        "Ich bin enttäuscht",
        "Ich könnte weinen",
        "Das tut weh",
        "Ich fühle mich leer",
        "Alles erscheint sinnlos",
        "Ich bin traurig über die Nachricht",
        "Das belastet mich",
        "Ich fühle mich verloren",
        "Ich bin bedrückt",
        "Mir fehlt die Motivation",
        "Heute fällt mir alles schwer",
        "Ich bin unglücklich",
        "Das hat mich verletzt",
        "Ich fühle mich einsam",
        "Ich bin am Boden zerstört"
    ],
    "Neutral": [
        "Heute ist Montag",
        "Ich gehe einkaufen",
        "Das Meeting beginnt um zehn Uhr",
        "Ich trinke einen Kaffee",
        "Der Zug fährt pünktlich ab",
        "Ich arbeite heute im Homeoffice",
        "Das Fenster ist geöffnet",
        "Ich lese ein Buch",
        "Das Wetter ist bewölkt",
        "Der Termin wurde verschoben",
        "Ich fahre zur Arbeit",
        "Das Paket ist angekommen",
        "Ich sitze am Schreibtisch",
        "Die Lampe ist eingeschaltet",
        "Heute habe ich mehrere Termine",
        "Der Computer startet gerade",
        "Ich bereite das Abendessen vor",
        "Das Dokument wurde gespeichert",
        "Ich gehe später spazieren",
        "Der Supermarkt hat geöffnet"
    ]
}

verstärker = [
    "wirklich",
    "extrem",
    "sehr",
    "unglaublich",
    "ziemlich"
]

rows = []

for emotion, sentences in data.items():
    for sentence in sentences:
        rows.append([sentence, emotion])

        for _ in range(9):  # 20 * 10 = 200 pro Kategorie
            modifier = random.choice(verstärker)
            rows.append([f"{sentence} {modifier}", emotion])

df = pd.DataFrame(rows, columns=["text", "emotion"])

df = df.sample(frac=1, random_state=42)

df.to_csv("emotions.csv", index=False)

print(f"{len(df)} Datensätze erzeugt.")