from django.shortcuts import render

# Create your views here.

def home(request):    
    context = {
    # Personal Information
    
    # Professional Summary
    'description': 'is a dedicated front-end web developer with a strong foundation in CSS, HTML, and JavaScript. '
                   'Passionate about crafting visually appealing and user-friendly web interfaces, he brings expertise in debugging and website optimization. '
                   'With a commitment to continuous improvement, he seeks to contribute innovative solutions to the field of information technology.',
    
    # Skills for SEO or Display
    'skills': 'Front-End Development, Website Optimization, Debugging, WordPress, Adobe Software Packages, CSS, HTML, GIT, Digital Animation, Customer Service',

    # Work Experience
    'work_experience': [
        {
            'role': 'Front-End Web Developer',
            'company': 'FOTOBOSS',
            'location': 'Seoul, Korea',
            'duration': 'May 2022 – August 2023',
            'responsibilities': [
                'Designed and implemented responsive website interfaces for mobile, desktop, and tablets.',
                'Utilized HTML5, CSS3, and object-oriented JavaScript to create dynamic web applications.',
                'Led project and web strategic planning for a collaborative team environment.',
                'Conducted thorough website testing to ensure quality across multiple browsers.',
                'Developed frameworks to enhance functionality and performance.'
            ]
        }
    ],
    
    # Education
    'education': [
        {
            'degree': 'Information Technology',
            'institution': 'Integrated Innovation and Hospitality College',
            'location': 'Caloocan, Philippines',
            'duration': 'June 2023 – Present',
        }
    ],
    
    # Interests and Hobbies
    'hobbies': 'Photography, Music, Cycling',

    # Page Metadata (Optional)
    'page_title': 'Mark Anthony Ocampos - Front-End Web Developer Resume',
    'page_description': 'Explore the professional background, skills, and experiences of Mark Anthony Ocampos, '
                        'a front-end web developer with a passion for user-friendly web design and optimization.',
    'canonical_url': 'https://www.yourwebsite.com/college-portal',
    'page_url': 'https://www.yourwebsite.com/mark-anthony-resume',
}
    return render(request, 'home.html', context)
