from model.housing_market_model import HousingMarketModel
import matplotlib.pyplot as plt

# Modell ausführen
model = HousingMarketModel()
for i in range(52):  # Simulation über 1 Jahr (52 Kalenderwochen)
    model.step()
    print(f"Woche {model.current_week - 1}: Verkäufe bisher = {len(model.sales)}")


# Ergebnisse drucken
print("Anzahl abgeschlossener Verkäufe:", len(model.sales))
print("Abgeschlossene Verkäufe durch Broker:", model.broker.completed_sales)

# Ergebnisse visualisieren
results = model.datacollector.get_model_vars_dataframe()

# Plotten
plt.figure(figsize=(10, 6))
plt.plot(results["Completed Sales"], label="Abgeschlossene Verkäufe gesamt")
plt.plot(results["Broker Sales"], label="Verkäufe über Broker")
plt.plot(results["Active Buyers"], label="Aktive Käufer")
plt.plot(results["Listed Properties"], label="Angebotene Immobilien")
plt.xlabel("Zeitschritte")
plt.ylabel("Anzahl")
plt.title("Immobilienmarktaktivität im Simulationsmodell")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
