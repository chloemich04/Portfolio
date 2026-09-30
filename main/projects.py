"""Portfolio entries curated from public repository READMEs and source trees.

Add a dictionary here to publish another card. Set featured=True to show it
on the homepage too. Keep descriptions specific to implemented work.
"""

PROJECTS = [
    {
        "title": "Atlas", "category": "Backend development", "label": "ATLAS / TRACKING API",
        "headline": "Everything in its place.", "caption": "ORGANIZE. SEARCH. DISCOVER.", "theme": "atlas",
        "description": "A tracking API with JWT authentication, item management, categories, tags, search, and pagination. Built with database migrations and a Pytest test suite.",
        "tags": ["Python", "FastAPI", "PostgreSQL", "Docker"],
        "url": "https://github.com/chloemich04/Atlas", "featured": True,
    },
    {
        "title": "Cyber Threat Intelligence & Anomaly Platform", "category": "Cybersecurity · Data visualization",
        "label": "THREAT INTELLIGENCE / DASHBOARD", "headline": "Making threats visible.",
        "caption": "EXPLORE. VISUALIZE. INVESTIGATE.", "theme": "cyber",
        "description": "A React and Django platform for exploring cyber-threat data, with geographic visualizations, threat listings, forecast views, and PDF dashboard exports.",
        "tags": ["React", "JavaScript", "Python", "Django"],
        "url": "https://github.com/chloemich04/Cyber-Threat-Intelligence-Anomaly-Platform", "featured": True,
    },
    {
        "title": "SkillForge", "category": "Full-stack development", "label": "SKILLFORGE / LEARNING TRACKER",
        "headline": "Build skills. Log progress.", "caption": "LEARN. PRACTICE. REPEAT.", "theme": "forge",
        "description": "A skill and activity tracking project pairing a React and TypeScript interface with an ASP.NET Core API. Includes endpoints and data models for managing skills and activity logs.",
        "tags": ["C#", "ASP.NET Core", "React", "TypeScript"],
        "url": "https://github.com/chloemich04/SkillForge", "featured": False,
    },
    {
        "title": "Mini Shop", "category": "E-commerce · Coursework", "label": "MINI SHOP / VIDEO GAME STORE",
        "headline": "Browse. Cart. Checkout.", "caption": "A FULL-STACK SHOPPING FLOW.", "theme": "shop",
        "description": "An educational video-game shop with authentication, product management, a shopping cart, and order history. A FastAPI backend connects to PostgreSQL; checkout uses demo data without real payments.",
        "tags": ["Python", "FastAPI", "PostgreSQL", "JavaScript"],
        "url": "https://github.com/chloemich04/CSCE-500-Project", "featured": False,
    },
    {
        "title": "DeepCore", "category": "Systems programming · Algorithms", "label": "DEEPCORE / PROGRAMMING FOUNDATIONS",
        "headline": "Under the hood.", "caption": "STRUCTURES. ALGORITHMS. SYSTEMS.", "theme": "core",
        "description": "A collection of programming fundamentals: data structures and sorting algorithms in C, a mini shell, a C calculator, and a browser-based sorting visualizer. Includes tests for the data structures and sorting implementations.",
        "tags": ["C", "Data structures", "Algorithms", "JavaScript"],
        "url": "https://github.com/chloemich04/DeepCore", "featured": False,
    },
    {
        "title": "Scamming Codebook: Data Analysis", "category": "Research · Data analysis", "label": "SCAMMING CODEBOOK / RESEARCH",
        "headline": "Patterns behind the data.", "caption": "COLLECT. EXAMINE. UNDERSTAND.", "theme": "research",
        "description": "Data collection and analysis supporting research into blackmail scams for the Scamming Codebook. The repository brings together Python scripts and datasets used to prepare the research project and paper.",
        "tags": ["Python", "Data collection", "Research"],
        "url": "https://github.com/chloemich04/Data-Analysis", "featured": False,
    },
    {
        "title": "Calculator", "category": "Frontend fundamentals", "label": "CALCULATOR / WEB BASICS",
        "headline": "Make it add up.", "caption": "SMALL PROJECT. CORE SKILLS.", "theme": "calculator",
        "description": "A basic browser calculator built with HTML, CSS, and JavaScript. A focused project bringing page structure, styling, and interactive logic together.",
        "tags": ["HTML", "CSS", "JavaScript"],
        "url": "https://github.com/chloemich04/Calculator", "featured": False,
    },
    {
        "title": "Anime Tracker", "category": "Web application · Team project", "label": "TOR / ANIME TRACKER",
        "headline": "Your next obsession.", "caption": "DISCOVER. TRACK. CONNECT.", "theme": "anime",
        "description": "A space for anime fans to track favorite series, discover something new, and connect through discussions and polls.",
        "tags": ["Discovery", "Community", "Tracking"],
        "url": "https://gitlab.com/ull-gitlab/sp25-team-projects/sp25-team-011/tor-anime", "featured": True,
    },
    {
        "title": "This portfolio", "category": "Web development · Personal project", "label": "PERSONAL PORTFOLIO / DJANGO",
        "headline": "A little corner of the web.", "caption": "BUILT WITH CODE & CURIOSITY.", "theme": "portfolio",
        "description": "A home for my work and the story behind it. Built with reusable Django templates, responsive layouts, and accessible navigation.",
        "tags": ["Python", "Django", "HTML & CSS"],
        "url": "https://github.com/chloemich04/Portfolio", "featured": True,
    },
]
