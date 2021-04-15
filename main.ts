controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.vy = -185
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.vy = -185
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite, location) {
    game.over(false)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.vy = -145
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite, location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile29`, function (sprite, location) {
    tiles.setTilemap(tilemap`level16`)
    mySprite.setPosition(0, 14)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile21`, function (sprite, location) {
    game.over(false)
})
function flipHorizontal () {
    mySprite.image.flipX()
    pause(100)
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile2`, function (sprite, location) {
    mySprite.vy = -500
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile5`, function (sprite, location) {
    mySprite.setPosition(0, 16)
    tiles.setTilemap(tilemap`level8`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile27`, function (sprite, location) {
    mySprite.setPosition(0, 14)
    tiles.setTilemap(tilemap`level10`)
    scene.setBackgroundColor(8)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleRedCrystal, function (sprite, location) {
    tiles.setTilemap(tilemap`level1`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile26`, function (sprite, location) {
    tiles.setTilemap(tilemap`level3`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile28`, function (sprite, location) {
    tiles.setTilemap(tilemap`level2`)
    mySprite.setPosition(70, 120)
})
let mySprite: Sprite = null
scene.setBackgroundColor(9)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 0)
tiles.setTilemap(tilemap`level1`)
mySprite.ay = 200
scene.cameraFollowSprite(mySprite)
