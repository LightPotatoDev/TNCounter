#i should probably make this pickle or JSON or smth

item_amount_dict = {
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
    'Ocean ice':0,
    'Sky-blue ice':0,
    'Elixir of board kingdom':0,
    'Drop of shimmering sky':0,
    
    'Yellow key':0,
    'Blue key':0,
    'Crimson key':0,
    'Violet key':0,
    'Platinum key':0,
    'Winner\'s key':0,
    'Glory key':0,
    'Return key':0,
    'Ice key':0,
    
    'Old mattock':0,
    'Mattock':0,
    'Super mattock':0,
    'Hyper mattock':0,
    'Miracle mattock':0,
    
    'Swap orb':0,
    'Pavement orb':0,
    'Reclamation orb':0,
    'Glory orb':0,
    'Guidance orb':0,
    'Teleport orb':0,
    'Resurrection orb':0,
    'Reverse orb':0,
    'Blizzard orb':0,
    'Spring orb':0,
    
    'Golden feather 30%':0,
    'Golden feather 50%':0,
    'Golden feather 100%':0,
    'Golden feather x2':0,
    'Life crown 10%':0,
    'Life crown 20%':0,
    'Life crown 30%':0,
    'Life crown 100%':0,
    
    'Anchor hook 1':0,
    'Anchor hook 3':0,
    'Anchor hook 5':0,
    'Anchor hook 10':0,
    
    'Clock hand':0,
    
    'Magic elixir':0
}

item_value_dict = {
    'Power piece':              {'Atk':1},
    'Power gem':                {'Atk':2},
    'Power potion':             {'Atk':3, 'Hp':300},
    'Power card':               {'Atk':5},
    'Power deck':               {'Atk':15},
    'Pulse book [Sword]':       {'Atk':50},
    
    'Guard piece':              {'Def':1},
    'Guard gem':                {'Def':2},
    'Guard potion':             {'Def':3, 'Hp':300},
    'Guard card':               {'Def':5},
    'Guard deck':               {'Def':15},
    'Pulse book [Shield]':      {'Def':50},
    
    'Red potion':               {'Hp':200},
    'Blue potion':              {'Hp':800},
    'Life potion':              {'Hp':2000},
    'Heavenly potion':          {'Atk':3, 'Def':3, 'Hp':3000},
    'Drop of dream ocean':      {'Atk':5, 'Def':5, 'Hp':10000}, #disclaimer: 10000 instead of 9999 for better readability
    'Immortal potion':          {'Atk':15, 'Def':15, 'Hp':50000},
    
    'Old mattock':              {'Mattock':5},
    'Mattock':                  {'Mattock':10},
    'Super mattock':            {'Mattock':20},
    'Hyper mattock':            {'Mattock':40},
    'Miracle mattock':          {'Mattock':99}
}