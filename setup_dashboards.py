import os

# 1. Define the folder and the 9 required filenames
template_dir = "templates"
dashboards = [
    "student_dashboard.html",
    "guest_dashboard.html",
    "house_renter_dashboard.html",
    "house_buyer_dashboard.html",
    "landlord_dashboard.html",
    "host_dashboard.html",
    "food_vendor_dashboard.html",
    "logistics_rider_dashboard.html",
    "car_hire_dashboard.html"
]

# 2. The Master HTML Content
master_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SHV | {{ wing|capitalize }} Terminal</title>
    <link rel="stylesheet" href="/static/style.css">
    <style>
        :root { --bg: #050505; --card: #0f0f0f; --accent: #d4af37; --low: #ff4d4d; --mid: #ffcc00; --high: #00ff88; }
        body { background: var(--bg); color: white; font-family: 'Segoe UI', sans-serif; margin: 0; display: flex; height: 100vh; overflow: hidden; }
        .sidebar { width: 260px; background: #000; border-right: 1px solid #222; display: flex; flex-direction: column; padding: 40px 20px; }
        .logo { font-size: 24px; font-weight: 800; letter-spacing: 4px; color: white; text-decoration: none; margin-bottom: 50px; }
        .nav-links a { display: block; color: #666; text-decoration: none; padding: 15px 0; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; }
        .nav-links a.active { color: var(--accent); }
        .main-stage { flex: 1; padding: 60px; overflow-y: auto; }
        header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 50px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 25px; }
        .card { background: var(--card); border: 1px solid #222; border-radius: 12px; padding: 25px; }
        .price { color: var(--accent); font-weight: bold; font-size: 20px; margin: 10px 0; }
        .energy-wrapper { background: #222; height: 4px; border-radius: 2px; margin-top: 15px; }
        .energy-fill { height: 100%; border-radius: 2px; }
    </style>
</head>
<body>
    <aside class="sidebar">
        <div class="logo">SHV</div>
        <nav class="nav-links">
            <a href="#" class="active">{{ wing|upper }} TERMINAL</a>
            <a href="/">EXIT SYSTEM</a>
        </nav>
    </aside>
    <main class="main-stage">
        <header>
            <h1>{{ wing|capitalize }} <span style="font-weight: 800; color: var(--accent);">DASHBOARD</span></h1>
            <div style="background: #111; padding: 10px 20px; border: 1px solid #222; border-radius: 20px; font-size: 12px;">
                USER: {{ user.username if user else 'AUTH_REQUIRED' }}
            </div>
        </header>
        <div class="grid">
            {% for item in leads %}
            <div class="card">
                <div style="font-size: 10px; color: #555;">{{ item.name }}</div>
                <h3 style="margin: 5px 0;">{{ item.item }}</h3>
                <div class="price">{{ item.symbol }}{{ item.price }}</div>
                <div class="energy-wrapper">
                    <div class="energy-fill" style="width: {{ item.percent }}%; background: {{ item.color }};"></div>
                </div>
            </div>
            {% endfor %}
        </div>
    </main>
</body>
</html>"""

# 3. Logic to create folder and files
if not os.path.exists(template_dir):
    os.makedirs(template_dir)
    print(f"✅ Created directory: {template_dir}")

for dash in dashboards:
    file_path = os.path.join(template_dir, dash)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(master_html)
    print(f"📄 Generated: {dash}")

print("\n🚀 All 9 Dashboards are ready! You can now restart your server.")