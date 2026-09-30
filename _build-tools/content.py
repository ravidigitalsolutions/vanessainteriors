"""All page content, taken from 'VANESSA INTERIORS website content.docx'.
Service pages map 1:1 to PAGES 4–14 of the document."""

SITE_URL = "https://www.vanessainteriors.in"
PHONE = "+91 9291199999"
PHONE_LINK = "+919291199999"
WA_URL = "https://wa.me/919291199999"
EMAIL = "vanessainteriors@mail.com"
ADDRESS = "Aruna Inn, 49-24-16, Sankara Matam Road, Madhuranagar, Akkayyapalem, Visakhapatnam, Andhra Pradesh – 530016"
INSTAGRAM = "https://www.instagram.com/vanessainteriorsindia/"

# ---------------------------------------------------------------- SERVICES
# block types: cards(title, items[(t,d)]) | checklist(title, lead, items, note)
#              steps(title, items[(t,d)]) | chain(title, items, note) | text(title, paras)
SERVICES = [
    dict(
        slug="home-interiors", name="Home Interiors", icon="home", img="home-interiors", est="completeHome",
        short="Customized interior designs for modern homes, apartments, and independent houses.",
        meta_title="Home Interior Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Vanessa Interiors offers luxury and customized home interior design services in Visakhapatnam for apartments, houses, and villas.",
        h1="Luxury Home Interiors Designed Around You",
        intro=[
            "Your home should be a reflection of your personality, lifestyle, and everyday needs.",
            "Vanessa Interiors offers customized home interior design services in Visakhapatnam, helping homeowners transform their spaces through thoughtful planning, luxury-inspired aesthetics, and functional design solutions.",
            "From living rooms and bedrooms to modular kitchens and wardrobes, we work to create interiors that bring together comfort, organization, and visual appeal.",
            "Our design approach is tailored to your property's layout, preferences, and project requirements.",
        ],
        link_sentence=("Explore our {modular kitchen design services} to create a functional and customized kitchen for your home.", "modular-kitchen"),
        blocks=[
            ("cards", "Our Home Interior Services", [
                ("Living Room Interiors", "Create elegant and welcoming living spaces with customized layouts, furniture planning, TV units, and coordinated finishes.", "living-room-design"),
                ("Bedroom Interiors", "Design comfortable bedrooms with personalized furniture arrangements, wardrobes, lighting, and design details.", "bedroom-design"),
                ("Modular Kitchen", "Explore kitchen layouts and storage solutions designed for your available space and requirements.", "modular-kitchen"),
                ("Wardrobes", "Plan customized wardrobe solutions that combine storage functionality with the overall room design.", "wardrobes"),
                ("False Ceiling", "Explore ceiling designs that support your room's visual appearance and lighting requirements.", "false-ceiling"),
                ("Complete Home Interiors", "Coordinate interior requirements across multiple rooms to create a cohesive design approach.", None),
            ]),
            ("checklist", "Why Choose Our Home Interior Services?", "", [
                "Customized design concepts", "Luxury-inspired interiors", "Residential interior solutions",
                "Functional space planning", "Own execution team", "Project-specific consultation"], ""),
            ("chain", "Home Interior Process", ["Consultation", "Planning", "Design", "Scope Finalization", "Execution", "Completion"], ""),
        ],
        faq=[1, 3, 6],
        cta="Get a Home Interior Consultation",
        related=["modular-kitchen", "living-room-design", "bedroom-design", "turnkey-interiors"],
    ),
    dict(
        slug="modular-kitchen", name="Modular Kitchen", icon="kitchen", img="modular-kitchen", est="kitchen",
        short="Functional and stylish kitchen designs with customized storage and finish options.",
        meta_title="Modular Kitchen Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Explore customized modular kitchen designs in Visakhapatnam with Vanessa Interiors. Functional layouts, storage planning, and stylish finishes.",
        h1="Modern Modular Kitchens Designed for Your Home",
        intro=[
            "A kitchen should be both visually appealing and practical for everyday use.",
            "Vanessa Interiors provides customized modular kitchen design solutions in Visakhapatnam, helping homeowners explore layouts, storage planning, materials, and finish options suited to their requirements.",
            "Whether you prefer a modern luxury kitchen or a clean, contemporary design, our team helps you plan a kitchen that complements your home.",
        ],
        blocks=[
            ("cards", "Our Modular Kitchen Solutions", [
                ("L-Shaped Kitchens", "Suitable for various kitchen layouts, with planning based on available space and workflow.", None),
                ("U-Shaped Kitchens", "Designed to utilize multiple sides of a kitchen area while considering movement and storage requirements.", None),
                ("Parallel Kitchens", "A layout option for kitchens with two facing work areas.", None),
                ("Straight-Line Kitchens", "A practical layout for suitable compact or linear spaces.", None),
                ("Customized Storage", "Explore cabinet, drawer, and storage planning based on your requirements.", None),
                ("Kitchen Finishes", "Discuss available finish options, countertop coordination, and backsplash concepts.", None),
            ]),
            ("checklist", "Our Kitchen Design Approach", "We consider:", [
                "Kitchen dimensions", "Storage requirements", "Cooking habits", "Movement and workflow",
                "Material preferences", "Design style", "Budget and project scope"],
             "The final kitchen specifications depend on the agreed design and execution requirements."),
        ],
        faq=[8, 3],
        cta="Design Your Dream Modular Kitchen",
        related=["home-interiors", "wardrobes", "living-room-design"],
    ),
    dict(
        slug="bedroom-design", name="Bedroom Design", icon="bed", img="bedroom-design", est="bedroom",
        short="Comfortable, elegant, and personalized bedroom interiors.",
        meta_title="Bedroom Interior Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Create luxury and customized bedroom interiors in Visakhapatnam with Vanessa Interiors. Personalized designs for master bedrooms and other spaces.",
        h1="Luxury Bedroom Interiors for Comfortable Living",
        intro=[
            "Your bedroom should provide comfort, organization, and a design that feels personal.",
            "Vanessa Interiors offers customized bedroom interior design services in Visakhapatnam, helping homeowners plan interiors based on their space, lifestyle, and design preferences.",
            "We focus on creating bedroom concepts that combine practical furniture placement, storage, lighting, and visual harmony.",
        ],
        blocks=[
            ("cards", "Our Bedroom Design Services", [
                ("Master Bedroom Interiors", "Personalized design concepts for comfortable and sophisticated master bedrooms.", None),
                ("Guest Bedroom Interiors", "Practical and welcoming interiors designed around guest comfort and space requirements.", None),
                ("Kids' Bedroom Interiors", "Customized room concepts that consider functionality, storage, and personal preferences.", None),
                ("Bed Back Wall Designs", "Explore decorative wall treatments and design concepts for the bed backdrop.", None),
                ("Bedroom Wardrobes", "Plan storage solutions that coordinate with the bedroom's overall design.", "wardrobes"),
                ("Lighting & Ceiling Coordination", "Consider lighting and ceiling design as part of the overall interior concept.", "false-ceiling"),
            ]),
            ("checklist", "Bedroom Design Considerations", "", [
                "Room dimensions", "Bed and furniture placement", "Storage requirements", "Lighting",
                "Color and material preferences", "Design style", "Functional requirements"], ""),
        ],
        faq=[6, 3],
        cta="Create Your Personalized Bedroom",
        related=["wardrobes", "false-ceiling", "home-interiors"],
    ),
    dict(
        slug="living-room-design", name="Living Room Design", icon="sofa", img="living-room", est="livingArea",
        short="Sophisticated living spaces designed for comfort, aesthetics, and everyday living.",
        meta_title="Living Room Interior Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Vanessa Interiors offers luxury living room interior design services in Visakhapatnam. Explore customized layouts, TV units, feature walls, and lighting.",
        h1="Living Room Interiors That Reflect Your Style",
        intro=[
            "The living room is often the central space for family time, relaxation, and entertaining guests.",
            "Vanessa Interiors offers customized living room interior design services in Visakhapatnam, helping homeowners develop stylish and functional spaces.",
            "Our designs focus on coordinating furniture, lighting, finishes, and decorative elements to suit your preferred aesthetic.",
        ],
        blocks=[
            ("cards", "Our Living Room Design Services", [
                ("Modern Living Room Interiors", "Clean and contemporary design concepts for modern homes.", None),
                ("Luxury Living Room Interiors", "Elegant design concepts featuring coordinated materials, furniture, and finishes.", None),
                ("TV Unit Designs", "Customized TV wall and storage concepts based on the room layout.", None),
                ("Feature Walls", "Decorative wall concepts designed to add visual interest.", None),
                ("False Ceiling & Lighting", "Coordinate ceiling and lighting concepts with the overall room design.", "false-ceiling"),
                ("Furniture Layout Planning", "Consider furniture placement, circulation, and available space.", None),
            ]),
            ("text", "Our Approach", [
                "We discuss your preferred design style, furniture requirements, space dimensions, and functional needs before developing a suitable design concept."]),
        ],
        faq=[6, 3],
        cta="Plan Your Living Room Interior",
        related=["false-ceiling", "home-interiors", "bedroom-design"],
    ),
    dict(
        slug="wardrobes", name="Wardrobes", icon="wardrobe", img="wardrobes", est="wardrobes",
        short="Customized wardrobe solutions that combine storage efficiency and design.",
        meta_title="Custom Wardrobe Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Explore customized wardrobe designs in Visakhapatnam with Vanessa Interiors. Stylish and functional storage solutions for modern homes.",
        h1="Customized Wardrobe Designs for Smart Storage",
        intro=[
            "A well-planned wardrobe can improve organization while complementing your bedroom interiors.",
            "Vanessa Interiors offers customized wardrobe design solutions in Visakhapatnam, helping clients explore storage layouts, design styles, and finish options based on their requirements.",
        ],
        blocks=[
            ("cards", "Our Wardrobe Solutions", [
                ("Sliding Wardrobes", "Explore sliding door concepts for suitable room layouts.", None),
                ("Hinged Wardrobes", "Traditional door-based wardrobe solutions with customized storage planning.", None),
                ("Full-Height Wardrobes", "Storage concepts designed to utilize available vertical space.", None),
                ("Walk-In Wardrobes", "Customized walk-in storage concepts for suitable spaces.", None),
                ("Loft Storage", "Additional storage planning above wardrobe units where appropriate.", None),
                ("Internal Storage Planning", "Consider shelves, drawers, hanging areas, and other organizational requirements.", None),
            ]),
            ("checklist", "Why Customized Wardrobes?", "Customized wardrobe planning can help you:", [
                "Use available space efficiently", "Organize different storage categories",
                "Coordinate wardrobe design with your bedroom", "Select suitable finishes", "Consider accessibility"], ""),
        ],
        faq=[6, 3],
        cta="Plan Your Custom Wardrobe",
        related=["bedroom-design", "modular-kitchen", "home-interiors"],
    ),
    dict(
        slug="false-ceiling", name="False Ceiling", icon="ceiling", img="false-ceiling", est=None,
        short="Decorative and functional ceiling design concepts for residential and commercial spaces.",
        meta_title="False Ceiling Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Discover false ceiling design solutions in Visakhapatnam for bedrooms, living rooms, homes, and commercial spaces with Vanessa Interiors.",
        h1="Elegant False Ceiling Designs for Modern Interiors",
        intro=[
            "A false ceiling can influence the visual appearance of a room while supporting lighting and design requirements.",
            "Vanessa Interiors offers false ceiling design solutions in Visakhapatnam for residential and commercial interiors.",
            "We help clients explore ceiling concepts based on their space, preferred design style, lighting requirements, and project specifications.",
        ],
        blocks=[
            ("cards", "Our False Ceiling Services", [
                ("Gypsum Ceiling Designs", "Explore gypsum-based ceiling concepts for suitable applications.", None),
                ("Modern False Ceilings", "Contemporary designs that coordinate with modern interior styles.", None),
                ("Cove Lighting Concepts", "Explore indirect lighting arrangements where appropriate for the design.", None),
                ("Bedroom False Ceilings", "Ceiling concepts designed to complement bedroom interiors.", "bedroom-design"),
                ("Living Room False Ceilings", "Decorative ceiling solutions for living spaces.", "living-room-design"),
                ("Commercial Ceiling Solutions", "Ceiling design concepts for suitable office and commercial environments.", "commercial-interiors"),
            ]),
            ("checklist", "Important Design Considerations", "False ceiling selection depends on:", [
                "Ceiling height", "Lighting requirements", "Room dimensions", "Material suitability",
                "Electrical planning", "Maintenance requirements"],
             "Final specifications should be evaluated for the particular project."),
        ],
        faq=[4, 3],
        cta="Explore False Ceiling Designs",
        related=["living-room-design", "bedroom-design", "office-interiors"],
    ),
    dict(
        slug="office-interiors", name="Office Interiors", icon="office", img="office-interiors", est=None,
        short="Professional workspace designs that support your business environment.",
        meta_title="Office Interior Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Vanessa Interiors offers professional office interior design services in Visakhapatnam, including workspaces, reception areas, cabins, and meeting rooms.",
        h1="Professional Office Interiors Designed for Your Business",
        intro=[
            "Your office should support the way your team works while reflecting your business identity.",
            "Vanessa Interiors provides customized office interior design solutions in Visakhapatnam for businesses seeking functional and visually consistent workspaces.",
            "We consider your office layout, furniture requirements, workflow, and design preferences when developing interior concepts.",
        ],
        blocks=[
            ("cards", "Our Office Interior Services", [
                ("Corporate Office Interiors", "Professional design solutions for corporate workspaces.", None),
                ("Small Office Interiors", "Space-conscious interior planning for smaller office environments.", None),
                ("Reception Area Design", "Create a professional first impression with customized reception concepts.", None),
                ("Cabin Interiors", "Design private workspaces with suitable furniture and layout planning.", None),
                ("Workstation Planning", "Explore workstation arrangements based on available space and team requirements.", None),
                ("Meeting Room Interiors", "Plan meeting spaces with consideration for furniture, lighting, and functionality.", None),
                ("Office Storage Solutions", "Customized storage planning for documents, equipment, and office needs.", None),
            ]),
            ("checklist", "Our Office Design Approach", "We focus on:", [
                "Space utilization", "Employee movement", "Furniture layout", "Lighting", "Storage",
                "Brand identity", "Functional requirements"], ""),
        ],
        faq=[4, 3],
        cta="Plan Your Office Interiors",
        related=["commercial-interiors", "false-ceiling", "turnkey-interiors"],
    ),
    dict(
        slug="commercial-interiors", name="Commercial Interiors", icon="store", img="commercial-interiors", est=None,
        short="Customized interior solutions for commercial properties and business spaces.",
        meta_title="Commercial Interior Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Explore customized commercial interior design services in Visakhapatnam with Vanessa Interiors for offices, retail spaces, showrooms, and businesses.",
        h1="Commercial Interiors Designed Around Your Business",
        intro=[
            "Commercial spaces need to balance design, operational requirements, customer experience, and business identity.",
            "Vanessa Interiors offers commercial interior design solutions in Visakhapatnam for businesses looking to create functional and visually appealing environments.",
            "We discuss the property's layout, business objectives, design preferences, and execution requirements to develop a suitable interior approach.",
        ],
        blocks=[
            ("cards", "Our Commercial Interior Services", [
                ("Retail Interiors", "Design concepts for retail environments, display areas, and customer movement.", None),
                ("Showroom Interiors", "Customized planning for product presentation and brand experience.", None),
                ("Restaurant Interiors", "Interior concepts that consider customer experience, layout, and design requirements.", None),
                ("Hospitality Interiors", "Design solutions for suitable hospitality environments.", None),
                ("Commercial Office Interiors", "Professional office spaces designed around business needs.", "office-interiors"),
                ("Reception & Display Areas", "Customized concepts for welcoming and functional business spaces.", None),
            ]),
            ("steps", "Commercial Interior Design Process", [
                ("Step 1", "Understand business requirements."), ("Step 2", "Review available space."),
                ("Step 3", "Discuss design direction."), ("Step 4", "Develop design concepts."),
                ("Step 5", "Finalize project scope."), ("Step 6", "Coordinate execution according to the agreement."),
            ]),
        ],
        faq=[4, 3],
        cta="Discuss Your Commercial Interior Project",
        related=["office-interiors", "renovation", "turnkey-interiors"],
    ),
    dict(
        slug="villa-interiors", name="Villa Interiors", icon="villa", img="villa-interiors", est="completeHome",
        short="Luxury and personalized interiors designed for villas.",
        meta_title="Villa Interior Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Vanessa Interiors offers luxury and customized villa interior design services in Visakhapatnam. Create personalized interiors for modern villas.",
        h1="Luxury Villa Interiors Designed for Modern Living",
        intro=[
            "A villa provides opportunities for personalized interior planning across multiple rooms, levels, and functional areas.",
            "Vanessa Interiors offers customized villa interior design services in Visakhapatnam, helping homeowners develop cohesive interiors that suit the property's layout and lifestyle.",
            "Our design approach focuses on combining luxury aesthetics, practical space planning, and coordinated design elements.",
        ],
        link_sentence=("Design comfortable and personalized spaces with our {bedroom interior design services}.", "bedroom-design"),
        blocks=[
            ("cards", "Our Villa Interior Services", [
                ("Living Room Interiors", "Elegant living spaces designed around the villa's layout and requirements.", "living-room-design"),
                ("Master Bedroom Interiors", "Personalized bedroom concepts with suitable furniture and storage planning.", "bedroom-design"),
                ("Modular Kitchen", "Customized kitchen designs for villa layouts.", "modular-kitchen"),
                ("Dining Area Interiors", "Design concepts for dining spaces that coordinate with the rest of the home.", None),
                ("Staircase Area Design", "Explore suitable design and finish concepts for staircase areas.", None),
                ("Wardrobes & Storage", "Customized storage solutions for different rooms.", "wardrobes"),
                ("False Ceiling", "Ceiling concepts that complement the villa's interior design.", "false-ceiling"),
                ("Complete Villa Interiors", "Coordinate interior requirements across the property based on the agreed project scope.", None),
            ]),
            ("checklist", "Why Choose Vanessa Interiors for Villas?", "", [
                "Luxury design focus", "Customized interiors", "Residential project experience",
                "Own execution team", "Complete interior planning", "Project-specific consultation"], ""),
        ],
        faq=[7, 3, 5],
        cta="Plan Your Villa Interiors",
        related=["bedroom-design", "modular-kitchen", "turnkey-interiors"],
    ),
    dict(
        slug="renovation", name="Renovation Services", icon="hammer", img="renovation", est=None,
        short="Interior improvement and renovation solutions for existing properties.",
        meta_title="Home Renovation Services in Visakhapatnam | Vanessa Interiors",
        meta_desc="Upgrade your home or commercial space with interior renovation services in Visakhapatnam from Vanessa Interiors. Customized renovation solutions.",
        h1="Transform Your Existing Space with Interior Renovation",
        intro=[
            "Over time, your interior requirements may change. You may want to update your kitchen, improve storage, refresh a bedroom, or redesign an entire space.",
            "Vanessa Interiors offers interior renovation solutions in Visakhapatnam for residential and commercial properties.",
            "We discuss the existing space, renovation requirements, design preferences, and execution scope to help plan suitable improvements.",
        ],
        blocks=[
            ("cards", "Our Renovation Services", [
                ("Home Interior Renovation", "Update selected interior areas or coordinate a broader home renovation project.", "home-interiors"),
                ("Kitchen Renovation", "Explore improvements to kitchen layouts, storage, finishes, and design elements.", "modular-kitchen"),
                ("Bedroom Renovation", "Refresh bedroom interiors through updated design and storage solutions.", "bedroom-design"),
                ("Living Room Renovation", "Redesign selected living room elements to improve appearance and functionality.", "living-room-design"),
                ("Wardrobe Renovation", "Explore wardrobe redesign or replacement options where suitable.", "wardrobes"),
                ("False Ceiling Updates", "Discuss ceiling improvements based on existing conditions and project requirements.", "false-ceiling"),
                ("Commercial Renovation", "Interior improvement solutions for suitable commercial properties.", "commercial-interiors"),
            ]),
            ("chain", "Our Renovation Process", ["Site Assessment", "Requirements", "Design Discussion", "Scope & Estimate", "Execution", "Completion"],
             "Renovation timelines and costs depend on existing conditions, materials, and the agreed scope."),
        ],
        faq=[9, 3],
        cta="Discuss Your Renovation Project",
        related=["modular-kitchen", "home-interiors", "commercial-interiors"],
    ),
    dict(
        slug="turnkey-interiors", name="Turnkey Interiors", icon="key", img="turnkey-interiors", est="completeHome",
        short="Coordinated interior design and execution services based on the agreed project scope.",
        meta_title="Turnkey Interior Designers in Visakhapatnam | Vanessa Interiors",
        meta_desc="Vanessa Interiors provides turnkey interior design and execution solutions in Visakhapatnam for homes, villas, apartments, offices, and commercial spaces.",
        h1="Turnkey Interiors from Design to Execution",
        intro=[
            "Managing different interior activities can be challenging when design, materials, and execution need to be coordinated.",
            "Vanessa Interiors offers turnkey interior solutions in Visakhapatnam for clients looking for coordinated interior design and execution services.",
            "Our turnkey approach is based on the agreed project scope, design requirements, materials, and execution responsibilities.",
        ],
        blocks=[
            ("cards", "Our Turnkey Interior Services", [
                ("Residential Turnkey Interiors", "Complete interior solutions for homes, apartments, and villas.", "home-interiors"),
                ("Villa Turnkey Interiors", "Coordinated interior design and execution for suitable villa projects.", "villa-interiors"),
                ("Apartment Turnkey Interiors", "Customized interior solutions for apartment owners.", None),
                ("Office Turnkey Interiors", "Design and execution coordination for office environments.", "office-interiors"),
                ("Commercial Turnkey Projects", "Interior solutions based on commercial property requirements.", "commercial-interiors"),
                ("Design & Execution Coordination", "Coordinate agreed project activities from design planning to execution.", None),
            ]),
            ("steps", "Our Turnkey Process", [
                ("Consultation", "Discuss the property and project requirements."),
                ("Planning", "Review the layout and identify interior needs."),
                ("Design", "Develop suitable design concepts and discuss materials."),
                ("Scope Finalization", "Agree on deliverables, specifications, and responsibilities."),
                ("Execution", "Coordinate the agreed work using our team."),
                ("Completion", "Review the project and address applicable finishing requirements."),
            ]),
            ("checklist", "Why Choose Turnkey Interiors?", "", [
                "Coordinated project approach", "Customized design solutions", "Residential and commercial services",
                "Own execution team", "Project-specific planning"], ""),
        ],
        faq=[10, 5, 3],
        cta="Discuss Your Turnkey Interior Project",
        related=["home-interiors", "villa-interiors", "office-interiors"],
    ),
]
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

# ---------------------------------------------------------------- FAQs (PAGE 23)
FAQS = {
    1: ("What services does Vanessa Interiors offer?", "Vanessa Interiors offers luxury and customized interior design services for residential and commercial properties, including home interiors, modular kitchens, bedrooms, living rooms, wardrobes, false ceilings, offices, villas, renovation, and turnkey interiors."),
    2: ("Where is Vanessa Interiors located?", "Our office is located at Aruna Inn, 49-24-16, Sankara Matam Road, Madhuranagar, Akkayyapalem, Visakhapatnam, Andhra Pradesh – 530016."),
    3: ("What is the minimum budget for an interior project?", "Our projects start from ₹5 Lakhs. The final cost depends on the property, design requirements, materials, and project scope."),
    4: ("Do you provide both residential and commercial interiors?", "Yes. We offer interior design solutions for residential and commercial properties."),
    5: ("Do you have your own execution team?", "Yes. Vanessa Interiors has its own workers to support interior execution."),
    6: ("Do you provide customized interior designs?", "Yes. We develop customized design solutions based on the client's preferences and project requirements."),
    7: ("Do you offer villa interior design?", "Yes. We provide customized villa interior design solutions for suitable projects."),
    8: ("Do you provide modular kitchen design?", "Yes. We offer customized modular kitchen design solutions, including layout planning and storage concepts."),
    9: ("Do you provide renovation services?", "Yes. We offer renovation-related interior solutions based on the property's condition and agreed scope."),
    10: ("Do you offer turnkey interiors?", "Yes. We provide turnkey interior solutions covering agreed design and execution requirements."),
    11: ("Do you provide warranty or post-project support?", "Yes. Warranty and post-project support are available according to the applicable project terms."),
    12: ("How can I contact Vanessa Interiors?", "You can contact us through our website, phone number, or WhatsApp to discuss your interior project."),
}

# Home page FAQ preview (PAGE 1, SECTION 9)
HOME_FAQS = [
    ("What is the minimum budget for an interior project?", "Our interior projects start from ₹5 Lakhs, depending on the project scope and requirements."),
    ("Do you provide residential and commercial interiors?", "Yes. We provide interior design solutions for residential and commercial properties."),
    ("Where is Vanessa Interiors located?", "Our office is located at Aruna Inn, 49-24-16, Sankara Matam Road, Madhuranagar, Akkayyapalem, Visakhapatnam."),
    ("Do you provide customized interior designs?", "Yes. We offer customized interior design solutions based on client requirements."),
]

# ---------------------------------------------------------------- HOME: why choose (SECTION 4)
WHY = [
    ("award", "14 Years of Experience", "Our business has been operating since 2012, with experience in interior design and execution."),
    ("grid", "100+ Completed Projects", "Our portfolio includes completed interior projects. Explore our actual work to understand our design approach."),
    ("team", "50+ Team Members", "We have a team of 50+ members supporting our interior work and project requirements."),
    ("spark", "Luxury & Customized Designs", "We focus on personalized interiors that reflect the client's design preferences and functional needs."),
    ("tools", "In-House Execution Team", "We have our own workers to support project execution."),
    ("layers", "Residential & Commercial Expertise", "We provide interior solutions for homes, villas, offices, and commercial spaces."),
    ("shield", "Warranty & Post-Project Support", "We provide warranty and post-project support according to the applicable project terms."),
]

PROCESS = [
    ("Consultation", "Discuss your requirements, property details, design preferences, and budget."),
    ("Space Planning", "Understand the available space and plan suitable layouts."),
    ("Design Development", "Develop design concepts based on your preferences and project needs."),
    ("Material & Scope Finalization", "Discuss materials, finishes, specifications, and project deliverables."),
    ("Interior Execution", "Coordinate the agreed execution work using our team."),
    ("Project Completion", "Review the completed work and address applicable finishing and support requirements."),
]

# ---------------------------------------------------------------- PORTFOLIO (PAGES 15–19)
PORTFOLIO = [
    dict(slug="residential", name="Residential", img="home-interiors",
         card="Explore home interior design projects, including living rooms, bedrooms, kitchens, and storage solutions.",
         meta_title="Residential Interior Design Projects in Visakhapatnam | Vanessa Interiors",
         meta_desc="Explore residential interior design projects by Vanessa Interiors in Visakhapatnam, including homes, apartments, kitchens, bedrooms, and living rooms.",
         h1="Residential Interior Design Projects", h2="Homes Designed Around Everyday Living",
         intro=["Our residential portfolio showcases interior design and execution work for homes and other residential properties.",
                "Explore different design styles, space planning approaches, and interior details across our projects."],
         cats=["Complete Home Interiors", "Living Room Interiors", "Bedroom Interiors", "Modular Kitchens", "Wardrobes", "False Ceilings", "Apartment Interiors"],
         cta="Discuss Your Residential Project", service="Home Interiors"),
    dict(slug="commercial", name="Commercial", img="commercial-interiors",
         card="View office and commercial interior projects.",
         meta_title="Commercial Interior Design Projects in Visakhapatnam | Vanessa Interiors",
         meta_desc="Explore commercial interior design projects by Vanessa Interiors, including offices, retail spaces, and business environments in Visakhapatnam.",
         h1="Commercial Interior Design Projects", h2="Spaces Designed for Business Requirements",
         intro=["Our commercial portfolio showcases interior design and execution projects for business environments.",
                "Explore office layouts, commercial design elements, space planning, and project-specific finishes."],
         cats=["Office Interiors", "Retail Interiors", "Showroom Interiors", "Commercial Renovation", "Reception Areas"],
         cta="Discuss Your Commercial Project", service="Commercial Interiors"),
    dict(slug="villas", name="Villas", img="villa-interiors",
         card="Explore customized villa interiors and design concepts.",
         meta_title="Villa Interior Design Projects in Visakhapatnam | Vanessa Interiors",
         meta_desc="Explore luxury and customized villa interior design projects by Vanessa Interiors in Visakhapatnam.",
         h1="Villa Interior Design Projects", h2="Personalized Interiors for Villa Living",
         intro=["Our villa portfolio showcases customized interior design work for villa properties.",
                "Explore living rooms, bedrooms, kitchens, dining areas, and other spaces designed according to the property's layout and client preferences."],
         cats=["Luxury Villa Interiors", "Modern Villa Interiors", "Complete Villa Interiors", "Villa Living Rooms", "Villa Bedrooms", "Villa Kitchens"],
         cta="Plan Your Villa Interiors", service="Villa Interiors"),
    dict(slug="apartments", name="Apartments", img="apartments",
         card="Discover apartment interior projects designed around practical space planning.",
         meta_title="Apartment Interior Design Projects in Visakhapatnam | Vanessa Interiors",
         meta_desc="Explore customized apartment interior design projects by Vanessa Interiors in Visakhapatnam, including kitchens, bedrooms, and living rooms.",
         h1="Apartment Interior Design Projects", h2="Functional & Stylish Apartment Interiors",
         intro=["Apartment interiors require thoughtful planning to make the best use of available space.",
                "Our apartment portfolio showcases interior design work for different layouts, design preferences, and residential requirements."],
         cats=["2BHK Apartment Interiors", "3BHK Apartment Interiors", "Living Room Designs", "Modular Kitchens", "Bedroom Interiors", "Storage Solutions"],
         cta="Design Your Apartment Interiors", service="Home Interiors"),
]

# ---------------------------------------------------------------- BLOG (PAGE 21)
BLOG_CATEGORIES = ["Home Interior Ideas", "Modular Kitchen", "Bedroom Design", "Living Room Design", "Villa Interiors",
                   "Office Interiors", "Commercial Interiors", "Renovation", "Interior Budget Planning", "Interior Design Trends"]
# (topic, focus keyword, category, related page, related label)
BLOG_TOPICS = [
    ("How to Choose the Right Interior Designer in Visakhapatnam", "Interior Designer in Visakhapatnam", "Home Interior Ideas", "services.html", "Our Services"),
    ("How Much Does Home Interior Design Cost in Vizag?", "Home Interior Cost in Vizag", "Interior Budget Planning", "cost-estimator.html", "Cost Estimator"),
    ("10 Modern Modular Kitchen Design Ideas", "Modular Kitchen Design Ideas", "Modular Kitchen", "services/modular-kitchen.html", "Modular Kitchen"),
    ("How to Plan a Luxury Home Interior", "Luxury Home Interiors", "Home Interior Ideas", "services/home-interiors.html", "Home Interiors"),
    ("Best Interior Design Ideas for 2BHK Apartments", "2BHK Interior Design", "Home Interior Ideas", "portfolio/apartments.html", "Apartment Projects"),
    ("Modern Living Room Design Ideas for Indian Homes", "Modern Living Room Design", "Living Room Design", "services/living-room-design.html", "Living Room Design"),
    ("How to Choose the Right Wardrobe Design", "Wardrobe Design Ideas", "Bedroom Design", "services/wardrobes.html", "Wardrobes"),
    ("Bedroom Interior Design Ideas for Modern Homes", "Bedroom Interior Design", "Bedroom Design", "services/bedroom-design.html", "Bedroom Design"),
    ("False Ceiling Design Ideas for Living Rooms", "Living Room False Ceiling", "Living Room Design", "services/false-ceiling.html", "False Ceiling"),
    ("How to Plan a Villa Interior Design Project", "Villa Interior Design", "Villa Interiors", "services/villa-interiors.html", "Villa Interiors"),
    ("Home Renovation Checklist for Homeowners", "Home Renovation Checklist", "Renovation", "services/renovation.html", "Renovation Services"),
    ("Modern Office Interior Design Ideas", "Office Interior Design", "Office Interiors", "services/office-interiors.html", "Office Interiors"),
    ("Residential vs Commercial Interior Design", "Interior Design Services", "Commercial Interiors", "services/commercial-interiors.html", "Commercial Interiors"),
    ("What Is Turnkey Interior Design?", "Turnkey Interior Design", "Home Interior Ideas", "services/turnkey-interiors.html", "Turnkey Interiors"),
    ("How to Choose Interior Colors for Your Home", "Interior Color Ideas", "Interior Design Trends", "services/home-interiors.html", "Home Interiors"),
    ("Modular Kitchen Storage Planning Guide", "Kitchen Storage Ideas", "Modular Kitchen", "services/modular-kitchen.html", "Modular Kitchen"),
    ("How to Plan Interior Lighting for Your Home", "Interior Lighting Design", "Interior Design Trends", "services/false-ceiling.html", "False Ceiling"),
    ("Luxury vs Minimalist Interior Design", "Luxury Interior Design", "Interior Design Trends", "services/home-interiors.html", "Home Interiors"),
    ("Questions to Ask Before Hiring an Interior Designer", "Hiring an Interior Designer", "Home Interior Ideas", "faqs.html", "FAQs"),
    ("How to Plan an Interior Project Budget", "Interior Project Budget", "Interior Budget Planning", "cost-estimator.html", "Cost Estimator"),
]

GALLERY_CATS = ["Living Room", "Bedroom", "Modular Kitchen", "Wardrobes", "False Ceiling", "Villa Interiors", "Office Interiors", "Commercial Interiors"]
