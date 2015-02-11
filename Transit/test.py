import json

__author__ = 'Ebrahim'

def getPolygon(polygonJSON):
    #polygonJSON = json.loads(polygon)
    new_polygon = ''
    for point in polygonJSON['coordinates'][0]:
        longitude = point[0]
        latitude = point[1]
        new_polygon += '%s %s ' % ("{0:.3f}".format(float(latitude)), "{0:.3f}".format(float(longitude)))
    new_polygon = new_polygon[:-1]
    return new_polygon

walkshed="""{"type": "FeatureCollection", "features": [{"type": "Feature","geometry": {"type":"Polygon","coordinates":[[[-114.065422333,51.0494065681],[-114.065235353,51.0495136376],[-114.063847497,51.0503083668],[-114.062642644,51.0509897818],[-114.061559839,51.0502428182],[-114.060314975,51.0493846562],[-114.060130305,51.0492549215],[-114.060318469,51.0483097727],[-114.060420023,51.0482501741],[-114.061860515,51.0474146005],[-114.062949314,51.0467908253],[-114.063772,51.046523],[-114.065373961,51.04845671],[-114.065422333,51.0494065681]]]}},{"type": "Feature","geometry": {"type":"Polygon","coordinates":[[[-114.080917071,51.053806494],[-114.080660898,51.0555355098],[-114.08007294,51.0573857648],[-114.079185445,51.0586273867],[-114.0773318,51.0607683],[-114.076870156,51.0612532144],[-114.075574194,51.0623056998],[-114.074324912,51.0628583391],[-114.071545416,51.0630263728],[-114.067477968,51.0638053697],[-114.06507937845,51.0624897670513],[-114.065278106,51.0633566734],[-114.065020684,51.0635163374],[-114.064248539535,51.0639984583182],[-114.0648819,51.0644109032],[-114.065017287,51.0652420832],[-114.0650174,51.0653786],[-114.065016844,51.0655159865],[-114.064695547399,51.0658048480514],[-114.0649469,51.0660285],[-114.0649639,51.0660518],[-114.0649917,51.0660952],[-114.064992052,51.0662171621],[-114.06477771,51.0670218956],[-114.064063852,51.0674510278],[-114.063369729,51.0678842612],[-114.063359848653,51.0678903230522],[-114.064104625,51.0683500156],[-114.064846596,51.0688023625],[-114.065478976,51.0697088748],[-114.064751417,51.0701670521],[-114.064023851,51.0706204426],[-114.064004141,51.0706329106],[-114.063289399,51.0710667823],[-114.0625367,51.0715195],[-114.061093947,51.0706178294],[-114.059926533,51.0698993579],[-114.059629145,51.0697132154],[-114.060223454,51.0687953086],[-114.0605947,51.0685605116],[-114.061643569047,51.0678687200412],[-114.060982975,51.0674443581],[-114.0611953,51.0669026],[-114.061582445418,51.0660736628229],[-114.060201481,51.0643946333],[-114.060849379491,51.0639877080408],[-114.060516502,51.0637693878],[-114.059926373,51.0633854497],[-114.059828667,51.0633227819],[-114.059993169,51.0624355255],[-114.060635924945,51.0620101458516],[-114.059932011,51.0615638193],[-114.059893008,51.0615387784],[-114.059896507,51.0606434692],[-114.059936517,51.0606186809],[-114.060909533623,51.0600200388285],[-114.06048611,51.0597448734],[-114.059548794,51.0588566165],[-114.059918181491,51.0586064388741],[-114.0540431,51.0514593],[-114.0533144,51.0512801],[-114.052601539,51.0511144451],[-114.0528187,51.0511543],[-114.054118414,51.0513852293],[-114.0552244,51.0517546],[-114.056941,51.0522187],[-114.0577306,51.0524668],[-114.0602111,51.053028],[-114.063039954,51.0525042131],[-114.065053946,51.0518200189],[-114.067579242,51.0509293842],[-114.070060442,51.0510917724],[-114.073398899,51.0524191503],[-114.076457206,51.0537399058],[-114.080917071,51.053806494]]]}}]}"""
walkshed=json.loads(walkshed)

if walkshed['type']=='FeatureCollection':
    for item in walkshed['features']:
        print getPolygon(item['geometry'])

else:
    getPolygon(walkshed)


a = {"type": "FeatureCollection", "features": [{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0680456,51.0612391]}, "properties": {"name": "Entertainment", "type": "Entertainment", "icon": "http://136.159.122.90/maki/basketball-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0692196,51.0608209]}, "properties": {"name": "Entertainment", "type": "Entertainment", "icon": "http://136.159.122.90/maki/basketball-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0661403,51.061532]}, "properties": {"name": "Crescent Heights High School", "type": "School", "icon": "http://136.159.122.90/maki/school-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0694312,51.0619641]}, "properties": {"name": "Entertainment", "type": "Entertainment", "icon": "http://136.159.122.90/maki/basketball-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.062806,51.0649132]}, "properties": {"name": "Sun's BBQ Restaurant", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0630892,51.0649024]}, "properties": {"name": "Lambda Oriental Foods Market", "type": "Shopping", "icon": "http://136.159.122.90/maki/shop-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0640248,51.0665799]}, "properties": {"name": "Central Grand Restaurant", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0694407,51.0582267]}, "properties": {"name": "Calgary Curling Club", "type": "Entertainment", "icon": "http://136.159.122.90/maki/playground-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0684421,51.0528362]}, "properties": {"name": "Jugo Juice", "type": "Restaurant", "icon": "http://136.159.122.90/maki/cafe-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0684791,51.0529643]}, "properties": {"name": "Subway", "type": "Restaurant", "icon": "http://136.159.122.90/maki/fast-food-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.067926,51.0511433]}, "properties": {"name": "Don Quijote Restaurante and Tapas Bar", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0755034,51.0593758]}, "properties": {"name": "Samie's Food Store", "type": "Shopping", "icon": "http://136.159.122.90/maki/shop-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0619379,51.0671522]}, "properties": {"name": "Subway", "type": "Restaurant", "icon": "http://136.159.122.90/maki/fast-food-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0630537,51.0676848]}, "properties": {"name": "Wa's", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0639871,51.0658172]}, "properties": {"name": "Pho Kim", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0622336,51.0640704]}, "properties": {"name": "Yamato Dessert Cafe", "type": "Shopping", "icon": "http://136.159.122.90/maki/shop-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0627826,51.0682312]}, "properties": {"name": "Shopping", "type": "Shopping", "icon": "http://136.159.122.90/maki/shop-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0627663,51.0640383]}, "properties": {"name": "Tim Hortons", "type": "Restaurant", "icon": "http://136.159.122.90/maki/cafe-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0630227,51.0640181]}, "properties": {"name": "Shoppers Drug Mart", "type": "Health", "icon": "http://136.159.122.90/maki/pharmacy-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0617626,51.0656498]}, "properties": {"name": "Tai Pan", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0627766,51.066632]}, "properties": {"name": "APM Bubble Tea Cafe", "type": "Restaurant", "icon": "http://136.159.122.90/maki/cafe-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0629963,51.0680525]}, "properties": {"name": "Beckham's Pub and Eatery", "type": "Restaurant", "icon": "http://136.159.122.90/maki/bar-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0627324,51.0662861]}, "properties": {"name": "Pho So 1", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0716237,51.0548551]}, "properties": {"name": "Restaurant", "type": "Restaurant", "icon": "http://136.159.122.90/maki/cafe-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0692737,51.0521138]}, "properties": {"name": "Joey Eau Claire", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0696787,51.0523246]}, "properties": {"name": "Barley Mill", "type": "Restaurant", "icon": "http://136.159.122.90/maki/bar-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0690944,51.0524146]}, "properties": {"name": "Good Earth Coffeehouse and Bakery", "type": "Restaurant", "icon": "http://136.159.122.90/maki/cafe-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0681329,51.0529845]}, "properties": {"name": "Garage Express", "type": "Restaurant", "icon": "http://136.159.122.90/maki/fast-food-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0689496,51.0528698]}, "properties": {"name": "Prego Cucina Italiana", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0684158,51.0527754]}, "properties": {"name": "Island Food", "type": "Shopping", "icon": "http://136.159.122.90/maki/shop-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0702867,51.0521398]}, "properties": {"name": "Barclay's Restaurant", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0684118,51.053014]}, "properties": {"name": "Grandma's Garden", "type": "Restaurant", "icon": "http://136.159.122.90/maki/fast-food-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0686224,51.0525023]}, "properties": {"name": "The Bean Stop", "type": "Restaurant", "icon": "http://136.159.122.90/maki/cafe-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0683796,51.0528445]}, "properties": {"name": "Asian Express Food", "type": "Restaurant", "icon": "http://136.159.122.90/maki/fast-food-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0679089,51.0531371]}, "properties": {"name": "Garage Billiards Sports", "type": "Restaurant", "icon": "http://136.159.122.90/maki/bar-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0695142,51.0524458]}, "properties": {"name": "1886 Buffalo Cafe", "type": "Restaurant", "icon": "http://136.159.122.90/maki/cafe-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0683193,51.0528521]}, "properties": {"name": "Taco Time", "type": "Restaurant", "icon": "http://136.159.122.90/maki/fast-food-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0683153,51.0530932]}, "properties": {"name": "Kid's Zone", "type": "Entertainment", "icon": "http://136.159.122.90/maki/playground-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0682589,51.0528639]}, "properties": {"name": "Delice Curry House and Bakery", "type": "Restaurant", "icon": "http://136.159.122.90/maki/fast-food-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0683917,51.0527155]}, "properties": {"name": "Babylon Qithara", "type": "Restaurant", "icon": "http://136.159.122.90/maki/fast-food-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0694762,51.0535221]}, "properties": {"name": "Eau Claire Spray Park", "type": "Entertainment", "icon": "http://136.159.122.90/maki/playground-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0630323,51.0707815]}, "properties": {"name": "Calypso's Taverna", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0681425,51.0524413]}, "properties": {"name": "Cineplex Odeon Eau Claire Market Cinema", "type": "Entertainment", "icon": "http://136.159.122.90/maki/cinema-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0619493,51.0590814]}, "properties": {"name": "Happy Hill Restaurant", "type": "Restaurant", "icon": "http://136.159.122.90/maki/restaurant-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0692984,51.0623945]}, "properties": {"name": "Entertainment", "type": "Entertainment", "icon": "http://136.159.122.90/maki/playground-18.png"}},{"type": "Feature","geometry": {"type": "Point", "coordinates":[-114.0697632,51.0516369]}, "properties": {"name": "Eau Claire Smokestack", "type": "Entertainment", "icon": "http://136.159.122.90/maki/town-hall-18.png"}}]}

print json.dumps(a['features'])[1:-1]