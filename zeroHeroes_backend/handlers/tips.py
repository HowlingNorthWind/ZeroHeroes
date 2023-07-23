import random

activity_tips = {
    'Nature Noshing': [
        'Remember to bring reusable utensils and containers for your food.',
        'Clean up after yourself to keep the natural environment pristine.',
        'Try to prepare plant-based meals to reduce your carbon footprint.',
        'Explore local biodiversity while enjoying your meal.',
        'Try to source your food from local, sustainable sources.'
    ],
    'Waste Warriors': [
        'Always sort your waste correctly.',
        'Try to reduce your waste production by using reusable items.',
        'Educate others about the importance of waste management.',
        'Research local recycling guidelines.',
        'Consider starting a community waste reduction initiative.'
    ],
    'Upcycle Palooza': [
        'Be creative and think of new uses for old items.',
        'Share your upcycling projects to inspire others.',
        'Before throwing something away, consider if it can be upcycled.',
        'Consider the lifecycle of products before you buy them.',
        'Educate yourself about materials and their potential for reuse.'
    ],
    'Compost Champions': [
        'Turn your organic waste into nutrient-rich compost.',
        'Use your compost to enrich the soil in your garden.',
        'Encourage others to start composting at home.',
        'Understand what can and cannot be composted.',
        'Consider worm composting as an indoor option.'
    ],
    'Canopy Crusaders': [
        'Plant native trees to support local biodiversity.',
        'Learn about the importance of trees for the climate.',
        'Join a local tree-planting event or organize your own.',
        'Promote the value of urban green spaces.',
        'Learn to identify local tree species.'
    ],
    'Marvelous Market': [
        'Support local producers by buying their products.',
        'Bring your own bags and containers when shopping.',
        'Choose organic and sustainably-produced items.',
        'Try to minimize food waste by planning meals and buying only what you need.',
        'Learn about the seasonality of local produce.'
    ],
    'Stream Safari': [
        'Be mindful of the fragile ecosystem of streams.',
        'Do not litter and clean up any trash you find.',
        'Learn about local aquatic species and their role in the ecosystem.',
        'Consider participating in a stream restoration project.',
        'Learn about the impact of water pollution on local wildlife.'
    ],
    'Move Mitigation': [
        'Use public transport, bike or walk whenever possible.',
        'If you have to drive, try to carpool with others.',
        'Consider switching to an electric or hybrid vehicle.',
        'Plan your routes to minimize fuel consumption.',
        'Support initiatives for sustainable transport in your community.'
    ],
    'Litter Quest': [
        'Always pick up your litter and dispose of it properly.',
        'Organize a litter collection event in your community.',
        'Consider using a trash grabbing tool to protect your back.',
        'Educate others about the impact of litter on wildlife.',
        'Promote the use of trash cans and recycling bins in public spaces.'
    ],
    'Beach Beautification': [
        'Clean up trash on the beach to protect marine life.',
        'Use biodegradable sunscreen to prevent water pollution.',
        'Respect all beach rules to preserve its natural beauty.',
        'Educate yourself and others about local marine life.',
        'Support local initiatives for beach conservation.'
    ]
}

def get_tips(activities):
    return  [random.choice(activity_tips[activity]) for activity in activities]