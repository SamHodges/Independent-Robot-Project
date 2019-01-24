cell = Cell.ll('wlan0')[0]
scheme  = Scheme.for_cell('wla00n0', 'ASUS', cell, passkey)
scheme.save()
scheme.activate()

scheme.all()
