from app import app

@app.route('/')
def home():
    return "API Tienda de Ropa funcionando correctamente"

# Mostrar todas las rutas registradas
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint}: {rule.rule}")

if __name__ == "__main__":
    app.run(debug=True)
