import csv
import pandas

titles = ['18*12.5 cm table small women cigarette joint smoking dish metal tin tobacco weed rolling paper tray storage', '1 pack (100 pieces) hot new weed tobacco bag tobacco weed sealed bag storage bag Smile yellow pattern with holder tobacco bag', 'Mini Toilet Model Metal Pipes Tobacco Smoking Pipes Gift Mill Smoke Weed Grinder Tobacco Pipe Smoking Accessories', 'Tobacco Roller Joint Roller Machine Size 70mm Blunt Fast Cigar Rolling Cigarette Weed Raw Tobacco Roller Drop Shipping 18jun27', '110mm Weed Rolling Machine Joint Roller Manual Hand Easy Cigarette Make Bell mouth Cone Cigarette bongo Smoking Tobacco Filling', 'US Warehouse 4 Layers Herb Tobacco Spice Weeds Grass Aluminium Grinder Smoke Crusher Hand Crank Muller Mill Smoking Pollinator', 'The Highest Quality Glass Multicolor Transparent Cigarette Tube Holder Smoking Filter Pipe Weed Accessories', '2019 Travel Unbreakable Skull-Shaped Silicone Smoking Pipe Weed Grinder Tobacco Cigarette Accessories Random Color', '4-layer Aluminum Herbal Herb Tobacco Grinder Smoke Grinders grinder weed herb grinder Cigarette Accessories', '1pcs Plastic Herb Grinder With Rolling Paper Function Diameter 30mm Grinders weed acessorios Tobacco Cigarette Crusher amoladora', 'PROSTORMER Electric Hedge Trimmer 2 in 1 3.6V USB Cordless Household Trimmer Rechargeable Weeding Shear Pruning Mower', '4Layers Aluminum Tobacco Grinder Weed Grinder Tobacco Smoking Herb Grinder Spice Herbal Hand Crank Crusher Accessories L*C', 'Tobacco Grinder Weed Grinder Tobacco Smoking Herb Grinder Spice Herbal Hand Crank Crusher Accessories maconha christmas navidad', 'Portable Metal Bracelet Smoking Pipe Herb Weed Pipe Smoke Tobacco Pipes For Cigarette Machine Smoking Accessories', 'Mini Beer Smoke Metal Pipes Portable Creative Smoking Pipe Herb Tobacco Pipes Gifts narguile Weed Grinder Smoke 6 colors Pipes', 'weed accessories Plate Discs For Smoke Bob Marley Herb Grinder weed Metal Tobacco Rolling Tray Storage Cigarette Holder Smoking', 'Manual Smoking Accessories Easy Hay Weed Tobacco Hemp Pepper Cans Spice Mill Crusher Household Grinding Gadgets #10', '3 Layer Plastic Tobacco Herb Grinder Patchwork Color Spice Crusher Case Gift Supply Tobacco Weed Herbal Cutter Shredder sale', 'Phlizon 1200w led grow light tent heater indoor weed growing flower seedling flowers lamp plant low watt adjustable rope 240v ac', '4-layer Aluminum Herbal Herb Tobacco Grinder Smoke Grinders Weed Grinders Smoking Pipe Accessorie', 'Revolver Pipe Weed Grinder Six Shooter Smoking Creative Tobacco Cigarette Herb Grinder Smoke Crusher 669', 'Nipple Smok Metal Pipes Creative Smoking Pipe Herb Tobacco Pipes Portable Gifts Weed Grinder Smoke Narguile Random Delivery', 'Mini Beer Smoke Metal Pipes Portable Creative Smoking Pipe Herb Tobacco Pipes Gifts Weed Grinder Smoke 6 colors Pipes K1160 F', '4 Layers Tobacco Grinder Herb Weed Grinder with Mill Handle Silver Color Smoke Grinder Metal Kitchen Gadgets', '3 Layers Zinc Alloy Star Wars Death Star Grinder Weed Herb Tobacco Crusher Grinder Cigarettes Accessories WIith Box', 'Multifunctional 3in1 Stainless Steel Smoking Tobacco Pipe Cleaner Cleaning Tool Smoking Accessories Weed Accessories New', 'Formax420 15*45*83MM CNC All In One Aluminum Container with Hitter Black Color', '4-layer Aluminum Grinder Crusher Crank Leaf Herbal Herb Machine Weed Tobacco Grinder Smoke Grinders Pipe Accessories Gadget J#1', 'Grinder 4 Layers Herb Weeds Smoking Muller Grass Spice Smoke Crusher Aluminium Crank Pollinator Hand Tobacco weed Accessories', 'Comb Shape Weed Storage Box Weed Accessories for Marijuanna Cannabiss Weed Smoking Accessories Smoking Pipe Herb Grinder', 'Plastic Tobacco Herb Grinder 3 Layers Herb Crusher Grinder Weed With Pollen Catcher Tobacco Storage Case Weed Accessories', 'New Wooden 2PC HERB / SPICE / GRASS / WEED Tobacco Herb Grinder For Smoking Pipe GR118a', 'Roll Tray Storage Plate Discs Raw Roll Paper Smoking Pipe Smoke Weed Accessories Herb Grinder Hookah Kaloud Chicha Glass Blunt', 'Rick and Morty Cartoon Sound Shape White Polished Edge Aluminum Ally Metal Herb Grinder Weed', 'PROSTORMER Electric Hedge Trimmer Pruning Shears 20V Cordless 2000mAh Rechargeable Weeding Hedge Household Mower Garden Tools', '78mm 110mm Weed Rolling Machine plastic tapered cigarette makerManual DIY Hand The horn Easy Smoking Tobacco Filling Cone', '180*120mm table small bob marly metal cigarette smoking raw tobacco joint weed rolling paper tin tray storage', 'Smoking Smell Proof Bag PU Leather Tobacco Pouch with Lock for Weed Herb Odor Proof Stash Container Case Storage', '250 Pieces (50 Packs) Silver Hookah Filter bong weed pipe fittings 3/4" Pipe Metal Filters Tobacco Smoking Pipe Screens', '4 In 1 Piece Zinc Alloy Metal Herb Grinder Mills Tobacco Spice Weed Grinder Crusher With Free Scraper', '1PC Pipe+1PC Tobacco+1PC Mesh Pocket Pipe Smoking Herb/weeds/ Pipe Tobacco Pipe With Grinder Mesh Filter @X', '4-layer Smoking Pipe Aluminum Herbal Herb Tobacco Grinder Smoke Grinders Weed Grinders Smoking Pipe Accessorie 2020', 'Formax420 Pull Tops All In One Aluminum Container Color Send Randomly', 'Multifunctional 3in1 Stainless Steel Smoking Tobacco Pipe Cleaner Cleaning Tool Smoking Accessories Weed Accessories', '4 Layes 40mm Metal Herbal Herb Tobacco Grinder Spice Weed Grinders Smoking Pipe Accessories Gold Smoke Cutter #T5P', 'Metal Tobacco Weed Pipe Magic Novelty Gift for women Hookah Grinder Narguile Cigarette Smoking Pipes', 'Hot Sale Mini 1pc Silvery Creative Metal Pipe Jamaica Rasta Reggae Style Herb Tobacco Smoking Pipes Weed Grinder for Men Gift', '18*12.5 cm table small women cigarette joint smoking dish metal tin tobacco weed rolling paper tray storage C106', 'Mini Mushroom smoke Metal Pipes Portable Creative Smoking Pipe Herb Tobacco Pipes Gifts Narguile Weed Grinder Smoke Random Color', 'Grinder Weed Smoking Pipes Skull Zinc Alloy Metal Bowl Smoking Hand Spoon Pipe Tobacco Fit Dry Herb Pipes Smoking Smoke', 'VERIDICAL 5 pairs/lot men short socks wool merino thermal warm socks winter thick weed socks Good Quality meia masculina solid', 'Vintage Durable Woody Break in Tobacco Pipe for Smoking Tube grinder weed accessories Smoking Pipe Weed Holder', 'New 1pcs Wood Smoking Pipe Portable Herb Tobacco Pipes Grinder Smoke Weed Pipes Smoke BY026', 'Quality 10PCS Smoking Pipe Metal Ball Stainless Steel Filter Screen Crystal Pipes Filter Mesh Smoking Weed Tobacco Accessories', 'Aluminum Smoke Metal Pipes Disguised Herb Tobacco Pipes Smoking Smoke Portable Grinder Weed Smoking Pipes', '1Pc Creative Battery Shaped Metal Zinc Alloy Herbal Herb Tobacco Grinder Weed Spice Cigarette Smoking Tools', 'New 1pcs Electronic Herb Grinder With Pollen Catcher For Tobacco Weed Crusher Cracker, Blue, Zinc Alloy 6colors Gr1121', '200g/0.01g Pocket Scale 500g/0.1g for Hookah Shisha Chicha Water Pipe Glass Pipe Tobacco Pipe Herb Weed Grinder', 'Xin Jia Yi Packaging Weed 3.5g Jar Label Sticker In Stock Small Plastic Lid Tin Can', 'Metal Bracelet Smoking Pipe Herb Weed Pipe Smoke Tobacco Pipes For Cigarette Machine Smoking Accessories New']


prices = ['US $1.42 - 2.76', 'US $0.82 - 2.32', 'US $1.78 - 1.90', 'US $1.11', 'US $2.07 - 3.20', 'US $3.77 - 4.29', 'US $1.58', 'US $1.25', 'US $4.98 - 6.99', 'US $1.77', 'US $30.42 - 40.57', 'US $1.14 - 3.64', 'US $0.89', 'US $1.62 - 1.63', 'US $0.84', 'US $2.20 - 4.26', 'US $1.37 - 2.81', 'US $1.39 - 1.78', 'US $131.99', 'US $0.68', 'US $4.70', 'US $1.34', 'US $1.86', 'US $2.84 - 2.98', 'US $1.99', 'US $0.64', 'US $11.27', 'US $2.35 - 3.30', 'US $4.08 - 4.15', 'US $8.99 - 10.99', 'US $0.63', 'US $2 - 4.30', 'US $2.77 - 5', 'US $7.95', 'US $74.99 - 108.99', 'US $1.80 - 3.19', 'US $2.81', 'US $13.99', 'US $2.16', 'US $2.12 - 3.26', 'US $1.25 - 2.50', 'US $1.20 - 2.80', 'US $10.33', 'US $0.29', 'US $2.67 - 3.03', 'US $1.59 - 1.60', 'US $2.38', 'US $0.90 - 1', 'US $0.77', 'US $1.97 - 2.12', 'US $12.16', 'US $0.69', 'US $2', 'US $1.72', 'US $1.60', 'US $4.43', 'US $5', 'US $4.90 - 5.84', 'US $0.34', 'US $1.71 - 1.82']


ratings = [' 4.6', ' 5.0', ' 4.5', ' 4.6', ' 4.8', ' 4.7', ' 4.4', ' 4.6', ' 4.7', ' 4.7', ' 4.9', ' 4.5', ' 4.6', ' 4.5', ' 4.5', ' 4.6', ' 5.0', ' 4.6', ' 5.0', ' 5.0', ' 5.0', ' 4.4', ' 4.9', ' 4.6', ' 5.0', ' 1.0', ' 4.8', ' 4.7', ' 4.8', ' 4.7', ' 4.8', ' 4.7', ' 4.6', ' 4.8', ' 4.3', ' 4.7', ' 4.8', ' 5.0', ' 4.8', ' 5.0', ' 5.0', ' 4.9', ' 3.5', ' 4.8', ' 5.0', ' 4.9', ' 4.7', ' 4.7', ' 4.9', ' 4.8', ' 4.9', ' 4.2', ' 4.3', ' 4.0', ' 4.6', ' 4.8', '-', '-', '-', '-']


sold = ['1348 Sold', '171 Sold', '466 Sold', '382 Sold', '118 Sold', '273 Sold', '60 Sold', '459 Sold', '2011 Sold', '1320 Sold', '347 Sold', '596 Sold', '318 Sold', '165 Sold', '232 Sold', '242 Sold', '69 Sold', '218 Sold', '4 Sold', '53 Sold', '18 Sold', '48 Sold', '93 Sold', '24 Sold', '133 Sold', '24 Sold', '3 Sold', '101 Sold', '648 Sold', '52 Sold', '210 Sold', '32 Sold', '535 Sold', '56 Sold', '183 Sold', '42 Sold', '283 Sold', '250 Sold', '78 Sold', '233 Sold', '95 Sold', '102 Sold', '4 Sold', '246 Sold', '43 Sold', '41 Sold', '72 Sold', '158 Sold', '135 Sold', '109 Sold', '35 Sold', '3 Sold', '62 Sold', '296 Sold', '25 Sold', '66 Sold', '80 Sold', '523 Sold', '1 Sold', '46 Sold']

#listoflists = zip(titles, prices, ratings, sold)
print(len(titles))
print(len(prices))
print(len(ratings))
print(len(sold))

#df = pd.DataFrame({'Count': [83, 19, 20]})
#result.index += 1
df = pandas.DataFrame({'Product': titles, 'Price': prices, 'Rating':ratings, '# Sold':sold})
df.index += 1
df.to_csv('testcsv.csv', index=True)