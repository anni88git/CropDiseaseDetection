"""
Kṣetrin - Agronomic Knowledge Base
Detailed symptoms, remedies, treatments, and prevention guidelines for all 38 classes.
"""

DISEASE_DB = {
    'Apple___Apple_scab': {
        'crop': 'Apple',
        'condition': 'Apple Scab',
        'is_healthy': False,
        'severity': 'Moderate to High',
        'pathogen': 'Venturia inaequalis (Fungus)',
        'description': 'A serious fungal disease causing olive-green to black velvety spots on leaves and scabby lesions on fruits, reducing fruit quality and tree vigor.',
        'symptoms': [
            'Olive-green to dark brown circular spots with velvety margins on upper leaf surfaces',
            'Leaves turn yellow and drop prematurely',
            'Cork-like brown scabs on developing fruit causing cracking and distortion'
        ],
        'organic_treatment': [
            'Apply sulfur or copper soap fungicide at bud break and early leaf emergence',
            'Rake and destroy fallen leaves in autumn to eliminate overwintering spores',
            'Prune tree canopy during dormancy to maximize sunlight penetration and air circulation'
        ],
        'chemical_treatment': [
            'Captan 50WP (2-3 lbs/acre) or Myclobutanil (Rally 40WSP)',
            'Mancozeb during early vegetative stage before bloom'
        ],
        'prevention': [
            'Plant scab-resistant cultivars (e.g., Liberty, Enterprise, Honeycrisp)',
            'Avoid overhead irrigation; use drip watering around the root zone'
        ]
    },
    'Apple___Black_rot': {
        'crop': 'Apple',
        'condition': 'Black Rot (Frogeye Leaf Spot)',
        'is_healthy': False,
        'severity': 'High',
        'pathogen': 'Botryosphaeria obtusa (Fungus)',
        'description': 'Causes purple-bordered frogeye leaf spots, cankers on branches, and severe rotting of mature fruit, often starting near the calyx.',
        'symptoms': [
            'Small purple specks on leaves that enlarge into circular spots with grey centers (frogeye)',
            'Black sunken cankers on limbs with dead bark',
            'Brown rot with concentric rings on fruits turning mummified and coal-black'
        ],
        'organic_treatment': [
            'Prune out dead branches, twigs, and mummified fruit 15 cm below visible infection',
            'Spray Bordeaux mixture (copper sulfate + hydrated lime) prior to bud break',
            'Apply bio-fungicides containing Bacillus subtilis'
        ],
        'chemical_treatment': [
            'Thiophanate-methyl (Topsin M) combined with Captan',
            'Flint Extra (Trifloxystrobin) applied from pink bud stage through cover sprays'
        ],
        'prevention': [
            'Sanitize pruning tools with 70% isopropyl alcohol between cuts',
            'Promptly remove fire blight strikes and insect-damaged branches'
        ]
    },
    'Apple___Cedar_apple_rust': {
        'crop': 'Apple',
        'condition': 'Cedar Apple Rust',
        'is_healthy': False,
        'severity': 'Moderate',
        'pathogen': 'Gymnosporangium juniperi-virginianae (Fungus)',
        'description': 'A heteroecious rust fungus requiring both Apple and Eastern Red Cedar/Juniper hosts to complete its two-year life cycle.',
        'symptoms': [
            'Bright yellow-orange or reddish spots on upper leaf surfaces in late spring',
            'Small tube-like raised pustules (aecia) on the underside of leaves',
            'Yellowish lesions on the calyx end of fruit, causing premature fruit drop'
        ],
        'organic_treatment': [
            'Eradicate or prune galls from nearby Eastern red cedar/juniper trees within 1 km',
            'Apply wettable sulfur or liquid copper spray when cedar galls form gelatinous orange horns',
            'Neem oil applications to protect young emerging foliage'
        ],
        'chemical_treatment': [
            'Myclobutanil (Immunox / Rally) sprayed at tight cluster through petal fall',
            'Propiconazole or Mancozeb protective fungicide schedule'
        ],
        'prevention': [
            'Plant rust-immune varieties such as Prima, Priscilla, or Freedom',
            'Maintain at least 500 meters separation from Juniperus species'
        ]
    },
    'Apple___Healthy': {
        'crop': 'Apple',
        'condition': 'Healthy Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'The apple foliage shows vibrant chlorophyll distribution, clean leaf margins, and intact vascular structures without fungal, bacterial, or pest damage.',
        'symptoms': [
            'Deep green uniform color across the leaf lamina',
            'Crisp, unblemished margins with no discoloration or curling',
            'Healthy petiole and vigorous vegetative growth'
        ],
        'organic_treatment': [
            'Maintain regular balanced organic compost and mulch layer',
            'Foliar spray with diluted seaweed extract for micronutrient vitality'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Continue integrated pest management (IPM) scouting',
            'Ensure consistent soil moisture and avoid waterlogging'
        ]
    },
    'Blueberry___Healthy': {
        'crop': 'Blueberry',
        'condition': 'Healthy Bush Foliage',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Blueberry leaves are clean, firm, and exhibit characteristic healthy wax cuticle with no indications of mummy berry, leaf rust, or root rot.',
        'symptoms': [
            'Glossy dark green or blue-green leaves with supple texture',
            'Uniform venation with no chlorosis between veins',
            'Robust terminal buds and healthy shoot growth'
        ],
        'organic_treatment': [
            'Maintain acidic soil pH between 4.5 and 5.2 with elemental sulfur',
            'Mulch with pine needles or aged sawdust to preserve root zone moisture'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Routine soil pH testing and drip irrigation with low-mineral water'
        ]
    },
    'Cherry_(including_sour)___Powdery_mildew': {
        'crop': 'Cherry',
        'condition': 'Powdery Mildew',
        'is_healthy': False,
        'severity': 'Moderate',
        'pathogen': 'Podosphaera clandestina (Fungus)',
        'description': 'A common fungal infection that covers young cherry leaves and shoots in powdery white mycelium, causing leaf distortion and reduced photosynthesis.',
        'symptoms': [
            'White to light grey powdery patches on the underside or surface of leaves',
            'Young terminal leaves curl upward and become crinkled or stunted',
            'Foliage may turn yellow, brown, and drop early'
        ],
        'organic_treatment': [
            'Potassium bicarbonate spray (3 tbsp per gallon water) or neem oil',
            'Sulfur-based fungicides applied during early vegetative shoot extension',
            'Prune water sprouts and dense inner branches to boost airflow'
        ],
        'chemical_treatment': [
            'Myclobutanil (Rally 40WSP) or Quinoxyfen (Quintec)',
            'Trifloxystrobin or Boscalid rotation to prevent fungicide resistance'
        ],
        'prevention': [
            'Avoid excessive nitrogen fertilization which stimulates overly succulent susceptible growth',
            'Irrigate early in the morning so canopy dries quickly'
        ]
    },
    'Cherry_(including_sour)___Healthy': {
        'crop': 'Cherry',
        'condition': 'Healthy Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Vigorous cherry foliage with rich green coloration, crisp serrated edges, and no shot-hole or mildew symptoms.',
        'symptoms': [
            'Glossy, oval-shaped leaves with healthy serrated leaf margins',
            'Absence of spots, shot-holes, or powdery residue',
            'Vigorous spur and new branch elongation'
        ],
        'organic_treatment': [
            'Maintain mulch barrier and compost tea foliar nutrition'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Dormant copper sprays in late autumn to prevent bacterial canker'
        ]
    },
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'crop': 'Corn (Maize)',
        'condition': 'Gray Leaf Spot',
        'is_healthy': False,
        'severity': 'High',
        'pathogen': 'Cercospora zeae-maydis (Fungus)',
        'description': 'One of the most destructive foliar diseases of maize worldwide, thriving in warm humid environments and causing extensive photosynthetic loss.',
        'symptoms': [
            'Small tan spots with yellow halos that expand into long, narrow rectangular lesions',
            'Lesions run parallel to leaf veins, bounded by lateral veins',
            'Entire leaves blight and die, leading to stalk lodging and reduced grain fill'
        ],
        'organic_treatment': [
            'Deep tillage of infected crop residues to accelerate soil decomposition',
            'Crop rotation away from corn for at least 1-2 years',
            'Foliar spray with bio-antagonists such as Trichoderma viride'
        ],
        'chemical_treatment': [
            'Azoxystrobin + Difenoconazole (Quadris Top)',
            'Pyraclostrobin (Headline AMP) or Trifloxystrobin applied at VT-R1 growth stage'
        ],
        'prevention': [
            'Select high-yielding corn hybrids with genetic resistance to Gray Leaf Spot',
            'Adjust plant density to allow optimal air drainage between rows'
        ]
    },
    'Corn_(maize)___Common_rust_': {
        'crop': 'Corn (Maize)',
        'condition': 'Common Rust',
        'is_healthy': False,
        'severity': 'Moderate',
        'pathogen': 'Puccinia sorghi (Fungus)',
        'description': 'Fungal disease spread by windborne spores from subtropical regions, creating cinnamon-brown pustules on both upper and lower leaf surfaces.',
        'symptoms': [
            'Oval to elongate cinnamon-brown powdery pustules on both leaf surfaces',
            'Pustules rupture the epidermis, releasing powdery reddish urediniospores',
            'Severe infections turn leaf tissue chlorotic and dry out leaves prematurely'
        ],
        'organic_treatment': [
            'Apply sulfur dust or horticultural sulfur sprays early in the season',
            'Encourage beneficial mycorrhizal fungi to enhance plant immunity'
        ],
        'chemical_treatment': [
            'Strobilurin or Triazole class fungicides (e.g., Pyraclostrobin, Propiconazole)',
            'Spray when pustules appear on more than 6 leaves per plant prior to tasseling'
        ],
        'prevention': [
            'Plant rust-resistant hybrids featuring the Rp gene complex',
            'Plant early in the season to mature before spore flights peak'
        ]
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
        'crop': 'Corn (Maize)',
        'condition': 'Northern Corn Leaf Blight',
        'is_healthy': False,
        'severity': 'High',
        'pathogen': 'Exserohilum turcicum (Fungus)',
        'description': 'A devastating fungal disease characterized by large cigar-shaped lesions that can defoliate corn fields during cool, wet reproductive stages.',
        'symptoms': [
            'Large, elongated cigar-shaped grayish-green to tan lesions (2.5 to 15 cm long)',
            'Dark olive or black fungal sporulation visible within lesions during damp weather',
            'Extensive canopy blighting resembling frost damage'
        ],
        'organic_treatment': [
            'Crop rotation with non-host crops (soybean, sorghum, alfalfa)',
            'Shred and plow down corn stover immediately following harvest'
        ],
        'chemical_treatment': [
            'Trivapro (Benzovindiflupyr + Azoxystrobin + Propiconazole)',
            'Delaro (Prothioconazole + Trifloxystrobin) around silking'
        ],
        'prevention': [
            'Choose resistant corn varieties possessing Ht resistance genes',
            'Avoid continuous no-till corn-on-corn planting schedules'
        ]
    },
    'Corn_(maize)___Healthy': {
        'crop': 'Corn (Maize)',
        'condition': 'Healthy Maize Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Corn leaf exhibits robust green blade coloration, prominent clear midrib, and no lesions, rust pustules, or streaks.',
        'symptoms': [
            'Broad, vibrant green leaves with strong cellular turgor',
            'Clear central midrib with no chlorotic streaking or leaf blight',
            'Optimal tassel and ear development'
        ],
        'organic_treatment': [
            'Ensure balanced nitrogen-phosphorus-potassium and zinc soil fertility'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Maintain weed control in early growth stages and monitor moisture'
        ]
    },
    'Grape___Black_rot': {
        'crop': 'Grape',
        'condition': 'Black Rot',
        'is_healthy': False,
        'severity': 'High to Critical',
        'pathogen': 'Guignardia bidwellii (Fungus)',
        'description': 'One of the most destructive diseases of cultivated grapes in warm, humid regions, attacking leaves, shoots, tendrils, and berries.',
        'symptoms': [
            'Circular reddish-brown leaf spots with dark margins and tiny black dots (pycnidia)',
            'Dark elongated cankers on young canes and tendrils',
            'Infected grapes turn pale, soften, shrivel into hard black wrinkled mummies'
        ],
        'organic_treatment': [
            'Thoroughly remove and burn mummified grapes and infected canes during winter',
            'Copper fungicide or lime-sulfur sprays during dormant and bud-swell stages',
            'Canopy management: leaf pulling around fruit clusters for air and sun exposure'
        ],
        'chemical_treatment': [
            'Myclobutanil (Rally), Tebuconazole (Elite), or Mancozeb',
            'Begin sprays at 2 to 4 inch shoot growth and continue every 10-14 days through veraison'
        ],
        'prevention': [
            'Ensure vineyard rows are oriented parallel to prevailing winds',
            'Avoid overhead sprinkler irrigation'
        ]
    },
    'Grape___Esca_(Black_Measles)': {
        'crop': 'Grape',
        'condition': 'Esca (Black Measles)',
        'is_healthy': False,
        'severity': 'Critical',
        'pathogen': 'Phaeomoniella chlamydospora & Fomitiporia mediterranea (Fungi)',
        'description': 'A complex vascular wood-decay disease of grapevine trunks that causes tiger-stripe leaf patterns, spotted berries, and vine apoplexy.',
        'symptoms': [
            'Distinct "tiger-stripe" interveinal chlorosis and necrosis on mature leaves',
            'Small dark purple or brown spots on grape skin (black measles appearance)',
            'Sudden wilting and collapse of entire vine branches in hot summer weather',
            'Spongy rot in the interior wood of vine cordons and trunks'
        ],
        'organic_treatment': [
            'Double pruning technique: prune non-fruiting canes early and final canes late in winter',
            'Apply wound sealants (Trichoderma-based paste) on all large pruning cuts immediately',
            'Trunk renewal by training a healthy sucker from below diseased wood'
        ],
        'chemical_treatment': [
            'Thiophanate-methyl paste on vine pruning wounds',
            'Sodium arsenite (historical, restricted/banned in most jurisdictions; use bio-protectants)'
        ],
        'prevention': [
            'Disinfect pruning shears regularly with bleach or alcohol',
            'Avoid pruning during rainy or high-humidity days'
        ]
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'crop': 'Grape',
        'condition': 'Leaf Blight (Isariopsis Clavispora)',
        'is_healthy': False,
        'severity': 'Moderate',
        'pathogen': 'Pseudocercospora vitis / Isariopsis clavispora (Fungus)',
        'description': 'Causes irregular necrotic leaf spots that can lead to early autumn defoliation, impairing sugar accumulation in ripening grapes.',
        'symptoms': [
            'Irregular brown or purplish lesions on leaves, often bounded by main veins',
            'Faint greyish-black velvety mold growth on the lower surface of lesions',
            'Extensive premature leaf drop weakening grapevine carbohydrate reserves'
        ],
        'organic_treatment': [
            'Spray copper oxychloride (0.25%) or Bordeaux mixture',
            'Rake and compost or bury fallen infected leaves after harvest'
        ],
        'chemical_treatment': [
            'Mancozeb 75 WP (2 g/L) or Carbendazim (1 g/L)',
            'Azoxystrobin or Difenoconazole spray schedule'
        ],
        'prevention': [
            'Maintain good canopy ventilation through trellis training',
            'Balanced potash fertilization to strengthen vine cell walls'
        ]
    },
    'Grape___Healthy': {
        'crop': 'Grape',
        'condition': 'Healthy Grape Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Grapevine leaves are broad, palmately lobed, vibrant green, and free of mildew, spots, or nutrient deficiencies.',
        'symptoms': [
            'Lush green lamina with intact margins and healthy petioles',
            'Clear venation without yellowing, scorch, or curling',
            'Uniform cluster development with healthy flowering and berry set'
        ],
        'organic_treatment': [
            'Foliar kelp and micronutrient sprays during active vegetative growth'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Regular scouting for leafhoppers and downy mildew'
        ]
    },
    'Orange___Haunglongbing_(Citrus_greening)': {
        'crop': 'Citrus (Orange)',
        'condition': 'Huanglongbing (Citrus Greening)',
        'is_healthy': False,
        'severity': 'Critical',
        'pathogen': 'Candidatus Liberibacter asiaticus (Bacterium, vectored by Asian Citrus Psyllid)',
        'description': 'The most devastating citrus disease known. It chokes the phloem transport system, causing bitter lopsided green fruit and tree mortality.',
        'symptoms': [
            'Asymmetric, blotchy yellow mottle on leaves crossing leaf veins',
            'Hardened, yellowed, upright foliage with small leaves resembling zinc deficiency',
            'Small, misshapen, lopsided green fruit with bitter taste and aborted seeds',
            'Dieback of twigs and progressive decline of tree vigor'
        ],
        'organic_treatment': [
            'Biological control of the Asian Citrus Psyllid vector using Tamarixia radiata parasitoid wasps',
            'Soil drench with nutritional supplements (chelated iron, zinc, potassium) to prolong root vitality',
            'Kaolin clay spray to deter psyllid feeding on new leaf flushes'
        ],
        'chemical_treatment': [
            'Insecticide rotation for psyllid control: Imidacloprid, Thiamethoxam, Fenpropathrin',
            'Antibiotic trunk injections (Oxytetracycline hydrochloride) where legally permitted'
        ],
        'prevention': [
            'Plant only certified disease-free nursery stock from screenhouses',
            'Strict quarantine enforcement and prompt removal of confirmed infected trees'
        ]
    },
    'Peach___Bacterial_spot': {
        'crop': 'Peach',
        'condition': 'Bacterial Spot',
        'is_healthy': False,
        'severity': 'High',
        'pathogen': 'Xanthomonas arboricola pv. pruni (Bacterium)',
        'description': 'Attacks leaves, twigs, and fruit of stone fruits, causing shot-hole lesions, premature defoliation, and deep unmarketable fruit blemishes.',
        'symptoms': [
            'Water-soaked angular purple-brown spots on leaves that dry and drop out ("shot-hole")',
            'Severe leaf drop leading to exposed fruit and sunscald',
            'Cracking and pitted gumming lesions on developing peach fruit'
        ],
        'organic_treatment': [
            'Fixed copper sprays applied at leaf fall in autumn and at dormant bud swell',
            'Bio-pesticides such as Bacillus amyloliquefaciens',
            'Prune affected cankered branches during winter'
        ],
        'chemical_treatment': [
            'Oxytetracycline (Mycoshield) sprays during bloom and petal fall',
            'Copper hydroxide + Mancozeb low-rate applications in early cover sprays'
        ],
        'prevention': [
            'Plant resistant peach varieties (e.g., Candor, Biscoe, Redhaven)',
            'Avoid sandy soils exposed to wind-driven rain; plant windbreaks'
        ]
    },
    'Peach___Healthy': {
        'crop': 'Peach',
        'condition': 'Healthy Peach Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Lanceolate peach leaves show pristine green chlorophyll, unspotted surfaces, and sturdy petioles with no curl or shot-hole.',
        'symptoms': [
            'Vibrant long lance-shaped green leaves with finely serrated margins',
            'Absence of leaf curl (Taphrina deformans) or bacterial spots',
            'Healthy shoot elongation and abundant blossom set'
        ],
        'organic_treatment': [
            'Dormant copper wash before bud swell to prevent peach leaf curl'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Ensure well-drained orchard soil and balanced spring fertilization'
        ]
    },
    'Pepper,_bell___Bacterial_spot': {
        'crop': 'Bell Pepper',
        'condition': 'Bacterial Spot',
        'is_healthy': False,
        'severity': 'High',
        'pathogen': 'Xanthomonas campestris pv. vesicatoria (Bacterium)',
        'description': 'Favored by warm humid rainstorms, it spreads rapidly across bell pepper fields, producing water-soaked leaf spots and blistered fruit lesions.',
        'symptoms': [
            'Small circular to irregular water-soaked spots turning dark brown with yellow halos',
            'Spots coalesce, causing leaves to turn brown, scorch, and drop prematurely',
            'Rough, raised, blister-like corky scabs on green bell peppers'
        ],
        'organic_treatment': [
            'Copper bactericide sprays (Copper hydroxide or Copper sulfate)',
            'Hot water seed treatment (50°C for 25 minutes) prior to seeding',
            'Foliar spray of Bacillus subtilis or bacteriophage solutions'
        ],
        'chemical_treatment': [
            'Copper + Mancozeb tank mix to combat copper-resistant bacterial strains',
            'Acibenzolar-S-methyl (Actigard) plant defense activator'
        ],
        'prevention': [
            'Use certified disease-free seed and resistant hybrids (Xcv 1-10 resistance)',
            'Rotate away from Solanaceous crops (tomato, potato, eggplant) for 2 years',
            'Avoid working in wet fields to prevent mechanical transmission'
        ]
    },
    'Pepper,_bell___Healthy': {
        'crop': 'Bell Pepper',
        'condition': 'Healthy Bell Pepper Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Bell pepper leaf exhibits uniform deep green luster, smooth margins, and firm structure without mosaic mottling or bacterial spots.',
        'symptoms': [
            'Deep green, smooth, ovate leaves with erect posture',
            'Clean petioles and nodes without dark stem streaks',
            'Strong flower buds and symmetric fruit setting'
        ],
        'organic_treatment': [
            'Maintain regular calcium levels to prevent blossom end rot in fruit',
            'Apply neem oil preventatively for aphid and thrips deterrence'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Drip irrigation under plastic mulch to suppress weeds and splash diseases'
        ]
    },
    'Potato___Early_blight': {
        'crop': 'Potato',
        'condition': 'Early Blight',
        'is_healthy': False,
        'severity': 'Moderate to High',
        'pathogen': 'Alternaria solani (Fungus)',
        'description': 'Attacks aging potato foliage first, producing characteristic "target-board" concentric ring lesions that cause significant tuber yield reduction.',
        'symptoms': [
            'Dark brown to black oval or angular spots showing concentric ring pattern ("target board")',
            'Lesions usually start on the lower, older leaves and move upward',
            'Yellow chlorotic halos surrounding spots, causing leaves to dry up and hang down'
        ],
        'organic_treatment': [
            'Spray copper-based fungicides at first sign of lower leaf spotting',
            'Bio-fungicide applications containing Bacillus amyloliquefaciens',
            'Ensure adequate nitrogen and potassium fertility; stressed plants are far more vulnerable'
        ],
        'chemical_treatment': [
            'Chlorothalonil (Bravo Weather Stik) or Mancozeb as protectant',
            'Difenoconazole, Boscalid, or Azoxystrobin for curative action'
        ],
        'prevention': [
            'Plant certified disease-free seed tubers',
            'Maintain 3-year crop rotation avoiding tomato, eggplant, and pepper',
            'Harvest potatoes only when vines are completely dead and skins have set'
        ]
    },
    'Potato___Late_blight': {
        'crop': 'Potato',
        'condition': 'Late Blight (Irish Potato Famine Pathogen)',
        'is_healthy': False,
        'severity': 'Critical',
        'pathogen': 'Phytophthora infestans (Oomycete)',
        'description': 'One of the most destructive agricultural plant pathogens in human history. Under cool, moist conditions it can ruin an entire potato field in days.',
        'symptoms': [
            'Dark water-soaked lesions on leaves and stems that expand rapidly with pale green halos',
            'White delicate fungal-like downy growth on the underside of leaves during high humidity',
            'Entire foliage rots into a black, foul-smelling mass',
            'Tubers exhibit granular reddish-brown dry rot beneath the skin'
        ],
        'organic_treatment': [
            'Preventative copper fungicide (Bordeaux mixture) applied before rain events',
            'Kill and destroy potato vines 2 weeks prior to harvest to protect tubers',
            'Immediate rogouing and burying of infected plants to protect neighboring crops'
        ],
        'chemical_treatment': [
            'Mefenoxam / Metalaxyl-M (Ridomil Gold)',
            'Fluopicolide (Presidio), Cyazofamid (Ranman), or Mandipropamid (Revus)'
        ],
        'prevention': [
            'Never plant culled or supermarket potatoes; use certified seed tubers',
            'Eliminate cull piles and volunteer potato plants which harbor overwintering inoculum',
            'Utilize BlightCast weather forecast alerts to time protective treatments'
        ]
    },
    'Potato___Healthy': {
        'crop': 'Potato',
        'condition': 'Healthy Potato Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Robust compound potato leaves with lush green leaflets, clear veins, and no necrotic spots, blight margins, or leafhopper burn.',
        'symptoms': [
            'Full compound leaves with vibrant emerald green color',
            'Intact leaflet margins with no wilting, curling, or spotting',
            'Vigorous stem growth supporting active underground tuber bulking'
        ],
        'organic_treatment': [
            'Ensure adequate hilling of soil around potato stems to shield tubers from light'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Monitor humidity and leaf wetness hours; keep foliage dry with drip irrigation'
        ]
    },
    'Raspberry___Healthy': {
        'crop': 'Raspberry',
        'condition': 'Healthy Raspberry Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Pinnately compound raspberry leaves with light green undersides, sharp serrations, and no rust, anthracnose, or spur blight.',
        'symptoms': [
            'Vibrant green upper leaf surface with characteristic silvery-white underside',
            'Clean serrated edges and flexible petioles',
            'Healthy floricane and primocane vegetative development'
        ],
        'organic_treatment': [
            'Trellis cane systems to maximize air flow and sun penetration'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Prune out spent fruiting canes immediately after summer harvest'
        ]
    },
    'Soybean___Healthy': {
        'crop': 'Soybean',
        'condition': 'Healthy Soybean Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Trifoliolate soybean leaf with uniform chlorophyll density, unblemished surface, and active symbiotic nitrogen fixation in root nodules.',
        'symptoms': [
            'Symmetrical trifoliate leaflets with healthy smooth margins',
            'Deep green coloration indicating optimal chlorophyll synthesis',
            'Abundant flower set and robust pod filling'
        ],
        'organic_treatment': [
            'Ensure Bradyrhizobium japonicum soil inoculation for organic nitrogen fixation'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Crop rotation with non-legumes (corn, wheat) to disrupt nematode and fungal cycles'
        ]
    },
    'Squash___Powdery_mildew': {
        'crop': 'Squash',
        'condition': 'Powdery Mildew',
        'is_healthy': False,
        'severity': 'Moderate to High',
        'pathogen': 'Podosphaera xanthii (Fungus)',
        'description': 'A pervasive cucurbit disease that spreads as white talcum-powder spots over broad squash leaves, leading to leaf death and sun-scalded fruit.',
        'symptoms': [
            'White circular powdery spots on upper and lower surfaces of leaves and stems',
            'Spots spread to cover entire leaves in a white talc-like coating',
            'Infected leaves turn yellow, then brown, becoming brittle and dying prematurely'
        ],
        'organic_treatment': [
            'Potassium bicarbonate or baking soda solution (1 tbsp + 1 tsp horticultural oil per gallon)',
            'Neem oil or milk-water spray (40% milk / 60% water in direct sun)',
            'Sulfur dust applied early before temperatures exceed 32°C (90°F)'
        ],
        'chemical_treatment': [
            'Myclobutanil, Triflumizole (Procure), or Quinoxyfen (Quintec)',
            'Boscalid + Pyraclostrobin (Pristine)'
        ],
        'prevention': [
            'Choose powdery mildew-resistant squash cultivars (e.g., Success PM, Dunja)',
            'Space plants adequately to facilitate drying of morning dew'
        ]
    },
    'Strawberry___Leaf_scorch': {
        'crop': 'Strawberry',
        'condition': 'Leaf Scorch',
        'is_healthy': False,
        'severity': 'Moderate',
        'pathogen': 'Diplocarpon earlianum (Fungus)',
        'description': 'Produces numerous irregular purple to brown blotches on strawberry leaves, giving the foliage a scorched or burned appearance in warm weather.',
        'symptoms': [
            'Small, irregular purplish spots (1-5 mm) lacking white centers (unlike leaf spot)',
            'Spots coalesce, turning the entire leaf purplish-red then brown and dry',
            'Leaf margins curl upward, giving a severely scorched look'
        ],
        'organic_treatment': [
            'Mow or shear strawberry foliage immediately after renovation harvest',
            'Apply copper soap or liquid copper fungicide in spring as new leaves emerge',
            'Remove and discard old infected runner leaves'
        ],
        'chemical_treatment': [
            'Captan 50WP or Thiram protectant fungicides',
            'Pyraclostrobin (Cabrio) or Fenhexamid (Elevate)'
        ],
        'prevention': [
            'Plant on raised beds with drip irrigation to avoid wet foliage',
            'Use certified virus and disease-free strawberry crowns'
        ]
    },
    'Strawberry___Healthy': {
        'crop': 'Strawberry',
        'condition': 'Healthy Strawberry Leaf',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Vibrant trifoliate strawberry leaves with bright green coloring, serrated edges, and strong runner growth with no leaf spot or scorch.',
        'symptoms': [
            'Bright glossy trifoliate leaflets with healthy serrated margins',
            'Clean crown with no red stele or anthracnose rot',
            'Vigorous flower trusses and sweet berry production'
        ],
        'organic_treatment': [
            'Straw mulch application around plants to keep berries off bare soil'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Maintain weed-free beds and rotate planting every 3 to 4 years'
        ]
    },
    'Tomato___Bacterial_spot': {
        'crop': 'Tomato',
        'condition': 'Bacterial Spot',
        'is_healthy': False,
        'severity': 'High',
        'pathogen': 'Xanthomonas perforans / vesicatoria (Bacterium)',
        'description': 'A devastating bacterial disease of tomatoes causing dark water-soaked spots on foliage, extensive leaf loss, and raised scabby spots on fruit.',
        'symptoms': [
            'Small (under 3mm) dark brown to black circular spots with greasy, water-soaked margins',
            'Centers of spots may dry and tear, giving a ragged appearance',
            'Extensive defoliation exposing green tomatoes to sunscald',
            'Black raised scab-like lesions on green and ripening fruit'
        ],
        'organic_treatment': [
            'Copper hydroxide + bio-pesticide spray (Bacillus subtilis)',
            'Hot water seed sanitation (50°C for 25 minutes)',
            'Disinfect pruning shears between plants with bleach or sanitizing wipes'
        ],
        'chemical_treatment': [
            'Copper + Mancozeb tank mix to suppress copper-tolerant bacterial populations',
            'Actigard (Acibenzolar-S-methyl) systemic acquired resistance inducer'
        ],
        'prevention': [
            'Use disease-free certified seeds and transplants',
            'Avoid overhead sprinkler irrigation; always water at base of stems',
            'Rotate away from Solanaceous crops for a minimum of 2 seasons'
        ]
    },
    'Tomato___Early_blight': {
        'crop': 'Tomato',
        'condition': 'Early Blight',
        'is_healthy': False,
        'severity': 'Moderate to High',
        'pathogen': 'Alternaria linariae / solani (Fungus)',
        'description': 'Very common tomato disease characterized by concentric bullseye rings on leaves starting from the bottom of the plant and moving upward.',
        'symptoms': [
            'Dark brown to black circular lesions with distinct concentric rings ("bullseye / target")',
            'Surrounding yellow chlorotic halos that eventually cause leaf yellowing and death',
            'Starts on oldest lower leaves and progressively moves up the canopy',
            'Dark sunken leathery cankers on stems near the soil line ("collar rot")'
        ],
        'organic_treatment': [
            'Prune lower 30 cm of tomato foliage to eliminate soil-splash contact',
            'Apply copper sulfate or copper octanoate at 7-10 day intervals',
            'Mulch heavily around the base of plants with straw or plastic film'
        ],
        'chemical_treatment': [
            'Chlorothalonil (Daconil 2787) or Mancozeb protective sprays',
            'Azoxystrobin (Quadris) or Difenoconazole curative treatments'
        ],
        'prevention': [
            'Stake or cage tomato plants to keep all foliage off the ground',
            'Water in the morning with drip lines to minimize canopy wetness hours'
        ]
    },
    'Tomato___Late_blight': {
        'crop': 'Tomato',
        'condition': 'Late Blight',
        'is_healthy': False,
        'severity': 'Critical',
        'pathogen': 'Phytophthora infestans (Oomycete)',
        'description': 'A catastrophic disease capable of turning healthy tomato vines into brown slimy ruins within a few rainy days. Requires urgent response.',
        'symptoms': [
            'Irregular pale to olive green water-soaked spots rapidly turning dark brown/purple',
            'White velvety mold growth on the underside of leaves during wet, foggy mornings',
            'Large brown firm greasy blotches on green fruit that quickly rot',
            'Rapid collapse and blackening of entire branches and stems'
        ],
        'organic_treatment': [
            'Immediate protective copper fungicide sprays before rain storms',
            'Immediately bag and remove infected tomato plants from the garden; do not compost',
            'Bio-fungicides containing Bacillus amyloliquefaciens'
        ],
        'chemical_treatment': [
            'Mandipropamid (Revus), Cyazofamid (Ranman), or Fluopicolide (Presidio)',
            'Chlorothalonil applied preventatively in wet weather'
        ],
        'prevention': [
            'Plant late blight-resistant tomato varieties (e.g., Mountain Magic, Defiant, Iron Lady)',
            'Avoid planting tomatoes near potato patches',
            'Track regional agricultural late-blight warning forecasts'
        ]
    },
    'Tomato___Leaf_Mold': {
        'crop': 'Tomato',
        'condition': 'Leaf Mold',
        'is_healthy': False,
        'severity': 'Moderate',
        'pathogen': 'Passalora fulva (Fungus)',
        'description': 'Thrives in humid conditions (especially high tunnels and greenhouses), producing pale yellow leaf spots with olive-brown velvety mold beneath.',
        'symptoms': [
            'Pale yellow or light green spots on upper leaf surfaces with indistinct borders',
            'Dense olive-green to grayish-brown velvety mold on corresponding leaf undersides',
            'Leaves curl, turn brown, wither, and drop, though fruit is rarely infected directly'
        ],
        'organic_treatment': [
            'Aggressive greenhouse ventilation: run exhaust fans to keep relative humidity below 85%',
            'Prune suckers and dense leaves to allow maximum airflow through the tomato canopy',
            'Copper fungicides or bio-fungicide sprays (Trichoderma or Bacillus strains)'
        ],
        'chemical_treatment': [
            'Chlorothalonil or Mancozeb applied to lower leaf surfaces',
            'Difenoconazole (Inspire Super) or Azoxystrobin'
        ],
        'prevention': [
            'Select leaf mold-resistant tomato hybrids (Cf gene resistance series)',
            'Use horizontal air flow (HAF) fans and under-bench heating in greenhouses'
        ]
    },
    'Tomato___Septoria_leaf_spot': {
        'crop': 'Tomato',
        'condition': 'Septoria Leaf Spot',
        'is_healthy': False,
        'severity': 'High',
        'pathogen': 'Septoria lycopersici (Fungus)',
        'description': 'One of the most destructive foliar diseases of tomatoes in home gardens and commercial fields, causing rapid lower-leaf defoliation.',
        'symptoms': [
            'Numerous tiny circular spots (1.5 - 3 mm) with dark brown margins and white or gray centers',
            'Tiny black speckles (pycnidia) clearly visible inside the light center of spots',
            'Leaves turn completely yellow, wither, and drop off starting from the base'
        ],
        'organic_treatment': [
            'Remove affected lower leaves as soon as first spots appear',
            'Spray copper soap or Bordeaux mixture weekly in rainy seasons',
            'Mulch heavily beneath tomato plants to create a physical barrier against soil spores'
        ],
        'chemical_treatment': [
            'Chlorothalonil (Bravo / Daconil) every 7-10 days',
            'Mancozeb or Pyraclostrobin (Cabrio)'
        ],
        'prevention': [
            'Space plants 60-90 cm apart on stakes or cages for airflow',
            'Clean all garden stakes and cages with 10% bleach before reusing'
        ]
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'crop': 'Tomato',
        'condition': 'Two-Spotted Spider Mites',
        'is_healthy': False,
        'severity': 'High',
        'pathogen': 'Tetranychus urticae (Acari / Arachnid Pest)',
        'description': 'Microscopic sap-sucking pests that multiply explosively in hot, dry conditions, spinning fine webbing and draining plant sap.',
        'symptoms': [
            'Fine yellow or bronze stippling / speckling across the upper leaf surface',
            'Fine silky webbing woven between leaves, stems, and growing tips',
            'Leaves dry out, turn bronze or yellow, and drop',
            'Tiny moving yellow or red specks visible with 10x hand lens on leaf undersides'
        ],
        'organic_treatment': [
            'Release predatory mites (Phytoseiulus persimilis or Neoseiulus californicus)',
            'Spray insecticidal soap or horticultural oil targeting leaf undersides',
            'Neem oil or Rosemary oil-based organic miticides',
            'Strong jet of water on leaf undersides to knock down populations and destroy webbing'
        ],
        'chemical_treatment': [
            'Abamectin (Agri-Mek)',
            'Bifenazate (Acramite) or Spiromesifen (Oberon) selective miticides'
        ],
        'prevention': [
            'Avoid excessive nitrogen fertilizers and avoid dusty farm conditions',
            'Keep greenhouse humidity balanced; spider mites thrive in dry heat'
        ]
    },
    'Tomato___Target_Spot': {
        'crop': 'Tomato',
        'condition': 'Target Spot',
        'is_healthy': False,
        'severity': 'Moderate to High',
        'pathogen': 'Corynespora cassiicola (Fungus)',
        'description': 'Attacks leaves, stems, and fruit, forming brown circular lesions with subtle target rings that can cause severe leaf drop and fruit rot.',
        'symptoms': [
            'Pinpoint brown spots that enlarge to 10 mm with pale brown centers and yellow halos',
            'Concentric rings visible on lesions similar to early blight but spots are generally smaller',
            'Sunken brown lesions with dark concentric rings on mature fruit'
        ],
        'organic_treatment': [
            'Apply fixed copper or copper hydroxide weekly during humid weather',
            'Prune lower suckers and leaves to minimize humidity around stems'
        ],
        'chemical_treatment': [
            'Chlorothalonil, Azoxystrobin, or Famoxadone + Cymoxanil (Tanos)',
            'Boscalid (Endura) or Fluxapyroxad'
        ],
        'prevention': [
            'Avoid planting near old tomato, papaya, or cucumber fields (shared hosts)',
            'Maintain dry foliage through drip irrigation and adequate spacing'
        ]
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'crop': 'Tomato',
        'condition': 'Tomato Yellow Leaf Curl Virus (TYLCV)',
        'is_healthy': False,
        'severity': 'Critical',
        'pathogen': 'Begomovirus (vectored by Silverleaf Whitefly, Bemisia tabaci)',
        'description': 'A devastating viral disease transmitted by whiteflies that severely stunts tomato plants, resulting in zero marketable fruit yield if infected early.',
        'symptoms': [
            'Upward curling and cupping of leaflets into a bowl shape',
            'Interveinal chlorosis (yellowing) along leaf margins',
            'Severe stunting and bushy upright growth habit with shortened internodes',
            'Flower blossoms drop prematurely; fruit set is dramatically reduced or stopped'
        ],
        'organic_treatment': [
            'Install 50-mesh insect-proof netting over greenhouse vents',
            'Yellow sticky traps placed near canopy tops to monitor and trap whiteflies',
            'Insecticidal soap, neem oil, or Beauveria bassiana entomopathogenic fungus against whiteflies',
            'Roguing: immediately pull out and bag infected plants to prevent virus spread'
        ],
        'chemical_treatment': [
            'Systemic neonicotinoids (Imidacloprid, Thiamethoxam) at transplant',
            'Cyantraniliprole (Exirel) or Spiromesifen to control whitefly vectors'
        ],
        'prevention': [
            'Plant TYLCV-resistant tomato cultivars with Ty-1 or Ty-3 resistance genes',
            'Maintain a 2-month host-free period before planting new tomato crops'
        ]
    },
    'Tomato___Tomato_mosaic_virus': {
        'crop': 'Tomato',
        'condition': 'Tomato Mosaic Virus (ToMV)',
        'is_healthy': False,
        'severity': 'High to Critical',
        'pathogen': 'Tobamovirus (Extremely stable mechanical virus)',
        'description': 'An extraordinarily durable virus that spreads effortlessly through hands, tools, and tobacco products, surviving for years in dry plant debris.',
        'symptoms': [
            'Light green and dark green mottled "mosaic" pattern on leaves',
            'Leaf distortion: blistering, wrinkling, and narrowing into a "shoestring" fern-like shape',
            'Uneven fruit ripening with internal brown necrotic rings ("brown wall")',
            'Stunted overall plant growth'
        ],
        'organic_treatment': [
            'No cure exists once infected; promptly remove and burn infected plants',
            'Wash hands thoroughly with soap or 20% non-fat dry milk before touching tomatoes',
            'Disinfect tools in trisodium phosphate (TSP) or 10% bleach solution'
        ],
        'chemical_treatment': [
            'No chemical antiviral treatments exist for plant viral infections'
        ],
        'prevention': [
            'Plant TMV/ToMV resistant cultivars (labeled with "T" or "ToMV")',
            'Prohibit tobacco smoking or handling anywhere near the greenhouse/garden',
            'Use certified hot-water or heat-treated seeds'
        ]
    },
    'Tomato___Healthy': {
        'crop': 'Tomato',
        'condition': 'Healthy Tomato Foliage',
        'is_healthy': True,
        'severity': 'None',
        'pathogen': 'None (Optimal Plant Health)',
        'description': 'Pristine tomato foliage displaying strong compound structure, vibrant glandular green leaf hairs, and zero signs of blight, wilt, or viral distortion.',
        'symptoms': [
            'Vibrant emerald green leaves with fragrant glandular trichomes (leaf hairs)',
            'Clean petioles and sturdy stems without lesions or streaks',
            'Abundant flower clusters and uniform developing green fruit'
        ],
        'organic_treatment': [
            'Foliar calcium and compost tea to support fruit development and prevent blossom end rot'
        ],
        'chemical_treatment': [
            'No chemical intervention required'
        ],
        'prevention': [
            'Continue pruning bottom leaves for airflow and keep drip lines active'
        ]
    }
}

def get_disease_info(class_name: str) -> dict:
    """Retrieve structured agronomic information for a predicted class name."""
    info = DISEASE_DB.get(class_name)
    if info:
        return info
    for k, v in DISEASE_DB.items():
        if k.lower() == class_name.lower():
            return v
    # Fallback parser if not found
    parts = class_name.split('___')
    crop = parts[0].replace('_', ' ').strip()
    condition = parts[1].replace('_', ' ').strip() if len(parts) > 1 else 'Unknown'
    is_healthy = 'healthy' in condition.lower()
    return {
        'crop': crop,
        'condition': condition,
        'is_healthy': is_healthy,
        'severity': 'None' if is_healthy else 'Moderate',
        'pathogen': 'None' if is_healthy else 'Unknown Pathogen',
        'description': f'Analysis indicates {condition} on {crop}.' if not is_healthy else f'Healthy {crop} leaf detected.',
        'symptoms': ['Normal leaf coloration'] if is_healthy else ['Foliar discoloration or lesions detected.'],
        'organic_treatment': ['Continue regular maintenance.'] if is_healthy else ['Prune affected leaves and apply organic bio-protectant.'],
        'chemical_treatment': ['No chemical treatment needed.'] if is_healthy else ['Consult local agricultural extension for certified treatments.'],
        'prevention': ['Maintain clean soil and balanced watering.']
    }
