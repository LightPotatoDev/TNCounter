itemDict = {
    'Power piece':0,
    'Power gem':0,
    'Power potion':0,
    'Power card':0,
    'Power deck':0,
    'Pulse book [Sword]':0,
    'Continental badge [Sword]':0,
    
    'Guard piece':0,
    'Guard gem':0,
    'Guard potion':0,
    'Guard card':0,
    'Guard deck':0,
    'Pulse book [Shield]':0,
    'Continental badge [Shield]':0,
    
    'Red potion':0,
    'Blue potion':0,
    'Life potion':0,
    'Heavenly potion':0,
    'Drop of dream ocean':0,
    'Immortal potion':0,
    'Continental potion':0,
    'Eternal potion':0,
    
    'Yellow key':0,
    'Blue key':0,
    'Crimson key':0,
    'Violet key':0,
    'Platinum key':0,
    'Winner\'s key':0,
    'Glory key':0,
    'Return key':0,
    'Ice key':0,
    
    'Swap orb':0,
    'Pavement orb':0,
    'Teleport orb':0,
    'Reverse orb':0,
    'Blizzard orb':0,
    
    'Golden feather 30%':0,
    'Golden feather x2':0,
    'Life crown 30%': 0,
    'Life crown 100%': 0
    
}

itemValueDict = {
    #atk, def, hp
    'Power piece':(1,0,0),
    'Power gem':(2,0,0),
    'Power potion':(3,0,300),
    'Power card':(5,0,0),
    'Power deck':(15,0,0),
    'Pulse book [Sword]':(50,0,0),
    
    'Guard piece':(0,1,0),
    'Guard gem':(0,2,0),
    'Guard potion':(0,3,300),
    'Guard card':(0,5,0),
    'Guard deck':(0,15,0),
    'Pulse book [Shield]':(0,50,0),
    
    'Red potion':(0,0,200),
    'Blue potion':(0,0,800),
    'Life potion':(0,0,2000),
    'Heavenly potion':(3,3,3000),
    'Drop of dream ocean':(5,5,10000), #disclaimer: 10000 instead of 9999 for better readability
    'Immortal potion':(15,15,50000),
}

def calculate_stats(itemAmount):
    stats = [0,0,0]
    for name,value in itemValueDict.items():
        for i in range(3):
            stats[i] += itemAmount[name]*value[i]
            
    return stats