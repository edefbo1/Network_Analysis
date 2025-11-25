import pandas as pd
import uuid
import json
import ast

df = pd.read_csv("nodes.csv")

genres = set()

for item in df["genres"].dropna():

    if item.strip() == "[]":
        continue

    try:
        lista = ast.literal_eval(item)

        for g in lista:
            genres.add(g.strip())

    except:
        continue
    
print("Numero totale di generi musicali:", len(genres))
print("Generi musicali:", genres)
   
# # Dizionario di tutti i generi musicali mappati in macro-categorie da Claude 
# genres_dict = {
# "Rock": [
#       "rock", "hard rock", "alternative rock", "indie rock", "punk rock", "garage rock", "psychedelic rock",
#       "progressive rock", "folk rock", "blues rock", "grunge", "post-punk", "post-rock", "math rock",
#       "noise rock", "art rock", "space rock", "stoner rock", "krautrock", "britpop", "merseybeat",
#       "garage punk", "protopunk", "punk", "hardcore punk", "post-hardcore", "emo", "screamo", "emocore",
#       "skate punk", "ska punk", "folk punk", "celtic punk", "gypsy punk", "anarcho-punk", "crust punk",
#       "street punk", "riot grrrl", "queercore", "orgcore", "easycore", "pop punk", "neon pop punk",
#       "rock-and-roll", "rockabilly", "psychobilly", "neo-rockabilly", "glam rock", "glam punk", "glam metal",
#       "paisley underground", "madchester", "shoegaze", "dream pop", "slowcore", "sadcore", "c86",
#       "indie garage rock", "beatlesque", "jangle pop", "chamber pop", "baroque pop", "art pop",
#       "experimental rock", "noise punk", "no wave", "industrial rock", "gothic rock", "gothic post-punk",
#       "deathrock", "darkwave", "coldwave", "minimal wave", "synth punk", "electro punk", "dance-punk",
#       "post-grunge", "nu metal", "nu-metalcore", "metalcore", "deathcore", "melodic metalcore",
#       "progressive metalcore", "djent", "mathcore", "grindcore", "goregrind", "pornogrind", "noisecore",
#       "powerviolence", "thrash core", "crossover thrash", "d-beat", "crust", "screamo", "skramz",
#       "emo trap", "sad rap", "lo-fi emo", "midwest emo", "emo mexicano", "emo punk", "emo trap italiana",
#       "alternative emo", "indie emo", "anthem emo", "diy emo", "new england emo", "post-screamo",
#       "screamocore", "post-post-hardcore", "swancore", "sasscore", "epa dunk", "dunk", "stomp and holler",
#       "stomp and whittle", "stomp and flutter", "beatlesque", "freakbeat", "mod revival", "new romantic",
#       "new wave pop", "synth pop", "electropop", "indietronica", "chillwave", "hyperpop", "glitchcore",
#       "alternative pop rock", "modern alternative rock", "modern alternative pop", "alternative dance",
#       "indie pop rock", "indie electronica", "indie electropop", "indie dream pop", "indie shoegaze",
#       "indie psych-pop", "indie pop", "modern indie pop", "modern indie folk", "indie folk",
#       "indie anthem-folk", "indie singer-songwriter", "lo-fi indie", "bedroom pop", "bedroom soul",
#       "anti-folk", "freak folk", "folk metal", "folk black metal", "pagan metal", "viking metal",
#       "celtic metal", "medieval folk", "neofolk", "neo-pagan", "dungeon synth", "atmospheric black metal",
#       "blackgaze", "doomgaze", "shoegaze", "nu gaze", "gauze pop", "shimmer pop", "shimmer psych",
#       "shiver pop", "dreamo", "dream pop", "chillwave", "bedroom pop", "lo-fi indie", "indie folk",
#       "stomp pop", "chamber pop", "baroque pop", "orchestral pop", "symphonic pop", "art pop",
#       "experimental pop", "glitch pop", "hyperpop", "bubblegum pop", "bubblegum dance", "dance pop",
#       "electropop", "synth pop", "power pop", "jangle pop", "twee pop", "c86", "indie pop",
#       "swedish indie pop", "finnish indie pop", "norwegian indie pop", "danish indie pop", "icelandic indie pop"
#     ],

#     "Metal": [
#       "metal", "heavy metal", "thrash metal", "death metal", "black metal", "doom metal", "sludge metal",
#       "stoner metal", "drone metal", "funeral doom", "progressive metal", "power metal", "symphonic metal",
#       "gothic metal", "industrial metal", "nu metal", "metalcore", "deathcore", "grindcore",
#       "melodic death metal", "technical death metal", "brutal death metal", "slam death metal",
#       "progressive death metal", "blackened death metal", "war metal", "speed metal", "thrash core",
#       "crossover thrash", "groove metal", "sludge metal", "post-metal", "atmospheric post-metal",
#       "drone metal", "doom metal", "stoner doom", "psychedelic doom", "funeral doom", "death-doom",
#       "black metal", "atmospheric black metal", "depressive black metal", "blackgaze", "blackened thrash",
#       "folk metal", "pagan metal", "viking metal", "celtic metal", "oriental metal", "pirate metal",
#       "power metal", "symphonic power metal", "melodic power metal", "progressive power metal",
#       "neoclassical metal", "shred", "metal guitar", "djent", "mathcore", "technical metalcore",
#       "melodic metalcore", "progressive metalcore", "symphonic metalcore", "deathcore", "slamming deathcore",
#       "progressive deathcore", "melodic deathcore", "symphonic deathcore", "brutal deathcore",
#       "grindcore", "goregrind", "pornogrind", "cybergrind", "noisegrind", "noisecore", "powerviolence",
#       "fastcore", "thrashcore", "d-beat", "crust punk", "anarcho-punk", "hardcore punk", "metallic hardcore",
#       "beatdown", "tough guy hardcore", "youth crew", "straight edge", "vegan straight edge",
#       "christian metalcore", "unblack metal", "christian metal", "white metal", "nsbm", "red and anarchist black metal",
#       "depressive suicidal black metal", "atmospheric sludge", "post-doom metal", "stoner rock",
#       "desert rock", "palm desert scene", "space rock", "psychedelic rock", "acid rock", "heavy psych",
#       "retro metal", "occult rock", "proto-metal", "proto-doom", "doom rock", "stoner doom",
#       "sludge doom", "funeral doom", "drone doom", "ambient doom", "dark ambient", "dungeon synth",
#       "medieval ambient", "dark dungeon music", "fantasy dungeon synth", "comfy synth", "lo-fi dungeon synth"
#     ],

#     "Electronic": [
#       "electronic", "edm", "techno", "house", "trance", "dubstep", "drum and bass", "ambient",
#       "downtempo", "trip hop", "idm", "breakbeat", "jungle", "garage", "electro", "synth",
#       "industrial", "ebm", "darkwave", "synthwave", "vaporwave", "chillwave", "witch house",
#       "electronica", "glitch", "drill and bass", "footwork", "juke", "ghetto house", "acid house",
#       "deep house", "tech house", "progressive house", "electro house", "big room", "future house",
#       "bass house", "uk garage", "speed garage", "2-step", "grime", "dubstep", "brostep",
#       "riddim dubstep", "deathstep", "drumstep", "neurostep", "chillstep", "liquid dubstep",
#       "melodic dubstep", "future garage", "uk funky", "bassline", "niche", "4x4", "uk drill",
#       "drill", "trap", "hip house", "ghetto tech", "juke", "footwork", "vogue", "ballroom",
#       "jersey club", "baltimore club", "philly club", "miami bass", "booty bass", "electro bass",
#       "breakbeat", "broken beat", "nu skool breaks", "progressive breaks", "funky breaks",
#       "florida breaks", "jungle", "drum and bass", "liquid funk", "neurofunk", "jump up",
#       "darkstep", "drumfunk", "atmospheric dnb", "dancefloor dnb", "jazzy dnb", "ragga jungle",
#       "hardstep", "techstep", "intelligent dnb", "deep dnb", "minimal dnb", "halftime dnb",
#       "ambient dnb", "downtempo dnb", "liquid dnb", "deep liquid", "deep liquid bass",
#       "trance", "uplifting trance", "progressive trance", "tech trance", "hard trance",
#       "acid trance", "goa trance", "psychedelic trance", "psytrance", "full on", "progressive psytrance",
#       "dark psytrance", "forest psych", "hitech psytrance", "suomisaundi", "psybreaks", "psybass",
#       "psytech", "zenonesque", "progressive psy", "minimal psy", "twilight psy", "night psy",
#       "darkpsy", "forest psy", "hi-tech", "full on night", "full on morning", "full on day",
#       "ambient", "dark ambient", "drone", "drone ambient", "isolationism", "lowercase", "microsound",
#       "click", "glitch", "idm", "intelligent dance music", "braindance", "drill and bass",
#       "breakcore", "raggacore", "mashcore", "speedcore", "extratone", "splittercore", "terrorcore",
#       "doomcore", "industrial hardcore", "crossbreed", "darkcore", "hardcore techno", "gabber",
#       "happy hardcore", "freeform hardcore", "uk hardcore", "bouncy techno", "donk", "scouse house",
#       "makina", "hard house", "hard trance", "hardstyle", "raw hardstyle", "rawstyle", "euphoric hardstyle",
#       "jumpstyle", "tekstyle", "hardtek", "frenchcore", "uptempo hardcore", "terror", "speedcore"
#     ],

#     "Hip Hop & Rap": [
#       "hip hop", "rap", "trap", "boom bap", "underground hip hop", "conscious hip hop", "gangsta rap",
#       "g funk", "west coast hip hop", "east coast hip hop", "southern hip hop", "midwest hip hop",
#       "crunk", "snap", "hyphy", "chopped and screwed", "phonk", "drift phonk", "memphis rap",
#       "cloud rap", "emo rap", "sad rap", "plugg", "pluggnb", "rage", "trap metal", "drill",
#       "uk drill", "ny drill", "chicago drill", "brooklyn drill", "bronx drill", "pop rap",
#       "alternative hip hop", "experimental hip hop", "abstract hip hop", "nerdcore", "geek rap",
#       "comedy rap", "novelty rap", "parody rap", "battle rap", "freestyle rap", "slam poetry",
#       "turntablism", "beatboxing", "instrumental hip hop", "jazz rap", "jazz hop", "lo-fi hip hop",
#       "chillhop", "boom bap", "underground boom bap", "golden age hip hop", "old school hip hop",
#       "new school hip hop", "hardcore hip hop", "horrorcore", "acid rap", "psychedelic hip hop",
#       "trip hop", "downtempo", "breakbeat", "big beat", "nu jazz", "future jazz", "broken beat",
#       "uk bass", "grime", "dubstep", "brostep", "riddim", "deathstep", "drumstep", "neurostep",
#       "trap beats", "drill beats", "type beat", "instrumental trap", "lo-fi beats", "study beats",
#       "focus beats", "chill beats", "sad beats", "emo beats", "rage beats", "plugg beats"
#     ],

#     "Pop": [
#       "pop", "teen pop", "bubblegum pop", "dance pop", "electropop", "synth pop", "indie pop",
#       "art pop", "chamber pop", "baroque pop", "power pop", "jangle pop", "twee pop", "sunshine pop",
#       "sophisti-pop", "yacht rock", "soft rock", "easy listening", "adult contemporary", "lite rock",
#       "mellow gold", "new age", "new age piano", "meditation music", "healing music", "spa music",
#       "massage music", "reiki music", "chakra music", "sound healing", "binaural beats", "432hz",
#       "ambient music", "chill out", "lounge", "downtempo", "trip hop", "chillwave", "dream pop",
#       "bedroom pop", "lo-fi pop", "indie pop", "alternative pop", "art pop", "experimental pop",
#       "hyperpop", "glitchcore", "nightcore", "vaporwave", "future funk", "city pop", "shibuya-kei",
#       "j-pop", "k-pop", "c-pop", "mandopop", "cantopop", "hokkien pop", "thai pop", "t-pop",
#       "pinoy pop", "opm", "indonesian pop", "malaysian pop", "vietnamese pop", "lao pop",
#       "cambodian pop", "burmese pop", "latin pop", "latino pop", "reggaeton pop", "urbano pop"
#     ],

#     "Jazz": [
#       "jazz", "swing", "bebop", "cool jazz", "hard bop", "modal jazz", "free jazz", "avant-garde jazz",
#       "post-bop", "soul jazz", "jazz funk", "jazz fusion", "latin jazz", "afro-cuban jazz",
#       "bossa nova jazz", "samba jazz", "nu jazz", "acid jazz", "jazz rap", "jazz hop", "lo-fi jazz",
#       "smooth jazz", "contemporary jazz", "straight-ahead jazz", "mainstream jazz", "modern jazz",
#       "jazz piano", "jazz guitar", "jazz saxophone", "jazz trumpet", "jazz trombone", "jazz bass",
#       "jazz drums", "jazz vibraphone", "jazz flute", "jazz clarinet", "jazz violin", "jazz accordion",
#       "jazz organ", "jazz harp", "vocal jazz", "jazz vocals", "scat singing", "big band", "swing orchestra",
#       "jazz orchestra", "modern big band", "jazz ensemble", "jazz trio", "jazz quartet", "jazz quintet"
#     ],

#     "Blues": [
#       "blues", "delta blues", "chicago blues", "texas blues", "electric blues", "acoustic blues",
#       "blues rock", "blues-rock guitar", "modern blues", "modern blues rock", "country blues",
#       "piedmont blues", "jump blues", "rhythm and blues", "r&b", "soul", "soul blues", "southern soul",
#       "southern soul blues", "memphis soul", "philadelphia soul", "philly soul", "detroit soul",
#       "motown", "northern soul", "deep soul", "neo soul", "contemporary r&b", "alternative r&b",
#       "progressive soul", "psychedelic soul", "soul jazz", "soul funk", "funk soul", "p funk"
#     ],

#     "Country & Folk": [
#       "country", "country rock", "country pop", "contemporary country", "modern country rock",
#       "traditional country", "classic country", "honky tonk", "neo honky tonk", "bakersfield sound",
#       "outlaw country", "alt country", "alternative country", "americana", "roots rock", "heartland rock",
#       "southern rock", "swamp rock", "swamp pop", "tex-mex", "tejano", "conjunto", "norteno",
#       "banda", "duranguense", "grupera", "mariachi", "ranchera", "corrido", "narco corrido",
#       "folk", "traditional folk", "contemporary folk", "folk rock", "folk pop", "indie folk",
#       "freak folk", "anti-folk", "neofolk", "dark folk", "apocalyptic folk", "martial industrial",
#       "neo-medieval", "chamber folk", "string folk", "singer-songwriter", "acoustic folk",
#       "bluegrass", "progressive bluegrass", "newgrass", "bluegrass gospel", "bluegrass fiddle",
#       "old-time", "old-time fiddle", "appalachian folk", "celtic folk", "irish folk", "scottish folk"
#     ],

#     "Classical": [
#       "classical", "baroque", "classical era", "romantic era", "modern classical", "contemporary classical",
#       "minimalism", "post-minimalism", "serialism", "twelve-tone", "aleatoric", "spectral music",
#       "new complexity", "totalism", "microtonality", "just intonation", "electroacoustic",
#       "musique concrete", "acousmatic", "sound art", "field recording", "soundscape",
#       "orchestral", "symphony", "concerto", "sonata", "string quartet", "chamber music",
#       "opera", "operetta", "oratorio", "cantata", "mass", "requiem", "passion",
#       "early music", "medieval", "renaissance", "baroque ensemble", "period instruments",
#       "historically informed performance", "early music ensemble", "consort", "madrigal"
#     ],

#     "Reggae & Caribbean": [
#       "reggae", "roots reggae", "dub", "dub reggae", "steppers", "one drop", "rockers",
#       "lovers rock", "dancehall", "ragga", "raggamuffin", "digital dancehall", "early reggae",
#       "ska", "traditional ska", "ska revival", "2 tone", "third wave ska", "ska punk",
#       "rocksteady", "calypso", "soca", "bouyon", "zouk", "kompa", "compas", "meringue",
#       "punta", "punta rock", "garifuna", "mento", "nyahbinghi", "kumina", "burru"
#     ],

#     "Latin": [
#       "latin", "salsa", "mambo", "cha-cha-cha", "bolero", "son cubano", "timba", "bachata",
#       "merengue", "cumbia", "vallenato", "champeta", "porro", "currulao", "bullerengue",
#       "tango", "milonga", "candombe", "murga", "zamba", "chacarera", "chamamé", "cueca",
#       "huayno", "marinera", "festejo", "landó", "vals criollo", "musica criolla"
#     ],

#     "Soul & Funk": [
#       "soul", "funk", "disco", "boogie", "electro funk", "g-funk", "p-funk", "funk rock",
#       "funk metal", "jazz funk", "soul jazz", "acid jazz", "rare groove", "northern soul",
#       "modern soul", "neo soul", "alternative r&b", "future r&b", "psychedelic soul",
#       "progressive soul", "quiet storm", "smooth r&b", "contemporary r&b", "urban contemporary"
#     ],

#     "Gospel & Christian": [
#       "gospel", "southern gospel", "black gospel", "urban gospel", "contemporary gospel",
#       "praise", "worship", "contemporary worship", "ccm", "christian rock", "christian metal",
#       "christian hardcore", "christian punk", "christian hip hop", "gospel rap", "christian trap",
#       "christian edm", "christian pop", "christian indie", "christian alternative"
#     ],

#     "World Music": [
#       "world", "world music", "world fusion", "ethno", "ethnomusicology", "traditional",
#       "folk", "indigenous", "tribal", "afrobeat", "highlife", "juju", "fuji", "apala",
#       "makossa", "bikutsi", "soukous", "rumba congolaise", "ndombolo", "kizomba", "kuduro",
#       "semba", "marrabenta", "taraab", "taarab", "benga", "ohangla", "mugithi", "genge",
#       "gengetone", "zilizopendwa", "rhumba", "chimurenga", "sungura", "zimdancehall"
#     ],

#     "Experimental & Avant-Garde": [
#       "experimental", "avant-garde", "noise", "harsh noise", "noise rock", "noise pop",
#       "no wave", "post-industrial", "power electronics", "death industrial", "dark ambient",
#       "drone", "drone metal", "drone rock", "space ambient", "cosmic ambient", "fourth world",
#       "tribal ambient", "ritual ambient", "isolationism", "lowercase", "microsound", "glitch",
#       "clicks and cuts", "idm", "braindance", "drill and bass", "breakcore", "raggacore"
#     ],

#     "Children's Music": [
#       "children's music", "kids music", "nursery rhymes", "lullaby", "educational music",
#       "preschool music", "toddler music", "family music", "disney", "sesame street",
#       "barney", "raffi", "wiggles", "kindie rock", "kindermusik", "kid-friendly"
#     ],

#     "Soundtrack & Score": [
#       "soundtrack", "film score", "movie soundtrack", "tv soundtrack", "game soundtrack",
#       "video game music", "vgm", "chiptune", "8-bit", "16-bit", "keygen music", "demoscene",
#       "tracker music", "module music", "sid music", "c64", "amiga music", "gameboy music"
#     ],

#     "Comedy & Novelty": [
#       "comedy", "novelty", "parody", "comedy rock", "comedy rap", "comedy folk", "satire",
#       "humorous", "funny songs", "joke songs", "comedy album", "stand-up comedy", "spoken word comedy"
#     ]
# }