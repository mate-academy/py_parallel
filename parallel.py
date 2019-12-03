'''
Module
'''


class Box:
    '''
    Class for representing the box
    '''

    def __init__(self, length, width, height):
        '''
        :param length:
        :param width:
        :param height:
        '''
        self.length = length
        self.width = width
        self.heigth = height

    def get_length(self):
        '''
        Return length of box
        :return:
        '''
        return self.length

    def get_height(self):
        '''
        Return height of box
        :return:
        '''
        return self.heigth

    def get_width(self):
        '''
        Return width of box
        :return:
        '''
        return self.width

    def get_volume(self):
        '''
        Return volume of box
        :return:
        '''
        return self.length * self.width * self.heigth
