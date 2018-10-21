from mathematica.random_functions import RandomChoice, RandomReal

_nList, _timeList = [], []
for i in range(0, 1000):
    _n, _time = 0, 0
    while True:
        _n += 1
        _rand = RandomReal()
        if 0 <= _rand < 1 / 3:
            _time += 2
            break
        elif 1 / 3 <= _rand < 2 / 3:
            _time += 3
        elif 2 / 3 <= _rand <= 1:
            _time += 5
    _timeList.append(_time)
    _nList.append(_n)
print(sum(_timeList) / _timeList.__len__())
print(sum(_nList) / _nList.__len__())
