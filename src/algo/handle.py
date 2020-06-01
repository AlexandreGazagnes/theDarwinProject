
def _save(Obj):
    """save an algo in redis"""
    pass


def _load(id):
    """rebuild and return an Object from json data in redis"""

    return None


def _run(id, n):
    """load run and save"""

    # obj = load("id")
    # obj.run(id)
    # save(obj)
    pass


def _ls() : 
    pass


def _change() : 
    pass


def _init() : 
    pass


class algo:
    ls = _ls
    change = _change
    load = _load
    save = _save
    run = _run
    init = _init
    # Algo = _Algo