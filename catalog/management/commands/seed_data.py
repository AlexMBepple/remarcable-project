from django.core.management.base import BaseCommand
from catalog.models import Category, Tag, Product


CATEGORIES = [
    "Structural Materials",
    "Finishing Materials",
    "Equipment Rentals",
    "Subcontractor Labor",
    "Permits & Fees"
]


TAGS = [
    "heavy-duty",
    "interior",
    "exterior",
    "certified",
    "hourly-rate",
    "flat-fee",
    "bulk-pricing",
    "eco-friendly",
    "moisture-resistant",
    "pre-fabricated"
]


PRODUCTS = [
    # Structural Materials
    ("Ready-Mix Concrete (Yard)", "Structural Materials", "Standard 4000 PSI concrete mix for foundations and structural slabs.", ["heavy-duty", "bulk-pricing"]),
    ("Premium 2x4 Lumber (Stud)", "Structural Materials", "Spruce-Pine-Fir structural framing lumber treated for structural consistency.", ["interior", "bulk-pricing"]),
    ("Rebar Grade 60 (No. 4)", "Structural Materials", "High-yield carbon steel reinforcing bars for concrete reinforcement.", ["heavy-duty"]),
    ("LVL Structural Beam", "Structural Materials", "Engineered laminated veneer lumber for high-load headers and beams.", ["pre-fabricated", "heavy-duty"]),

    # Finishing Materials
    ("Drywall Sheet 4x8", "Finishing Materials", "Standard 1/2-inch gypsum board for interior wall and ceiling framing.", ["interior", "bulk-pricing"]),
    ("Exterior Latex Paint (5G)", "Finishing Materials", "Premium commercial-grade weatherproofing paint with UV inhibitors.", ["exterior"]),
    ("Porcelain Floor Tile", "Finishing Materials", "High-traffic matte finish porcelain tiles for commercial or residential use.", ["interior", "moisture-resistant"]),
    ("Moisture-Shield Drywall", "Finishing Materials", "Mold and moisture-resistant gypsum board designed for bathrooms and kitchens.", ["interior", "moisture-resistant"]),

    # Equipment Rentals
    ("Scissor Lift (Daily)", "Equipment Rentals", "26-foot electric scissor lift rental for indoor overhead tasks.", ["interior", "flat-fee"]),
    ("Mini Excavator (Weekly)", "Equipment Rentals", "Compact diesel track excavator for trenching, digging, and light grading.", ["exterior", "heavy-duty"]),
    ("Submersible Trash Pump", "Equipment Rentals", "Heavy-duty water pump rental for clearing flooded foundation pits.", ["heavy-duty", "moisture-resistant"]),
    ("Towable Air Compressor", "Equipment Rentals", "High-capacity diesel air compressor for industrial pneumatic tools.", ["exterior"]),

    # Subcontractor Labor
    ("Master Electrician (Hour)", "Subcontractor Labor", "Licensed electrical installation, rough-ins, and final panel trim work.", ["hourly-rate", "certified"]),
    ("Journeyman Plumber (Hour)", "Subcontractor Labor", "Commercial plumbing rough-ins, drainage layout, and fixture hookups.", ["hourly-rate", "certified"]),
    ("Drywall Taping Crew (Hour)", "Subcontractor Labor", "Professional mudding, taping, and level-5 finish wall sanding.", ["hourly-rate", "interior"]),
    ("HVAC Technician (Hour)", "Subcontractor Labor", "Certified technician for ductwork layout and heating/cooling system installation.", ["hourly-rate", "certified"]),

    # Permits & Fees
    ("Commercial Building Permit", "Permits & Fees", "Standard local municipality authorization fee for structural construction.", ["flat-fee", "certified"]),
    ("Environmental Impact Assessment", "Permits & Fees", "Mandatory green compliance review and site runoff inspection fee.", ["flat-fee", "eco-friendly"]),
    ("Safety Inspection Fee", "Permits & Fees", "Official third-party code validation and occupational safety sign-off.", ["flat-fee", "certified"]),
    ("Dumpster Permit Fee", "Permits & Fees", "City sidewalk and street clearance authorization for waste container placement.", ["flat-fee", "exterior"])
]


class Command(BaseCommand):
    help = "Seeds the database with sample categories, tags, and products. Safe to run more than once."

    def handle(self, *args, **options):
        category_map = {}
        for name in CATEGORIES:
            category, created = Category.objects.get_or_create(name=name)
            category_map[name] = category
        self.stdout.write(f"Categories ready: {len(category_map)}")

        tag_map = {}
        for name in TAGS:
            tag, created = Tag.objects.get_or_create(name=name)
            tag_map[name] = tag
        self.stdout.write(f"Tags ready: {len(tag_map)}")

        created_count = 0
        for name, category_name, description, tag_names in PRODUCTS:
            product, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    'description': description,
                    'category': category_map[category_name],
                },
            )
            if created:
                created_count += 1
            product.tags.set([tag_map[t] for t in tag_names])

        self.stdout.write(self.style.SUCCESS(
            f"Done. {created_count} new products created, {len(PRODUCTS) - created_count} already existed."
        ))