tuple_1 = (1, 2, 3)
tuple_2 = ('one', 'hello')
tuple_3 = (3, 2.3, 'three')

print(tuple_1[1])
print(type(tuple_1))
print(tuple_2)
print(tuple_3)


computer = {
    'CPU': 'AMD',
    'RAM': 16000,
    'SDD': 240,
    'VideoCard': 'GeForce 1080ti',
    'size': {'width': 350, 'height': 560, 'length': 420}
}

pc_tuple = ('CPU: AMD', 'RAM: 16000', 'SDD: 240', 'VideoCard: GeForce 1080ti')
cpu, ram, ssd, vga = pc_tuple
print(cpu, ram, ssd, vga )