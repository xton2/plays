def includeme(config):
    config.add_route('plays', '/plays')
    config.add_route('getPlay', '/plays/{play}')
    config.add_route('getPlayAct', '/plays/{play}/act/{act}')
    config.add_route('getPlaySpeaker', '/plays/{play}/speaker/{speaker}')
    config.add_route('getPlayActScene', '/plays/{play}/act/{act}/scene/{scene}')
