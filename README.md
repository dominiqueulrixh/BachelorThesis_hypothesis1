# Hypothese 1 – Abbildbarkeit des Immobilienmarkts durch ein Multi-Agentensystem

Diese Simulation überprüft die Hypothese, dass ein Multi-Agentensystem (MAS) in der Lage ist, zentrale Akteure und Interaktionen auf dem Immobilienmarkt strukturell und technisch realitätsnah abzubilden. Ziel ist die Nachbildung grundlegender Marktprozesse wie Angebot, Nachfrage, Vermittlung und Transaktion.

---

## Ziel der Hypothese

> Ein Multi-Agentensystem kann Marktakteure und deren Interaktion auf dem Immobilienmarkt strukturell und technisch realitätsnah abbilden.

Die Validierung erfolgt über die Abbildung folgender Komponenten:

- Relevante Marktakteure: Käufer, Verkäufer, Makler
- Angebot und Nachfrage als zeitabhängige Grössen
- Preisverhalten und Matchingprozesse
- Transaktionsdynamiken unter realitätsnahen Bedingungen

---

## Modellübersicht

| Komponente      | Beschreibung                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `BuyerAgent`     | Kaufinteressierte mit Budget und Standortpräferenz, aktiviert mit Wahrscheinlichkeit |
| `SellerAgent`    | Anbieter mit fixem Preis, Standort, begrenzter Angebotsdauer                 |
| `BrokerAgent`    | Vermittler, prüft Matching zwischen Käufern und Verkäufern                   |
| `HousingMarketModel` | Steuert die Agentenerzeugung, Zeitschritte und Matchinglogik            |

Die Simulation wurde mit dem Python-Framework [`Mesa`](https://mesa.readthedocs.io/) implementiert und läuft standardmässig über 52 Wochen.

---

## Methodik

- **Zufällige Aktivierung** von Käuferagenten mit 40 %-Wahrscheinlichkeit pro Woche
- Verkäufer bieten Immobilien an, reduzieren Preis nach längerer Nichtvermarktung
- Makler vermittelt Transaktionen bei erfolgreichem Matching (Preis ≤ Budget, passende Lage)
- Alle Transaktionen werden geloggt und grafisch analysiert

---

## Ergebnisse

- Kumulative Transaktionen über Zeit spiegeln zyklische Marktaktivität wider
- Temporäre Nachfrageüberhänge bei geringer Angebotsmenge erkennbar
- Angebot sinkt in Teilen auf 0 → realistische Engpasssituation
- Käuferverhalten volatil, Markt reagiert differenziert

> Fazit: Das Modell bildet typische Marktmechanismen wie Nachfrageengpässe, Angebotsreaktionen und Transaktionsflüsse strukturell konsistent und plausibel ab.

---

## Dateien im Projektordner

| Datei                     | Funktion                                           |
|---------------------------|----------------------------------------------------|
| `main.py`                 | Startpunkt der Simulation                          |
| `housing_market_model.py` | Zentrale Modellstruktur                            |
| `buyer_agent.py`          | Logik des Käuferverhaltens                         |
| `seller_agent.py`         | Angebotslogik und Preisverlauf                     |
| `broker_agent.py`         | Matching-Mechanismus und Transaktionsverwaltung    |
| `visualisierung.ipynb`    | Grafische Auswertung der Simulationsmetriken       |
| `simulationsdaten.csv`    | Exportierte Ergebnisse für weitere Analysen        |

---

## Beispielhafte Visualisierungen

- Anzahl aktiver Käufer:innen vs. angebotene Immobilien
- Kumulative Transaktionen im Zeitverlauf
- Marktspannung (Nachfrage/Angebotsverhältnis)

---

## Weiterführend

Die Simulation bildet die methodische Grundlage für Hypothese 2 (Integration verhaltensbasierter Daten) und Hypothese 3 (erweiterte Agententypen & makroökonomische Einflussgrössen).

---
