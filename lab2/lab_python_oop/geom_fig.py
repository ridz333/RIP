from abc import ABCMeta, abstractmethod


class Fig(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass