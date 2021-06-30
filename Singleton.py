class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        print("Singleton call {}".format(cls)) # FIXME:
        if cls not in cls.__instances:
            print("Singleton instance {}".format(cls)) # FIXME:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]