from django.db import migrations


SERVICES = [
    ('code', 'Custom Software', 'Software Personalizat',
     'Bespoke solutions designed around your unique business challenges and goals.',
     'Soluții create în jurul provocărilor și obiectivelor unice ale afacerii tale.'),
    ('globe', 'Web Development', 'Dezvoltare Web',
     'Fast, accessible sites with WordPress, Jekyll or fully custom builds.',
     'Site-uri rapide și accesibile cu WordPress, Jekyll sau soluții custom.'),
    ('shield', 'IT Consulting', 'Consultanță IT',
     'Expert guidance on strategy, digital transformation and IT optimisation.',
     'Îndrumare pe strategie, transformare digitală și optimizare IT.'),
    ('server', 'Infrastructure', 'Infrastructură',
     'Design and run on-prem or cloud infrastructure, databases and networks.',
     'Proiectăm și întreținem infrastructură on-prem sau cloud, baze de date și rețele.'),
    ('plug', 'Software Integration', 'Integrare Software',
     'Deploy and connect open-source CRMs, ERPs and collaboration suites.',
     'Implementăm și conectăm CRM-uri, ERP-uri și suite de colaborare open-source.'),
    ('wrench', 'Hosting & Maintenance', 'Găzduire & Mentenanță',
     'Reliable hosting, monitoring and maintenance to keep you running smoothly.',
     'Găzduire fiabilă, monitorizare și mentenanță ca totul să meargă lin.'),
]

AI_SERVICES = [
    ('bot', 'Intelligent Chatbots', 'Chatboți Inteligenți',
     'Assistants that understand natural language and help customers 24/7.',
     'Asistenți care înțeleg limbajul natural și ajută clienții 24/7.', 'RAG', 'RAG'),
    ('mic', 'Voice Assistants', 'Asistenți Vocali',
     'Conversational voice interfaces for natural, hands-free interaction.',
     'Interfețe vocale conversaționale pentru interacțiune naturală.', 'Voice', 'Voce'),
    ('chart', 'Predictive Analytics', 'Analiză Predictivă',
     'Uncover patterns and forecast trends to drive informed decisions.',
     'Descoperă tipare și anticipează tendințe pentru decizii informate.', 'ML', 'ML'),
]

PROJECTS = [
    ('globe', 'web', 'E-commerce', 'Custom E-commerce Suite', 'Suită E-commerce',
     'Online platform with integrated payments for niche service providers.',
     'Platformă online cu procesare de plăți pentru furnizori de servicii nișate.'),
    ('bot', 'ai', 'AI', 'Documentation Chatbot', 'Chatbot Documentație',
     'AI assistant that helps users navigate complex documentation.',
     'Asistent AI care ajută utilizatorii să navigheze documentație complexă.'),
    ('cloud', 'cloud', 'Cloud', 'Self-hosted Cloud Suite', 'Suită Cloud Self-hosted',
     'Secure private cloud with file sharing and collaboration tools.',
     'Cloud privat securizat cu partajare de fișiere și colaborare.'),
    ('layers', 'software', 'App', 'Contract Management App', 'Gestionare Contracte',
     'Streamlined contract lifecycle with automated workflows and alerts.',
     'Ciclu de viață al contractelor cu fluxuri și alerte automate.'),
    ('globe', 'web', 'WordPress', 'WordPress Websites', 'Site-uri WordPress',
     'Custom WordPress builds with optimised performance and SEO.',
     'Build-uri WordPress custom cu performanță și SEO optimizate.'),
    ('zap', 'software', 'NFC', 'NFC Business Cards', 'Cărți de Vizită NFC',
     'Digital business cards with NFC for instant contact sharing.',
     'Cărți de vizită digitale cu NFC pentru partajare instant.'),
]


def seed(apps, schema_editor):
    Service = apps.get_model('core', 'Service')
    AIService = apps.get_model('core', 'AIService')
    Project = apps.get_model('core', 'Project')

    for i, (icon, t_en, t_ro, d_en, d_ro) in enumerate(SERVICES):
        Service.objects.create(icon=icon, title_en=t_en, title_ro=t_ro,
                               desc_en=d_en, desc_ro=d_ro, order=i)

    for i, (icon, t_en, t_ro, d_en, d_ro, b_en, b_ro) in enumerate(AI_SERVICES):
        AIService.objects.create(icon=icon, title_en=t_en, title_ro=t_ro,
                                 desc_en=d_en, desc_ro=d_ro,
                                 badge_en=b_en, badge_ro=b_ro, order=i)

    for i, (icon, cat, tag, t_en, t_ro, d_en, d_ro) in enumerate(PROJECTS):
        Project.objects.create(icon=icon, category=cat, tag=tag, title_en=t_en,
                               title_ro=t_ro, desc_en=d_en, desc_ro=d_ro, order=i)


def unseed(apps, schema_editor):
    for model in ('Service', 'AIService', 'Project'):
        apps.get_model('core', model).objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
