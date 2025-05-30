"""
Products data for the mall agents bill system.
"""

products = {
    # Electronics
    "e001": {
        "name": "iPhone 15 Pro",
        "description": "Latest Apple smartphone with A17 Pro chip",
        "price": 999.99,
        "category": "electronics",
        "stock": 25
    },
    "e002": {
        "name": "Samsung Galaxy S24",
        "description": "Android flagship with AI features",
        "price": 899.99,
        "category": "electronics",
        "stock": 30
    },
    "e003": {
        "name": "MacBook Air M3",
        "description": "Lightweight laptop with M3 chip",
        "price": 1299.99,
        "category": "electronics",
        "stock": 15
    },
    "e004": {
        "name": "iPad Pro 12.9",
        "description": "Professional tablet with M2 chip",
        "price": 1099.99,
        "category": "electronics",
        "stock": 20
    },
    "e005": {
        "name": "AirPods Pro",
        "description": "Wireless earbuds with noise cancellation",
        "price": 249.99,
        "category": "electronics",
        "stock": 50
    },
    "e006": {
        "name": "Sony WH-1000XM5",
        "description": "Premium noise-canceling headphones",
        "price": 399.99,
        "category": "electronics",
        "stock": 35
    },
    "e007": {
        "name": "Nintendo Switch OLED",
        "description": "Gaming console with OLED screen",
        "price": 349.99,
        "category": "electronics",
        "stock": 40
    },
    "e008": {
        "name": "Dell XPS 13",
        "description": "Ultrabook with Intel Core i7",
        "price": 1199.99,
        "category": "electronics",
        "stock": 12
    },
    "e009": {
        "name": "Apple Watch Series 9",
        "description": "Smartwatch with health monitoring",
        "price": 399.99,
        "category": "electronics",
        "stock": 45
    },
    "e010": {
        "name": "Canon EOS R6",
        "description": "Mirrorless camera for professionals",
        "price": 2499.99,
        "category": "electronics",
        "stock": 8
    },

    # Clothing
    "c001": {
        "name": "Levi's 501 Jeans",
        "description": "Classic straight-leg denim jeans",
        "price": 89.99,
        "category": "clothing",
        "stock": 60
    },
    "c002": {
        "name": "Nike Air Force 1",
        "description": "Iconic white sneakers",
        "price": 110.00,
        "category": "clothing",
        "stock": 75
    },
    "c003": {
        "name": "Patagonia Fleece Jacket",
        "description": "Warm outdoor fleece jacket",
        "price": 149.99,
        "category": "clothing",
        "stock": 25
    },
    "c004": {
        "name": "Adidas Ultraboost 22",
        "description": "Running shoes with boost technology",
        "price": 180.00,
        "category": "clothing",
        "stock": 40
    },
    "c005": {
        "name": "Uniqlo Heattech Shirt",
        "description": "Thermal base layer shirt",
        "price": 19.99,
        "category": "clothing",
        "stock": 100
    },
    "c006": {
        "name": "Ray-Ban Aviators",
        "description": "Classic aviator sunglasses",
        "price": 154.99,
        "category": "clothing",
        "stock": 30
    },
    "c007": {
        "name": "North Face Puffer Jacket",
        "description": "Insulated winter jacket",
        "price": 299.99,
        "category": "clothing",
        "stock": 20
    },
    "c008": {
        "name": "Converse Chuck Taylor",
        "description": "Classic canvas sneakers",
        "price": 65.00,
        "category": "clothing",
        "stock": 55
    },
    "c009": {
        "name": "Polo Ralph Lauren Shirt",
        "description": "Cotton polo shirt",
        "price": 89.99,
        "category": "clothing",
        "stock": 45
    },
    "c010": {
        "name": "Lululemon Yoga Pants",
        "description": "High-performance athletic leggings",
        "price": 128.00,
        "category": "clothing",
        "stock": 35
    },

    # Books
    "b001": {
        "name": "The Psychology of Money",
        "description": "Financial wisdom by Morgan Housel",
        "price": 16.99,
        "category": "books",
        "stock": 80
    },
    "b002": {
        "name": "Atomic Habits",
        "description": "Build good habits by James Clear",
        "price": 18.99,
        "category": "books",
        "stock": 95
    },
    "b003": {
        "name": "Dune",
        "description": "Classic sci-fi novel by Frank Herbert",
        "price": 14.99,
        "category": "books",
        "stock": 60
    },
    "b004": {
        "name": "The Midnight Library",
        "description": "Fiction by Matt Haig",
        "price": 15.99,
        "category": "books",
        "stock": 70
    },
    "b005": {
        "name": "Sapiens",
        "description": "History of humankind by Yuval Noah Harari",
        "price": 19.99,
        "category": "books",
        "stock": 55
    },
    "b006": {
        "name": "The Lean Startup",
        "description": "Business methodology by Eric Ries",
        "price": 17.99,
        "category": "books",
        "stock": 40
    },
    "b007": {
        "name": "1984",
        "description": "Dystopian novel by George Orwell",
        "price": 13.99,
        "category": "books",
        "stock": 85
    },
    "b008": {
        "name": "The Alchemist",
        "description": "Philosophical novel by Paulo Coelho",
        "price": 14.99,
        "category": "books",
        "stock": 75
    },
    "b009": {
        "name": "Clean Code",
        "description": "Programming best practices by Robert Martin",
        "price": 42.99,
        "category": "books",
        "stock": 30
    },
    "b010": {
        "name": "The 7 Habits",
        "description": "Self-help by Stephen Covey",
        "price": 16.99,
        "category": "books",
        "stock": 50
    },

    # Home
    "h001": {
        "name": "Dyson V15 Vacuum",
        "description": "Cordless vacuum with laser detection",
        "price": 749.99,
        "category": "home",
        "stock": 15
    },
    "h002": {
        "name": "Instant Pot Duo",
        "description": "7-in-1 electric pressure cooker",
        "price": 99.99,
        "category": "home",
        "stock": 35
    },
    "h003": {
        "name": "Philips Hue Starter Kit",
        "description": "Smart LED light bulbs",
        "price": 199.99,
        "category": "home",
        "stock": 25
    },
    "h004": {
        "name": "Roomba i7+",
        "description": "Robot vacuum with auto-empty base",
        "price": 599.99,
        "category": "home",
        "stock": 12
    },
    "h005": {
        "name": "Ninja Blender",
        "description": "High-performance blender",
        "price": 149.99,
        "category": "home",
        "stock": 40
    },
    "h006": {
        "name": "Nest Thermostat",
        "description": "Smart programmable thermostat",
        "price": 249.99,
        "category": "home",
        "stock": 20
    },
    "h007": {
        "name": "KitchenAid Stand Mixer",
        "description": "Professional stand mixer",
        "price": 379.99,
        "category": "home",
        "stock": 18
    },
    "h008": {
        "name": "Casper Mattress Queen",
        "description": "Memory foam mattress",
        "price": 1095.00,
        "category": "home",
        "stock": 10
    },
    "h009": {
        "name": "Ring Video Doorbell",
        "description": "Smart doorbell with camera",
        "price": 199.99,
        "category": "home",
        "stock": 30
    },
    "h010": {
        "name": "Shark Steam Mop",
        "description": "Steam cleaning mop",
        "price": 79.99,
        "category": "home",
        "stock": 45
    },

    # Sports
    "s001": {
        "name": "Peloton Bike+",
        "description": "Interactive exercise bike",
        "price": 2495.00,
        "category": "sports",
        "stock": 5
    },
    "s002": {
        "name": "Wilson Tennis Racket",
        "description": "Professional tennis racket",
        "price": 199.99,
        "category": "sports",
        "stock": 25
    },
    "s003": {
        "name": "Spalding Basketball",
        "description": "Official size basketball",
        "price": 29.99,
        "category": "sports",
        "stock": 60
    },
    "s004": {
        "name": "Yoga Mat Premium",
        "description": "Non-slip exercise mat",
        "price": 49.99,
        "category": "sports",
        "stock": 80
    },
    "s005": {
        "name": "Bowflex Dumbbells",
        "description": "Adjustable weight dumbbells",
        "price": 349.99,
        "category": "sports",
        "stock": 15
    },
    "s006": {
        "name": "Fitbit Charge 5",
        "description": "Fitness tracker with GPS",
        "price": 179.99,
        "category": "sports",
        "stock": 40
    },
    "s007": {
        "name": "Coleman Camping Tent",
        "description": "4-person waterproof tent",
        "price": 129.99,
        "category": "sports",
        "stock": 20
    },
    "s008": {
        "name": "Hydro Flask Water Bottle",
        "description": "Insulated stainless steel bottle",
        "price": 44.99,
        "category": "sports",
        "stock": 70
    },
    "s009": {
        "name": "TRX Suspension Trainer",
        "description": "Bodyweight training system",
        "price": 195.00,
        "category": "sports",
        "stock": 30
    },
    "s010": {
        "name": "Garmin GPS Watch",
        "description": "Multi-sport GPS smartwatch",
        "price": 449.99,
        "category": "sports",
        "stock": 22
    }
}