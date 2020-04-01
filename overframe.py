class textFrame:
    '''
    class for text frames with different align
    '''
    def __init__(
                self,
                own_template=None, align='left', scr_width=80, fill_with=' '):
        self.version = '1.01'
        self._commands = [
                         'right', 'rjust', 'r',
                         'left', 'ljust', 'l',
                         'center', 'c',
                        ]
        self.ordinary_template = '┌─┐└─┘││'
        self.double_template = '╔═╗╚═╝║║'
        self.light_shadow_template = '┌─╖╘═╝│║'
        self.shadow_template = '┌─ └▄█│█'
        self.align = align.lower() if align in self._commands else 'left'
        self.width = scr_width if int(scr_width) in range(1, 255) else 80
        self.fill = fill_with if len(fill_with) == 1 else fill_with[0]

    def ordinary(self, text):
        self.__print_me(text, self.ordinary_template)

    def doubled(self, text):
        self.__print_me(text, self.double_template)

    def light_shadow(self, text):
        self.__print_me(text, self.light_shadow_template)

    def shadow(self, text):
        self.__print_me(text, self.shadow_template)

    def __print_me(self, text, template):
        t = template
        s = len(text)
        up = t[0] + t[1]*s + t[2]
        ct = t[-2] + text + t[-1]
        dn = t[3] + t[4]*s + t[5]
        if self.align in ['left', 'ljust', 'l']:
            t = '{}'.format(up).ljust(self.width, self.fill) + '\n'
            t += '{}'.format(ct).ljust(self.width, self.fill) + '\n'
            t += '{}'.format(dn).ljust(self.width, self.fill)
        elif self.align in ['center', 'c']:
            t = '{}'.format(up).center(self.width, self.fill) + '\n'
            t += '{}'.format(ct).center(self.width, self.fill) + '\n'
            t += '{}'.format(dn).center(self.width, self.fill)
        elif self.align in ['right', 'rjust', 'r']:
            t = '{}'.format(up).rjust(self.width, self.fill) + '\n'
            t += '{}'.format(ct).rjust(self.width, self.fill) + '\n'
            t += '{}'.format(dn).rjust(self.width, self.fill)
        print(t)


if __name__ == '__main__':
    c = textFrame(align='center')
    c.ordinary(' This is "overframe" 1.0 unit ')
    c.doubled(' For making different frames ')
    c.light_shadow('  F R A M E S   W I T H   L I G H T   S H A D O W  ')
    c.shadow(' F R A M E S   W I T H    N O R M A L   S H A D O W S  ')
    c.doubled(' Version: {} '.format(c.version))
