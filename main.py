def on_up_pressed():
    if mySprite.vy == 0:
        mySprite.vy = -185
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

def on_a_pressed():
    if mySprite.vy == 0:
        mySprite.vy = -145
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    tiles.set_tilemap(tilemap("""
        level16
    """))
    mySprite.set_position(0, 14)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile29
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile21
    """),
    on_overlap_tile4)

def flipHorizontal():
    mySprite.image.flip_x()
    pause(100)

def on_overlap_tile5(sprite, location):
    mySprite.vy = -500
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite, location):
    mySprite.set_position(0, 16)
    tiles.set_tilemap(tilemap("""
        level8
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile6)

def on_overlap_tile7(sprite, location):
    mySprite.set_position(0, 14)
    tiles.set_tilemap(tilemap("""
        level10
    """))
    scene.set_background_color(8)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile27
    """),
    on_overlap_tile7)

def on_overlap_tile8(sprite, location):
    tiles.set_tilemap(tilemap("""
        level1
    """))
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile8)

def on_overlap_tile9(sprite, location):
    tiles.set_tilemap(tilemap("""
        level3
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile26
    """),
    on_overlap_tile9)

def on_overlap_tile10(sprite, location):
    tiles.set_tilemap(tilemap("""
        level2
    """))
    mySprite.set_position(70, 120)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile28
    """),
    on_overlap_tile10)

mySprite: Sprite = None
scene.set_background_color(9)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f f f . . . 
            . . . . f e e e e e e e e f . . 
            . . . f e e e e e e f e e f . . 
            . . f f e e e e e e e e e f . . 
            . . f e f e e e e e e e e 4 4 . 
            . . f e e f e e e e e e e 4 4 . 
            . . f e e e f e e e f f f . . . 
            . . f e e e f e e e 4 4 f . . . 
            . . f e e e f e e f 4 4 f . . . 
            . . f e e e f e e f 4 4 f . . . 
            . . f e e e f e e f 4 4 f . . . 
            . . f f f f f f f f f f . . . . 
            . . . . . 4 . . . . 4 . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 0)
tiles.set_tilemap(tilemap("""
    level1
"""))
mySprite.ay = 200
scene.camera_follow_sprite(mySprite)
