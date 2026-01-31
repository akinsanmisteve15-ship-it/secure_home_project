from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# --- DATABASE ---
properties = [
    {"id": 1, "title": "Lekki Luxury Penthouse", "location": "Lekki Phase 1", "tour_url": "https://panoee.com/t/sample-tour", "price": "150,000"},
    {"id": 2, "title": "Victoria Island Studio", "location": "VI, Lagos", "tour_url": "https://panoee.com/t/sample-tour", "price": "85,000"}
]
user_wallet = {"balance": 0}
bookings = []

@app.get("/", response_class=HTMLResponse)
async def home():
    is_ready = user_wallet['balance'] >= 100000
    
    # Desktop Grid Layout for Properties
    property_cards = ""
    for p in properties:
        property_cards += f"""
        <div style="background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: flex; flex-direction: column;">
            <div style="height: 200px; background: #ddd; display: flex; align-items: center; justify-content: center; color: #666;">
                [Thumbnail Image Placeholder]
            </div>
            <div style="padding: 20px;">
                <h3 style="margin: 0 0 10px 0;">{p['title']} <span style="background: #28a745; color: white; font-size: 10px; padding: 3px 8px; border-radius: 10px; vertical-align: middle;">3D VERIFIED</span></h3>
                <p style="color: #666; margin-bottom: 20px;">📍 {p['location']} <br> <b>₦{p['price']} / night</b></p>
                
                <div style="display: flex; gap: 10px;">
                    <a href="/property/{p['id']}" style="flex: 1; text-align: center; border: 1px solid #007bff; color: #007bff; padding: 10px; border-radius: 5px; text-decoration: none; font-weight: bold;">Enter 3D Tour</a>
                    {"<a href='/book/"+str(p['id'])+"' style='flex: 1; text-align: center; background: #007bff; color: white; padding: 10px; border-radius: 5px; text-decoration: none;'>Book Inspection</a>" if is_ready else "<button disabled style='flex: 1; background: #ccc; border: none; border-radius: 5px; color: white; cursor: not-allowed;'>Wallet Low</button>"}
                </div>
            </div>
        </div>
        """

    return f"""
    <html>
        <head>
            <title>Secure Home Verify | Dashboard</title>
        </head>
        <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f5; margin: 0; display: flex;">
            
            <div style="width: 280px; background: #1a1a2e; color: white; height: 100vh; position: fixed; padding: 30px 20px;">
                <h2 style="color: #4e73df;">SHV PLATFORM</h2>
                <hr style="border: 0.5px solid #333; margin: 20px 0;">
                <p style="color: #888; font-size: 12px;">MAIN WALLET</p>
                <h2 style="margin-top: 5px;">₦{user_wallet['balance']:,}</h2>
                <a href="/fund" style="background: #28a745; color: white; display: block; text-align: center; padding: 10px; border-radius: 5px; text-decoration: none; margin-bottom: 30px;">+ Fund Wallet</a>
                
                <p style="color: #888; font-size: 12px;">MY INSPECTIONS</p>
                <div style="font-size: 14px;">
                    {"<p>No active requests</p>" if not bookings else "".join([f"<p style='background: #333; padding: 8px; border-radius: 5px; margin-bottom: 5px;'>📅 {b}</p>" for b in bookings])}
                </div>
            </div>

            <div style="margin-left: 280px; padding: 40px; width: 100%;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;">
                    <h1>Verified Shortlet Marketplace</h1>
                    <div style="background: white; padding: 10px 20px; border-radius: 30px; border: 1px solid #ddd;">
                        Status: <b>{'🟢 Payment Ready' if is_ready else '🔴 Unverified'}</b>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 30px;">
                    {property_cards}
                </div>
            </div>
        </body>
    </html>
    """

# --- REMAINDER OF LOGIC (3D PAGE & ROUTES) ---
@app.get("/property/{{prop_id}}", response_class=HTMLResponse)
async def view_property(prop_id: int):
    prop = next((p for p in properties if p['id'] == prop_id), None)
    if not prop: return "Error"
    return f"""
    <html><body style="margin:0; overflow:hidden;">
        <div style="position: absolute; top: 10px; left: 10px; z-index: 100;">
            <a href="/" style="background: rgba(0,0,0,0.7); color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">← Exit 3D View</a>
        </div>
        <iframe src="{prop['tour_url']}" width="100%" height="100vh" style="border:none; height: 100vh;"></iframe>
    </body></html>
    """

@app.get("/book/{{prop_id}}")
async def book_inspection(prop_id: int):
    if user_wallet['balance'] >= 100000:
        prop = next((p for p in properties if p['id'] == prop_id), None)
        if prop: bookings.append(prop['title'])
    return RedirectResponse(url="/", status_code=303)

@app.get("/fund")
async def fund():
    user_wallet['balance'] += 150000
    return RedirectResponse(url="/", status_code=303)