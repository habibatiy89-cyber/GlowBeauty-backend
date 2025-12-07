from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models

def seed_data():
    db = SessionLocal()
    
    # Clear existing data
    db.query(models.OrderItem).delete()
    db.query(models.Order).delete()
    db.query(models.Product).delete()
    db.query(models.Category).delete()
    db.commit()

    # Verified working images
    image1 = "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=500&q=60"
    image2 = "https://images.unsplash.com/photo-1522337660859-02fbefca4702?auto=format&fit=crop&w=500&q=60"
    image3 = "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?auto=format&fit=crop&w=500&q=60"
    image4 = "https://images.unsplash.com/photo-1596755389378-c31d21fd1273?auto=format&fit=crop&w=500&q=60" # Check this one, if not I'll stick to 3
    # Let's stick to the 3 verified ones to be safe, cycling them.
    images = [image1, image2, image3]

    categories_data = [
        {
            "name": "Skincare",
            "description": "Nourish and protect your skin with our premium formulations.",
            "products": [
                {"name": "Hydrating Face Serum", "price": 45.00, "description": "Deeply moisturizing serum with hyaluronic acid.", "image_url": "/assets/products/skincare_1.jpg"},
                {"name": "Vitamin C Glow Cream", "price": 38.50, "description": "Brightening moisturizer for radiant skin.", "image_url": "/assets/products/skincare_2.jpg"},
                {"name": "Gentle Foam Cleanser", "price": 22.00, "description": "Daily cleanser that removes impurities without stripping.", "image_url": "/assets/products/skincare_3.jpg"},
                {"name": "Rose Water Toner", "price": 18.00, "description": "Soothing toner to balance pH levels.", "image_url": "/assets/products/skincare_4.jpg"},
                {"name": "Overnight Repair Mask", "price": 55.00, "description": "Intensive treatment working while you sleep.", "image_url": "/assets/products/skincare_5.jpg"},
                {"name": "SPF 50 Sunscreen", "price": 30.00, "description": "Invisible broad-spectrum protection.", "image_url": "/assets/products/skincare_6.jpg"}
            ]
        },
        {
            "name": "Makeup",
            "description": "Enhance your features with our long-lasting cosmetics.",
            "products": [
                {"name": "Velvet Matte Lipstick", "price": 24.00, "description": "Richly pigmented color with a soft matte finish.", "image_url": "/assets/products/makeup_1.jpg"},
                {"name": "Liquid Foundation", "price": 42.00, "description": "Full coverage foundation with a natural finish.", "image_url": "/assets/products/makeup_2.jpg"},
                {"name": "Volumizing Mascara", "price": 26.00, "description": "Dramatic volume and lift without clumping.", "image_url": "/assets/products/makeup_3.jpg"},
                {"name": "Eyeshadow Palette", "price": 58.00, "description": "12 shimmering and matte shades for every mood.", "image_url": "/assets/products/makeup_4.jpg"},
                {"name": "Cream Blush", "price": 28.00, "description": "Blendable flush of color for cheeks.", "image_url": "/assets/products/makeup_5.jpg"},
                {"name": "Setting Spray", "price": 32.00, "description": "Lock in your look for up to 16 hours.", "image_url": "/assets/products/makeup_6.jpg"}
            ]
        },
        {
            "name": "Haircare",
            "description": "Salon-quality care for healthy, shiny hair.",
            "products": [
                {"name": "Argan Oil Shampoo", "price": 28.00, "description": "Nourishing shampoo for dry and damaged hair.", "image_url": "/assets/products/haircare_1.jpg"},
                {"name": "Keratin Conditioner", "price": 28.00, "description": "Smoothing conditioner that reduces frizz.", "image_url": "/assets/products/haircare_2.jpg"},
                {"name": "Hair Repair Mask", "price": 35.00, "description": "Deep conditioning treatment for stronger strands.", "image_url": "/assets/products/haircare_3.jpg"},
                {"name": "Scalp Scrub", "price": 30.00, "description": "Exfoliating treatment to detoxify the scalp.", "image_url": "/assets/products/haircare_4.jpg"},
                {"name": "Styling Hair Oil", "price": 25.00, "description": "Adds shine and protects against heat.", "image_url": "/assets/products/haircare_5.jpg"},
                {"name": "Dry Shampoo", "price": 22.00, "description": "Refresh your hair instantly between washes.", "image_url": "/assets/products/haircare_6.jpg"}
            ]
        },
        {
            "name": "Fragrance",
            "description": "Captivating scents that leave a lasting impression.",
            "products": [
                {"name": "Midnight Rose EDP", "price": 85.00, "description": "Seductive blend of rose, vanilla, and amber.", "image_url": "/assets/products/fragrance_1.jpg"},
                {"name": "Citrus Breeze EDT", "price": 65.00, "description": "Fresh and uplifting notes of lemon and bergamot.", "image_url": "/assets/products/fragrance_2.jpg"},
                {"name": "Vanilla Woods", "price": 75.00, "description": "Warm and cozy scent with woody undertones.", "image_url": "/assets/products/fragrance_3.jpg"},
                {"name": "Ocean Mist", "price": 60.00, "description": "Clean and crisp aquatic fragrance.", "image_url": "/assets/products/fragrance_4.jpg"},
                {"name": "Floral Bouquet", "price": 80.00, "description": "Timeless mix of jasmine, lily, and peony.", "image_url": "/assets/products/fragrance_5.jpg"},
                {"name": "Travel Mini Set", "price": 45.00, "description": "Set of 3 signature scents in travel size.", "image_url": "/assets/products/fragrance_6.jpg"}
            ]
        },
        {
            "name": "Bath & Body",
            "description": "Indulge in luxurious self-care rituals.",
            "products": [
                {"name": "Shea Butter Body Lotion", "price": 24.00, "description": "Ultra-rich hydration for dry skin.", "image_url": "/assets/products/bath_1.jpg"},
                {"name": "Lavender Bath Salts", "price": 20.00, "description": "Relaxing salts to soothe tired muscles.", "image_url": "/assets/products/bath_2.jpg"},
                {"name": "Exfoliating Body Scrub", "price": 26.00, "description": "Sugar scrub for smooth, glowing skin.", "image_url": "/assets/products/bath_3.jpg"},
                {"name": "Hand Cream Trio", "price": 18.00, "description": "Mini hand creams in three scents.", "image_url": "/assets/products/bath_4.jpg"},
                {"name": "Shower Gel", "price": 16.00, "description": "Foaming gel with a refreshing scent.", "image_url": "/assets/products/bath_5.jpg"},
                {"name": "Body Oil", "price": 35.00, "description": "Lightweight oil for a satin finish.", "image_url": "/assets/products/bath_6.jpg"}
            ]
        }
    ]


    img_idx = 0
    for cat_data in categories_data:
        category = models.Category(name=cat_data["name"], description=cat_data["description"])
        db.add(category)
        db.commit()
        db.refresh(category)
        
        print(f"Created Category: {category.name}")
        
        for prod_data in cat_data["products"]:
            product = models.Product(
                name=prod_data["name"],
                description=prod_data["description"],
                price=prod_data["price"],
                image_url=prod_data["image_url"],
                category_id=category.id
            )
            db.add(product)
        db.commit()
        print(f"Added {len(cat_data['products'])} products to {category.name}")

    db.close()

if __name__ == "__main__":
    seed_data()
