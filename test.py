from mathematica.load_all_functions import *

for i in range(0, 10):
    __size = 200
    __list = RandomSample(Range(0, __size), __size)
    QuickSortTrack(__list, 'D:\\Mathematica Files 4K\\sheldon_ross\\sheldon_ross_chapter_03\\sheldon_ross_example_3.16\\sheldon_ross_example_3.16_animation_data_' + f'{i:03}' + '.txt')